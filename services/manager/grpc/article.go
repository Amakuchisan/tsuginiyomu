package grpc

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	set "github.com/deckarep/golang-set"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// CreateArticle は新規記事の登録を行う
func (s *Server) CreateArticle(ctx context.Context, in *pb.CreateArticleRequest) (*pb.CreateArticleReply, error) {
	newCreatedURL := []string{}
	user, err := s.manager.GetUser(ctx, in.HatenaID)
	if err != nil {
		return &pb.CreateArticleReply{NewCreatedUrl: nil}, err
	}
	articleURLNotHaveWord, err := s.manager.GetArticleURLNotHaveWord(ctx)
	if err != nil {
		return &pb.CreateArticleReply{NewCreatedUrl: nil}, err
	}
	URL, URLNotHaveWord := getBothAndDifference(stringsToInterface(in.Url), stringsToInterface(articleURLNotHaveWord))

	for _, url := range URL {
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
		_, err = s.manager.CreateUserArticle(ctx, user.ID, article.URL)
		if err != nil {
			if err != manager.ErrAlreadyRegistered {
				return &pb.CreateArticleReply{NewCreatedUrl: newCreatedURL}, err
			}
		}
	}
	return &pb.CreateArticleReply{NewCreatedUrl: append(newCreatedURL, URLNotHaveWord...)}, nil
}

func stringsToInterface(strings []string) (ret []interface{}) {
	for _, s := range strings {
		ret = append(ret, s)
	}
	return
}

func interfaceToStrings(in []interface{}) (ret []string) {
	for _, r := range in {
		ret = append(ret, r.(string))
	}
	return
}

func getBothAndDifference(left []interface{}, right []interface{}) ([]string, []string) {
	s1 := set.NewSetFromSlice(left)
	s2 := set.NewSetFromSlice(right)
	both := s1.Intersect(s2)
	onlyLeft := s1.Difference(both)
	return interfaceToStrings(onlyLeft.ToSlice()), interfaceToStrings(both.ToSlice())
}
