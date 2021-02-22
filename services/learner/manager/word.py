import grpc

import pb.manager.manager_pb2 as manager_pb2
import pb.manager.manager_pb2_grpc as manager_pb2_grpc

# 辞書型で返却
def find_word(hatena_id: str) -> dict[str, int]:
    with grpc.insecure_channel('manager:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.GetWord(manager_pb2.GetWordRequest(hatenaID=hatena_id))
    return response.wordCount

def create(article: manager_pb2.Article()):
    with grpc.insecure_channel('manager:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.CreateWord(createRequest(article))

def createRequest(article: manager_pb2.Article()) -> manager_pb2.CreateWordRequest():
    req = manager_pb2.CreateWordRequest()
    req.article.extend(article)
    return req
