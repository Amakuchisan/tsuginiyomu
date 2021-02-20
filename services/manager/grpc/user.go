package grpc

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// CreateUser は新規ユーザの登録を行う
func (s *Server) CreateUser(ctx context.Context, in *pb.CreateUserRequest) (*pb.CreateUserReply, error) {
	user, err := s.manager.CreateUser(ctx, in.HatenaID)
	if err != nil {
		if err == manager.ErrAlreadyRegistered {
			return &pb.CreateUserReply{HatenaID: user.HatenaID, WordCloud: user.Wordcloud}, nil
		}
		if err == manager.ErrInvalidArgument {
			return nil, status.Error(codes.InvalidArgument, "invalid argument")
		}
		return nil, err
	}
	return &pb.CreateUserReply{HatenaID: user.HatenaID, WordCloud: nil}, nil
}

// UpdateWordcloud はユーザのwordcloudを更新する
func (s *Server) UpdateWordcloud(ctx context.Context, in *pb.UpdateWordcloudRequest) (*pb.UpdateWordcloudReply, error) {
	user, err := s.manager.UpdateWordcloud(ctx, in.HatenaID, in.Wordcloud)
	if err != nil {
		if err == manager.ErrInvalidArgument {
			return nil, status.Error(codes.InvalidArgument, "invalid argument")
		}
		return nil, err
	}
	return &pb.UpdateWordcloudReply{HatenaID: user.HatenaID, Wordcloud: user.Wordcloud}, nil
}
