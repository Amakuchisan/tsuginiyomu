import grpc

import pb.manager.manager_pb2 as manager_pb2
import pb.manager.manager_pb2_grpc as manager_pb2_grpc

def create(hatena_id: str, url: list[str]) -> list[str]:
    with grpc.insecure_channel('manager:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.CreateArticle(manager_pb2.CreateArticleRequest(hatenaID=hatena_id, url=url))
    return response.new_created_url

def createArticleModel(url: str, wordCount: dict[str, int]) -> manager_pb2.Article():
    article = manager_pb2.Article()
    article.url = url
    article.word_count.update(wordCount)
    return article
