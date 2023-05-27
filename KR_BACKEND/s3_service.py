from KR_BACKEND.generated import services_pb2 as pb2
from KR_BACKEND.generated import services_pb2_grpc as pb2_grpc
import grpc
from concurrent import futures

class S3ServiceClient:
    def __init__(self, host, port):
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.FileServiceStub(channel)

    def upload_file(self, file_name, file_content):
        request = pb2.UploadFileRequest(file_name=file_name, file_content=file_content)
        response = self.stub.UploadFile(request)
        if response.success:
            return response.message
        else:
            raise Exception(response.message)

    def download_file(self, file_name):
        request = pb2.DownloadFileRequest(file_name=file_name)
        response = self.stub.DownloadFile(request)
        return response.file_content

    def get_file_content(self, file_name):
        request = pb2.DownloadFileRequest(file_name=file_name)
        response = self.stub.DownloadFile(request)
        return response.file_content

    def get_file_info(self, file_name):
        # Implement your logic to retrieve file information
        pass

class S3ServiceServer(pb2_grpc.FileServiceServicer):
    def UploadFile(self, request, context):
        # Implement your logic to handle file upload
        pass

    def DownloadFile(self, request, context):
        # Implement your logic to handle file download
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    pb2_grpc.add_FileServiceServicer_to_server(S3ServiceServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
