import grpc

import pb.learner.learner_pb2 as learner_pb2
import pb.learner.learner_pb2_grpc as learner_pb2_grpc

def learn(hatena_id: str):
    with grpc.insecure_channel('learner:50050') as channel:
        stub = learner_pb2_grpc.LearnerStub(channel)
        response = stub.Learn(learner_pb2.LearnRequest(hatena_id=hatena_id))

def create_wordcloud(hatena_id: str) -> bytes:
    with grpc.insecure_channel('learner:50050') as channel:
        stub = learner_pb2_grpc.LearnerStub(channel)
        response = stub.CreateWordCloud(learner_pb2.CreateWordCloudRequest(hatena_id=hatena_id))
    return response.wordcloud

def get_suggestion(hatena_id: str) -> learner_pb2.Suggestion:
    with grpc.insecure_channel('learner:50050') as channel:
        stub = learner_pb2_grpc.LearnerStub(channel)
        response = stub.GetSuggestion(learner_pb2.GetSuggestionRequest(hatena_id=hatena_id))
    return response.suggestions

def exists_hatena_id(hatena_id: str) -> bool:
    with grpc.insecure_channel('learner:50050') as channel:
        stub = learner_pb2_grpc.LearnerStub(channel)
        response = stub.ExistsHatenaID(learner_pb2.ExistsHatenaIDRequest(hatena_id=hatena_id))
    return response.existed
