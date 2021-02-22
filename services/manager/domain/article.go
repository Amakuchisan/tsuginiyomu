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
	URL string    `db:"url"`
}

// CreateArticleInput は記事作成時の入力
type CreateArticleInput struct {
	URL string
}

// ArticleRepository は記事のリポジトリ
type ArticleRepository interface {
	Create(ctx context.Context, input *CreateArticleInput) (*Article, error)
	FindByURL(ctx context.Context, url string) (*Article, error)
	FindNotHaveWord(ctx context.Context) ([]Article, error)
}

// GetArticle は記事を取得する
func GetArticle(url string) func(ctx context.Context, r Repository) (*Article, error) {
	return func(ctx context.Context, r Repository) (*Article, error) {
		return r.Article().FindByURL(ctx, url)
	}
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

// GetArticleURLNotHaveWord は単語を持っていない記事を取得する
func GetArticleURLNotHaveWord() func(ctx context.Context, r Repository) ([]string, error) {
	return func(ctx context.Context, r Repository) ([]string, error) {
		articles, err := r.Article().FindNotHaveWord(ctx)
		if err != nil {
			return nil, err
		}
		articleURL := getURLFromStruct(articles)
		return articleURL, err
	}
}

func getURLFromStruct(articles []Article) []string {
	url := []string{}
	for _, article := range articles {
		url = append(url, article.URL)
	}
	return url
}
