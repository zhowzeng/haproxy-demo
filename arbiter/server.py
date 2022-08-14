from concurrent import futures
import logging

import grpc
import arbiter_pb2
import arbiter_pb2_grpc


class Arbiter(arbiter_pb2_grpc.ArbiterServicer):

    def CallArbiter(self, request, context):
        logging.info("HA")
        return arbiter_pb2.ArbiterResponse(res='this is a response from arbiter')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    arbiter_pb2_grpc.add_ArbiterServicer_to_server(Arbiter(), server)
    server.add_insecure_port('[::]:2222')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    serve()
