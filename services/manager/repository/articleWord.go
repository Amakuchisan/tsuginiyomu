package repository

import (
	"context"
	"database/sql"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/jmoiron/sqlx"
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
			INSERT INTO article_word (article_id, word_id, word_count)
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

// FindByArticleAndWordID は既にArticleIDとWordIDの関係が登録されているか調べる
func (r *ArticleWordRepository) FindByArticleAndWordID(ctx context.Context, articleID domain.ArticleID, wordID domain.WordID) (*domain.ArticleWord, error) {
	var articleWord domain.ArticleWord
	err := sqlx.GetContext(
		ctx,
		r.db,
		&articleWord,
		`
			SELECT id FROM article_word
				WHERE article_id = ? AND word_id = ? LIMIT 1
		`,
		articleID, wordID,
	)
	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return &articleWord, nil
}
