package domain

import (
	"context"
)

// UserArticleID はユーザと記事の関係にユニークに割り当てられる ID
type UserArticleID uint64

// UserArticle は記事を表す
type UserArticle struct {
	ID        UserArticleID `db:"id"`
	UserID    UserID        `db:"user_id"`
	ArticleID ArticleID     `db:"article_id"`
}

// CreateUserArticleInput はUserArticle作成時の入力
type CreateUserArticleInput struct {
	UserID    UserID
	ArticleID ArticleID
}

// UserArticleRepository はUserArticleのリポジトリ
type UserArticleRepository interface {
	Create(ctx context.Context, input *CreateUserArticleInput) (*UserArticle, error)
	FindByUserAndArticleID(ctx context.Context, userID UserID, articleID ArticleID) (*UserArticle, error)
}

// CreateUserArticle は記事と単語の関係を作成する
func CreateUserArticle(userID UserID, articleURL string) func(ctx context.Context, r Repository) (*UserArticle, error) {
	return func(ctx context.Context, r Repository) (*UserArticle, error) {
		article, err := r.Article().FindByURL(ctx, articleURL)
		if err != nil {
			return nil, err
		}
		_, err = r.UserArticle().FindByUserAndArticleID(ctx, userID, article.ID)
		if err != ErrNotFound {
			if err != nil {
				return nil, err
			}
			return nil, ErrAlreadyExists
		}
		return r.UserArticle().Create(ctx, &CreateUserArticleInput{
			UserID:    userID,
			ArticleID: article.ID,
		})
	}
}
