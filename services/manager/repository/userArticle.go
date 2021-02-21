package repository

import (
	"context"
	"database/sql"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/jmoiron/sqlx"
)

// UserArticleRepository は domain.UserArticleRepository に対するデータベースを使った実装
type UserArticleRepository struct {
	db DB
}

func newUserArticleRepository(db DB) *UserArticleRepository {
	return &UserArticleRepository{db}
}

// Create はユーザと記事の関係を作成し, リポジトリに保存する
func (r *UserArticleRepository) Create(ctx context.Context, input *domain.CreateUserArticleInput) (*domain.UserArticle, error) {
	userArticle := &domain.UserArticle{
		UserID:    input.UserID,
		ArticleID: input.ArticleID,
	}
	_, err := r.db.ExecContext(
		ctx,
		`
			INSERT INTO user_article (user_id, article_id)
				VALUES (?, ?)
		`,
		userArticle.UserID,
		userArticle.ArticleID,
	)
	if err != nil {
		return nil, err
	}
	return userArticle, nil
}

// FindByUserAndArticleID は既にUserIDとArticleIDの関係が登録されているか調べる
func (r *UserArticleRepository) FindByUserAndArticleID(ctx context.Context, userID domain.UserID, articleID domain.ArticleID) (*domain.UserArticle, error) {
	var userArticle domain.UserArticle
	err := sqlx.GetContext(
		ctx,
		r.db,
		&userArticle,
		`
			SELECT id FROM user_article
				WHERE user_id = ? AND article_id = ? LIMIT 1
		`,
		userID, articleID,
	)
	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return &userArticle, nil
}
