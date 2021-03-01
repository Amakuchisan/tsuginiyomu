import grpc

import pb.manager.manager_pb2 as manager_pb2
import pb.manager.manager_pb2_grpc as manager_pb2_grpc

def create_user(hatena_id: str):
    with grpc.insecure_channel('manager:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.CreateUser(manager_pb2.CreateUserRequest(hatenaID=hatena_id))
    return response
