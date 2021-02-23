import grpc

from util.bookmark import Bookmark
import pb.learner.learner_pb2 as learner_pb2
import pb.learner.learner_pb2_grpc as learner_pb2_grpc

class Learner(learner_pb2_grpc.LearnerServicer):
    def Learn(self, request, context):
        bookmark = Bookmark()
        learned = bookmark.learn(request.hatena_id)
        return learner_pb2.LearnReply(learned=learned)

    def CreateWordCloud(self, request, context):
        bookmark = Bookmark()
        wordcloud = bookmark.update_wordcloud(request.hatena_id)
        return learner_pb2.CreateWordCloudReply(wordcloud=wordcloud)
