package repository

import (
	"context"
	"database/sql"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/jmoiron/sqlx"
)

// ArticleRepository は domain.ArticleRepository に対するデータベースを使った実装
type ArticleRepository struct {
	db DB
}

func newArticleRepository(db DB) *ArticleRepository {
	return &ArticleRepository{db}
}

// Create は新規単語を作成し, リポジトリに保存する
func (r *ArticleRepository) Create(ctx context.Context, input *domain.CreateArticleInput) (*domain.Article, error) {
	article := &domain.Article{
		URL: input.URL,
	}
	_, err := r.db.ExecContext(
		ctx,
		`
			INSERT INTO article (url)
				VALUES (?)
		`,
		article.URL,
	)
	if err != nil {
		return nil, err
	}
	return article, nil
}

// FindByURL はリポジトリからURLで記事を検索する
// BINARYを指定することで、大文字小文字の区別をつける
func (r *ArticleRepository) FindByURL(ctx context.Context, url string) (*domain.Article, error) {
	var article domain.Article
	err := sqlx.GetContext(
		ctx,
		r.db,
		&article,
		`
			SELECT id, url FROM article
				WHERE url = BINARY ? LIMIT 1
		`,
		url,
	)
	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return &article, nil
}

// FindNotHaveWord はリポジトリから単語と関連付けられていない記事を検索する
func (r *ArticleRepository) FindNotHaveWord(ctx context.Context) ([]domain.Article, error) {
	article := []domain.Article{}
	err := sqlx.SelectContext(
		ctx,
		r.db,
		&article,
		`
		SELECT article.id, url from article LEFT OUTER
			JOIN article_word ON article.id=article_word.article_id
			WHERE article_word.id IS NULL;
		`,
	)

	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return article, nil
}
