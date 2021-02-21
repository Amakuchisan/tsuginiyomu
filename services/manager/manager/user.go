package manager

import (
	"context"
	"regexp"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
)

// はてなIDは最初の文字をアルファベット、最後の文字をアルファベットまたは数字とし、
// 間に[a-zA-Z0-9_-]を1文字以上30文字以下で成り立つ
var hatenaIDRE = regexp.MustCompile(`^[a-zA-Z][a-zA-Z0-9_-]{1,30}[a-zA-Z0-9]$`)

// GetUser はユーザの取得を行う
func (m *Manager) GetUser(ctx context.Context, hatenaID string) (*domain.User, error) {
	if ok := hatenaIDRE.MatchString(hatenaID); !ok {
		return nil, ErrInvalidArgument
	}
	repo := repository.NewRepository(m.db)
	user, err := domain.GetUser(hatenaID)(ctx, repo)
	if err != nil {
		return nil, err
	}
	return user, nil
}

// CreateUser はユーザの登録を行う
func (m *Manager) CreateUser(ctx context.Context, hatenaID string) (*domain.User, error) {
	if ok := hatenaIDRE.MatchString(hatenaID); !ok {
		return nil, ErrInvalidArgument
	}
	repo := repository.NewRepository(m.db)
	user, err := domain.CreateUser(hatenaID)(ctx, repo)
	if err != nil {
		if err == domain.ErrAlreadyExists {
			return user, ErrAlreadyRegistered
		}
		return nil, err
	}
	return user, nil
}

// UpdateWordcloud はユーザのwordcloudを更新する
func (m *Manager) UpdateWordcloud(ctx context.Context, hatenaID string, wordcloud []byte) (*domain.User, error) {
	if ok := hatenaIDRE.MatchString(hatenaID); !ok {
		return nil, ErrInvalidArgument
	}
	repo := repository.NewRepository(m.db)
	user, err := domain.UpdateWordcloud(hatenaID, wordcloud)(ctx, repo)
	if err != nil {
		return nil, err
	}
	return user, nil
}
