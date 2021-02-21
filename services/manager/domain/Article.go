package domain

import (
	"context"
	// "strconv"
)

// ArticleID は記事にユニークに割り当てられる ID
type ArticleID uint64

// Article は記事を表す
type Article struct {
	ID  ArticleID `db:"id"`
	URL string `db:"url"`
}

// CreateArticleInput は記事作成時の入力
type CreateArticleInput struct {
	URL string
}

// ArticleRepository は記事のリポジトリ
type ArticleRepository interface {
	Create(ctx context.Context, input *CreateArticleInput) (*Article, error)
	FindByURL(ctx context.Context, url string) (*Article, error)
}

// CreateArticle は新規記事を作成する
func CreateArticle(url string) func(ctx context.Context, r Repository) (*Article, error) {
	return func(ctx context.Context, r Repository) (*Article, error) {
		article, err := r.Article().FindByURL(ctx, url)
		if err != ErrNotFound {
			if err != nil {
				return nil, err
			}
			// Articleが既に作成されていた場合、見つかったarticleの情報を返却する
			return article, ErrAlreadyExists
		}
		return r.Article().Create(ctx, &CreateArticleInput{
			URL: url,
		})
	}
}
