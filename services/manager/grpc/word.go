package grpc

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// CreateWord は新規単語の登録を行う
func (s *Server) CreateWord(ctx context.Context, in *pb.CreateWordRequest) (*pb.CreateWordReply, error) {
	for _, article := range in.Article {
		art, err := s.manager.GetArticle(ctx, article.Url)
		if err != nil {
			return &pb.CreateWordReply{Created: false}, err
		}
		_, err = s.manager.CreateWord(ctx, article.WordCount)
		if err != nil {
			return &pb.CreateWordReply{Created: false}, err
		}
		err = s.manager.CreateArticleWord(ctx, art.ID, article.WordCount)
		if err != manager.ErrAlreadyRegistered {
			if err != nil {
				return &pb.CreateWordReply{Created: false}, nil
			}
		}
	}

	return &pb.CreateWordReply{Created: true}, nil
}

// GetWord は新規単語の検索を行い, 結果を返す
func (s *Server) GetWord(ctx context.Context, in *pb.GetWordRequest) (*pb.GetWordReply, error) {
	wordCount, err := s.manager.GetWord(ctx, in.HatenaID)
	if err != nil {
		if err == manager.ErrInvalidArgument {
			return nil, status.Error(codes.InvalidArgument, "invalid argument")
		}
		return nil, err
	}
	return &pb.GetWordReply{WordCount: wordCount}, nil
}
