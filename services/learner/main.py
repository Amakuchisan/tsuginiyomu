# from __future__ import print_function
import logging

import grpc

import pb.learner.learner_pb2 as learner_pb2
import pb.learner.learner_pb2_grpc as learner_pb2_grpc
import pb.manager.manager_pb2 as manager_pb2
import pb.manager.manager_pb2_grpc as manager_pb2_grpc

def calc_feature(hatena_id: str):
    print("CNaan")
    url_list = ['https://please-sleep.cou929.nu/bash-strict-mode.html', 'https://wonderwall.hatenablog.com/entry/rust-command-line-tools', 'https://qiita.com/mrok273/items/58532c06a3af3324d970']
    print("url_list: ", url_list)
    articles = []
    for url in url_list:
        dic_list = {"Go": 3, "Python": 2, "Rust": 3}
        articles.append(createArticle(url, dic_list))
        # print(dic_list)
        # word.create(url, dic_list)
        # for dic in dic_list:
        #     if(word.find_name(dic[0]) is None):
        #         word.create(dic[0])
        #     article_word.create(dic[0], dic[1], url)
    req = createRequest(articles)
    print(req)

def run():
    calc_feature("CNaan")
    return
    # hatenaID = "John"
    # articleReq = []
    # url = "http://hogehoge.hoge"
    # d = {"Rust": 1, "Go": 2}
    # article = createArticle(url, d)
    # articleReq.append(article)

    # url = "http://fugafuga.fuga"
    # d = {"Rust": 2, "C++": 3}
    # article = createArticle(url, d)
    # articleReq.append(article)

    req = createRequest(hatenaID, articleReq)
    # print(req)
    # print(article)
    # url = ["http://hogehoge.hoge", "http://fugafuga.fuga"]
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        # response = stub.CreateUser(manager_pb2.CreateUserRequest(hatenaID = "John"))
        # response = stub.CreateArticle(manager_pb2.CreateArticleRequest(hatenaID = "John", url = url))
        response = stub.CreateWord(req)
        # response = stub.UpdateWordcloud(manager_pb2.UpdateWordcloudRequest(hatenaID='CNaan', wordcloud='abcd'.encode()))
        # response = stub.GetWord(manager_pb2.GetWordRequest(hatenaID='John'))
    print("Manager client received!")
    # print(response.hatenaID)
    print(response)
    # print(response.wordCount)
    # print(response.wordCount['Rust'])

def createArticle(url: str, wordCount) -> manager_pb2.Article():
# def createArticle(url: str, wordCount: dict[str, int]) -> manager_pb2.Article():
    article = manager_pb2.Article()
    article.url = url
    article.word_count.update(wordCount)
    return article

def createRequest(article: manager_pb2.Article()) -> manager_pb2.CreateWordRequest():
    req = manager_pb2.CreateWordRequest()
    req.article.extend(article)
    return req

if __name__ == '__main__':
    logging.basicConfig()
    run()
