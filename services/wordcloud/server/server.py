from concurrent import futures
import logging

import grpc
# import pb.wordcloud.wordcloud_pb2 as wordcloud_pb2
import pb.wordcloud.wordcloud_pb2_grpc as wordcloud_pb2_grpc
from server.wordcloud import Wordcloud

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wordcloud_pb2_grpc.add_WordcloudServicer_to_server(Wordcloud(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()
