from concurrent import futures
import logging

import grpc
import pb.learner.learner_pb2 as learner_pb2
import pb.learner.learner_pb2_grpc as learner_pb2_grpc
from learner.learner import Learner

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    learner_pb2_grpc.add_LearnerServicer_to_server(Learner(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
