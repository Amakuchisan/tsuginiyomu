import grpc

from generator import wordcloud
import pb.wordcloud.wordcloud_pb2 as wordcloud_pb2
import pb.wordcloud.wordcloud_pb2_grpc as wordcloud_pb2_grpc

class Wordcloud(wordcloud_pb2_grpc.WordcloudServicer):
    def CreateWordCloud(self, request, context):
        wordcloud_image = wordcloud.update_wordcloud(request.hatena_id)
        return wordcloud_pb2.CreateWordCloudReply(wordcloud=wordcloud_image)
