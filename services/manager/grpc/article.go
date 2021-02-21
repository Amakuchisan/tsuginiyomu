package grpc

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// CreateArticle は新規ユーザの登録を行う
func (s *Server) CreateArticle(ctx context.Context, in *pb.CreateArticleRequest) (*pb.CreateArticleReply, error) {
	article, err := s.manager.CreateArticle(ctx, in.Url)
	if err != nil {
		if err == manager.ErrAlreadyRegistered {
			return &pb.CreateArticleReply{Url: article.URL}, nil
		}
		if err == manager.ErrInvalidArgument {
			return nil, status.Error(codes.InvalidArgument, "invalid argument")
		}
		return nil, err
	}
	return &pb.CreateArticleReply{Url: article.URL}, nil
}
