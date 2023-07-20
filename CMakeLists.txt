cmake_minimum_required(VERSION 3.12)
project(druncschema VERSION 0.0.0)

find_package(daq-cmake REQUIRED)

daq_setup_environment()

find_package(Protobuf REQUIRED)

daq_protobuf_codegen( *.proto )
#daq_grpc_codegen( *service.proto )

daq_add_library(*.cpp)

daq_install()
