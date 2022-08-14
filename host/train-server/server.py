from concurrent import futures
import logging

import grpc
import train_pb2
import train_pb2_grpc


class Train(train_pb2_grpc.TrainServicer):

    def CallTrain(self, request, context):
        logging.info("HA")
        return train_pb2.TrainResponse(res='this is a response from train')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    train_pb2_grpc.add_TrainServicer_to_server(Train(), server)
    server.add_insecure_port('[::]:2233')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    serve()
