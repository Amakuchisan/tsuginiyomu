package manager

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
)

// CreateUserArticle はユーザと記事の関係を登録する
func (m *Manager) CreateUserArticle(ctx context.Context, userID domain.UserID, articleURL string) (*domain.UserArticle, error) {
	repo := repository.NewRepository(m.db)
	userArticle, err := domain.CreateUserArticle(userID, articleURL)(ctx, repo)
	if err != nil {
		if err == domain.ErrAlreadyExists {
			return nil, ErrAlreadyRegistered
		}
		return nil, err
	}
	return userArticle, nil
}
