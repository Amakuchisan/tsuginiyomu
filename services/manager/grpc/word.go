package grpc

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// GetWord は新規単語の検索を行い, 結果を返す
func (s *Server) GetWord(ctx context.Context, in *pb.GetWordRequest) (*pb.GetWordReply, error) {
	wordCount, err := s.manager.GetWord(ctx, in.HatenaID)
	// word, err := s.manager.GetWord(ctx, in.HatenaID)
	if err != nil {
		if err == manager.ErrInvalidArgument {
			return nil, status.Error(codes.InvalidArgument, "invalid argument")
		}
		return nil, err
	}
	return &pb.GetWordReply{WordCount: wordCount}, nil
}
