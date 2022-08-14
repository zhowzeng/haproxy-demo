from concurrent import futures
import logging

import grpc
import api_pb2
import api_pb2_grpc


class Api(api_pb2_grpc.ApiServicer):

    def CallApi(self, request, context):
        logging.info("HA")
        return api_pb2.ApiResponse(res='this is a response from api')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    api_pb2_grpc.add_ApiServicer_to_server(Api(), server)
    server.add_insecure_port('[::]:2244')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    serve()
