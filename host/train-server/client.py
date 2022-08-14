from __future__ import print_function

import logging

import grpc
import train_pb2
import train_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:5566') as channel:
        stub = train_pb2_grpc.TrainStub(channel)
        response = stub.CallTrain(train_pb2.TrainRequest(
            req='this is a request from client'))
    logging.info(f"\tReceived: {response.res}")


if __name__ == '__main__':
    logging.basicConfig(level=1)
    run()
