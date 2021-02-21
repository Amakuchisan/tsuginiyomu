package manager

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
)

// CreateArticle は記事の登録を行う
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

// GetArticleURLNotHaveWord はDBから単語を持っていない記事を取得する
func (m *Manager) GetArticleURLNotHaveWord(ctx context.Context) ([]string, error) {
	repo := repository.NewRepository(m.db)
	articleURL, err := domain.GetArticleURLNotHaveWord()(ctx, repo)
	if err != nil {
		return nil, err
	}
	return articleURL, nil
}
