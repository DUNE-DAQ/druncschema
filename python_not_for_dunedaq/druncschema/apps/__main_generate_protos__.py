import importlib
import logging
import os
import subprocess
from pathlib import Path

import click
from rich.console import Console
from rich.logging import RichHandler

log_levels = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "NOTSET": logging.NOTSET,
}
log = logging.getLogger("druncschema-generate-protos")
try:
    width = os.get_terminal_size()[0]
except:
    width = 150
log.addHandler(RichHandler(
    console=Console(width=width),
    omit_repeated_times=False,
    markup=True,
    rich_tracebacks=True,
    show_path=False,
    tracebacks_width=width,
))

compiled_extensions = ["_pb2.py", "_pb2.pyi", "_pb2_grpc.py"]
def in_dev_mode():
    """Validates dev mode by attempting to import a library that otherwise would not be a part of the stack"""
    if importlib.util.find_spec("mypy_protobuf"):
        return True
    else:
        return False

def generate_protos(source_path: Path, druncschema_root: Path, proto_files: list[Path], output_dir: Path, subdir: Path) -> None:
    """Compiles the protobuf messages"""
    for proto_file in proto_files:
        log.info(f"Processing file {str(proto_file)} to output dir {str(output_dir)}")
        if not str(proto_file).endswith(".proto"):
            raise Exception(f"File names must end in a '.proto', received {proto_file}")
        try:
            cmd = " ".join([
                f"source {source_path}; cd {druncschema_root}; "
                "python -m grpc_tools.protoc",
                "-I'./schema'",
                f"--python_out={str(output_dir)}",
                f"--grpc_python_out={str(output_dir)}",
                f"--mypy_out={str(output_dir)}",
                str(proto_file)
            ])
            log.debug(cmd)
            subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True, executable='/bin/bash')
        except subprocess.CalledProcessError as e:
            log.exception(e)
            log.error(e.stderr)
        output_files = [output_dir / Path("druncschema") / subdir / Path(Path(proto_file.name).stem + extension) for extension in compiled_extensions]
        for output_file in output_files:
            if not output_file.exists():
                log.error(output_file)
                e = ValueError(f"Could not find output file {output_file}.")
                log.exception(e)
            else:
                log.debug(f"Generated {output_file}")
    return

def clear_previous_compiled_schema(output_dir: Path, output_files: list[Path]) ->None:
    for output_file in output_files:
        for compiled_extension in compiled_extensions:
            existing_file = output_dir / output_file.with_name(output_file.stem + compiled_extension)
            if existing_file.exists():
                log.info(f"Deleting file {existing_file}")
                existing_file.unlink()

def call_generate_protos(source_path: Path, druncschema_root: Path, output_dir: Path, subdir: Path, clean: bool, do_not_compile: bool) -> None:
    """Finds all the protobuf message schema definitions, calls the compiling function generate_protos"""
    proto_relative_path = Path("schema/druncschema")
    proto_files = [proto_relative_path / subdir / Path(f.name) for f in (druncschema_root / proto_relative_path / subdir).glob("*.proto")]
    if not proto_files:
        return
    if clean:
        clear_previous_compiled_schema(output_dir / Path("druncschema") / subdir, proto_files)
        if get_files(output_dir):
            e = Exception("Not all files removed, exiting")
            log.error(get_files(output_dir))
            log.exception(e)
    if not do_not_compile:
        generate_protos(source_path, druncschema_root, proto_files, output_dir, subdir)
    return

def get_subdirs(path: Path) ->list[str]:
    return [Path(p.name) for p in path.iterdir() if p.is_dir() and not str(p.name).endswith("__") and not str(p.name).endswith("apps")]

def get_files(path: Path) ->list[Path]:
    return [Path(p.name) for p in path.iterdir() if p.is_file() and not str(p.name).endswith("__.py") and not str(p.name).endswith("typed")]

@click.command() 
@click.option(
    "-l",
    "--log-level",
    type=click.Choice(log_levels.keys(), case_sensitive=False),
    default="INFO",
    help="Set the log level",
)
@click.option(
    "-c",
    "--clean",
    is_flag=True,
    help="Explicitly deletes the existing compiled schemas before starting the compile the new ones",
)
@click.option(
    "-d",
    "--do-not-compile",
    is_flag=True,
    help="Does not compile the schema. Only allowed with use of the clean flag",
)
def main(
    log_level: str,
    clean: bool,
    do_not_compile: bool
    ) -> None:
    """This script compiles the protobuf message schema into the relevant python code"""
    log.setLevel(log_level)

    if not in_dev_mode():
        e = Exception("This command is only available in developer mode. See the druncschema wiki for further clarification.")
        log.exception(e)
    if not any(path.endswith("/druncschema") for path in os.getenv("DUNEDAQ_DB_PATH").split(":")):
        e = Exception("druncschema not found in DUNEDAQ_DB_PATH, perhaps you forgot to dbt-build and dbt-workarea-env?")
        log.exception(e)
    if do_not_compile and not clean:
        e = Exception("Used option -d/--do-not-compile but not -c/--clean, require -c to use -d")
        log.exception(e)

    druncschema_root = Path([path for path in os.getenv("DUNEDAQ_DB_PATH").split(":") if path.endswith("/druncschema")][0])
    log.debug(f"Found druncschema directory at {druncschema_root}")

    output_dir = druncschema_root / "python_not_for_dunedaq/"
    log.debug(f"Set output directory as {output_dir}")

    source_path = druncschema_root.parents[1] / "env.sh"
    log.debug(f"Set source path to {source_path=}")

    subdir = Path("")
    call_generate_protos(source_path, druncschema_root, output_dir, subdir, clean, do_not_compile)

    subdirs = get_subdirs(druncschema_root / Path("schema/druncschema"))
    for subdir in subdirs:
        call_generate_protos(source_path, druncschema_root, output_dir, subdir, clean, do_not_compile)
