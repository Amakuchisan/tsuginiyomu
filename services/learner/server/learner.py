import grpc

from bookmark.bookmark import Bookmark
import pb.learner.learner_pb2 as learner_pb2
import pb.learner.learner_pb2_grpc as learner_pb2_grpc

class Learner(learner_pb2_grpc.LearnerServicer):
    def __init__(self):
        self.bookmark = Bookmark()
    def Learn(self, request, context):
        learned = self.bookmark.learn(request.hatena_id)
        return learner_pb2.LearnReply(learned=learned)

    def GetSuggestion(self, request, context):
        suggestions = self.bookmark.get_suggestions(request.hatena_id, "tag=あとで読む&")
        return learner_pb2.GetSuggestionReply(suggestions=suggestions)

    def GetHotentrySuggestion(self, request, context):
        suggestions = self.bookmark.get_hotentry_suggestions(request.hatena_id, request.category)
        return learner_pb2.GetSuggestionReply(suggestions=suggestions)

    def ExistsHatenaID(self, request, context):
        try:
            self.bookmark.count_bookmark_page(request.hatena_id)
        except Exception as err: 
            return learner_pb2.ExistsHatenaIDReply(existed=False)
        return learner_pb2.ExistsHatenaIDReply(existed=True)
