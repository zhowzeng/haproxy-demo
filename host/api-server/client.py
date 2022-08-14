from __future__ import print_function

import logging

import grpc
import api_pb2
import api_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:5566') as channel:
        stub = api_pb2_grpc.ApiStub(channel)
        response = stub.CallApi(api_pb2.ApiRequest(
            req='this is a request from client'))
    logging.info(f"\tReceived: {response.res}")


if __name__ == '__main__':
    logging.basicConfig(level=1)
    run()
