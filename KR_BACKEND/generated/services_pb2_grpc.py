# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services_pb2 as services__pb2


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadFile = channel.unary_unary(
                '/myapp.FileService/UploadFile',
                request_serializer=services__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=services__pb2.UploadFileResponse.FromString,
                )
        self.DownloadFile = channel.unary_unary(
                '/myapp.FileService/DownloadFile',
                request_serializer=services__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=services__pb2.DownloadFileResponse.FromString,
                )


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=services__pb2.UploadFileRequest.FromString,
                    response_serializer=services__pb2.UploadFileResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=services__pb2.DownloadFileRequest.FromString,
                    response_serializer=services__pb2.DownloadFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'myapp.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/myapp.FileService/UploadFile',
            services__pb2.UploadFileRequest.SerializeToString,
            services__pb2.UploadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/myapp.FileService/DownloadFile',
            services__pb2.DownloadFileRequest.SerializeToString,
            services__pb2.DownloadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
