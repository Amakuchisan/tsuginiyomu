package repository

import (
	"context"
	// "database/sql"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	// "github.com/jmoiron/sqlx"
)

// ArticleWordRepository は domain.ArticleWordRepository に対するデータベースを使った実装
type ArticleWordRepository struct {
	db DB
}

func newArticleWordRepository(db DB) *ArticleWordRepository {
	return &ArticleWordRepository{db}
}

// Create は新規単語を作成し, リポジトリに保存する
func (r *ArticleWordRepository) Create(ctx context.Context, input *domain.CreateArticleWordInput) (*domain.ArticleWord, error) {
	articleWord := &domain.ArticleWord{
		ArticleID: input.ArticleID,
		WordID:    input.WordID,
		Count:     input.Count,
	}
	_, err := r.db.ExecContext(
		ctx,
		`
			INSERT INTO article_word (article_id, word_id, count)
				VALUES (?, ?, ?)
		`,
		articleWord.ArticleID,
		articleWord.WordID,
		articleWord.Count,
	)
	if err != nil {
		return nil, err
	}
	return articleWord, nil
}
