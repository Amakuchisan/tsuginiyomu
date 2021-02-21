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
	newCreatedURL := []string{}
	for _, url := range in.Url {
		article, err := s.manager.CreateArticle(ctx, url)
		if err != nil {
			if err == manager.ErrInvalidArgument {
				return nil, status.Error(codes.InvalidArgument, "invalid argument")
			}
			if err != manager.ErrAlreadyRegistered {
				return nil, err
			}
		} else {
			newCreatedURL = append(newCreatedURL, article.URL)
		}
	}
	return &pb.CreateArticleReply{NewCreatedUrl: newCreatedURL}, nil
}
