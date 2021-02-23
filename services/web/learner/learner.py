import grpc

import pb.learner.learner_pb2 as learner_pb2
import pb.learner.learner_pb2_grpc as learner_pb2_grpc

def learn(hatena_id: str):
    with grpc.insecure_channel('learner:50050') as channel:
        stub = learner_pb2_grpc.LearnerStub(channel)
        response = stub.Learn(learner_pb2.LearnRequest(hatena_id=hatena_id))

def create_wordcloud(hatena_id: str):
    with grpc.insecure_channel('learner:50050') as channel:
        stub = learner_pb2_grpc.LearnerStub(channel)
        response = stub.CreateWordCloud(learner_pb2.CreateWordCloudRequest(hatena_id=hatena_id))
    return response.wordcloud
