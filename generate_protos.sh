#!/bin/bash
for FILE in proto/*.proto;
do
    echo "Generating protocols for ${FILE}"
    python -m grpc_tools.protoc --experimental_allow_proto3_optional -I./proto --python_out=src/druncschema --grpc_python_out=src/druncschema ${FILE}
    FILE_NAME=$(basename -- "$FILE")
    CLASS_NAME="${FILE_NAME%.*}"
    PY_OUT_FILE_NAME="src/druncschema/${CLASS_NAME}_pb2_grpc.py"
    # echo "FILE_NAME        " $FILE_NAME
    # echo "CLASS_NAME       " $CLASS_NAME
    # echo "PY_OUT_FILE_NAME " $PY_OUT_FILE_NAME
    # echo "s/import ${CLASS_NAME}_pb2/import drunc.communication.${CLASS_NAME}_pb2/"
    sed -i '' "/google/! s/import \(.*_pb2\)/import druncschema.\1/" ${PY_OUT_FILE_NAME}
    PY_OUT_FILE_NAME="src/druncschema/${CLASS_NAME}_pb2.py"
    sed -i '' "/google/! s/import \(.*_pb2\)/import druncschema.\1/" ${PY_OUT_FILE_NAME}
done


