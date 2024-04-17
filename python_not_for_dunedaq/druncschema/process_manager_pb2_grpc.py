# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from druncschema import request_response_pb2 as druncschema_dot_request__response__pb2


class ProcessManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.describe = channel.unary_unary(
                '/dunedaq.druncschema.ProcessManager/describe',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )
        self.boot = channel.unary_unary(
                '/dunedaq.druncschema.ProcessManager/boot',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )
        self.restart = channel.unary_unary(
                '/dunedaq.druncschema.ProcessManager/restart',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )
        self.kill = channel.unary_unary(
                '/dunedaq.druncschema.ProcessManager/kill',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )
        self.flush = channel.unary_unary(
                '/dunedaq.druncschema.ProcessManager/flush',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )
        self.ps = channel.unary_unary(
                '/dunedaq.druncschema.ProcessManager/ps',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )
        self.logs = channel.unary_stream(
                '/dunedaq.druncschema.ProcessManager/logs',
                request_serializer=druncschema_dot_request__response__pb2.Request.SerializeToString,
                response_deserializer=druncschema_dot_request__response__pb2.Response.FromString,
                )


class ProcessManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def describe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def boot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def restart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def kill(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def flush(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProcessManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'describe': grpc.unary_unary_rpc_method_handler(
                    servicer.describe,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
            'boot': grpc.unary_unary_rpc_method_handler(
                    servicer.boot,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
            'restart': grpc.unary_unary_rpc_method_handler(
                    servicer.restart,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
            'kill': grpc.unary_unary_rpc_method_handler(
                    servicer.kill,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
            'flush': grpc.unary_unary_rpc_method_handler(
                    servicer.flush,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
            'ps': grpc.unary_unary_rpc_method_handler(
                    servicer.ps,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
            'logs': grpc.unary_stream_rpc_method_handler(
                    servicer.logs,
                    request_deserializer=druncschema_dot_request__response__pb2.Request.FromString,
                    response_serializer=druncschema_dot_request__response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dunedaq.druncschema.ProcessManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProcessManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def describe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dunedaq.druncschema.ProcessManager/describe',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def boot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dunedaq.druncschema.ProcessManager/boot',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def restart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dunedaq.druncschema.ProcessManager/restart',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def kill(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dunedaq.druncschema.ProcessManager/kill',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def flush(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dunedaq.druncschema.ProcessManager/flush',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dunedaq.druncschema.ProcessManager/ps',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def logs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dunedaq.druncschema.ProcessManager/logs',
            druncschema_dot_request__response__pb2.Request.SerializeToString,
            druncschema_dot_request__response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
