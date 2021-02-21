package manager

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
)

// CreateArticle はユーザの登録を行う
func (m *Manager) CreateArticle(ctx context.Context, url string) (*domain.Article, error) {
	repo := repository.NewRepository(m.db)
	article, err := domain.CreateArticle(url)(ctx, repo)
	if err != nil {
		if err == domain.ErrAlreadyExists {
			return article, ErrAlreadyRegistered
		}
		return nil, err
	}
	return article, nil
}
