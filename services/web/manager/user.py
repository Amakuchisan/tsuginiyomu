import grpc

import pb.manager.manager_pb2 as manager_pb2
import pb.manager.manager_pb2_grpc as manager_pb2_grpc

def update_wordcloud(hatena_id: str, wordcloud):
    with grpc.insecure_channel('manager:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.UpdateWordcloud(manager_pb2.UpdateWordcloudRequest(hatenaID=hatena_id, wordcloud=wordcloud))
    # return response # -> manager_pb2.UpdateWordcloudRequest()

def create(hatena_id: str) -> manager_pb2.CreateUserRequest():
    with grpc.insecure_channel('manager:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.CreateUser(manager_pb2.CreateUserRequest(hatenaID=hatena_id))
    return response
