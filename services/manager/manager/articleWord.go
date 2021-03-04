package manager

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
)

// CreateArticleWord は記事と単語の関係を登録する
func (m *Manager) CreateArticleWord(ctx context.Context, articleID domain.ArticleID, wordCount map[string]float64) error {
	repo := repository.NewRepository(m.db)
	err := domain.CreateArticleWord(articleID, wordCount)(ctx, repo)
	if err != nil {
		if err == domain.ErrAlreadyExists {
			return ErrAlreadyRegistered
		}
	}
	return err
}
