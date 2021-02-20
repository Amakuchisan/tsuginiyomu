package grpc

import (
	"context"
	"fmt"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	// "github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	// "github.com/lestrrat-go/jwx/jwa"
	// "github.com/lestrrat-go/jwx/jwt"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// GetWord は新規単語の検索を行い, 結果を返す
func (s *Server) GetWord(ctx context.Context, in *pb.GetWordRequest) (*pb.GetWordReply, error) {
	wordCount, err := s.manager.GetWord(ctx, in.HatenaID)
	fmt.Println(wordCount)
	fmt.Printf("%T\n", wordCount)
	// word, err := s.manager.GetWord(ctx, in.HatenaID)
	if err != nil {
		if err == manager.ErrInvalidArgument {
			return nil, status.Error(codes.InvalidArgument, "invalid argument")
		}
		return nil, err
	}
	return &pb.GetWordReply{WordCount: wordCount}, nil
	// return &pb.GetWordReply{WordCount: wordCount}, nil
}
