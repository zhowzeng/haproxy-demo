from __future__ import print_function

import logging

import grpc
import arbiter_pb2
import arbiter_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:5555') as channel:
        stub = arbiter_pb2_grpc.ArbiterStub(channel)
        response = stub.CallArbiter(arbiter_pb2.ArbiterRequest(
            req='this is a request from client'))
    logging.info(f"\tReceived: {response.res}")


if __name__ == '__main__':
    logging.basicConfig(level=1)
    run()
