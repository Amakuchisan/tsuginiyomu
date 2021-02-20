package domain

import (
	"context"
)

// ID は ArticleWord にユニークに割り当てられる ID
type ID uint64

// ArticleWord は記事を表す
type ArticleWord struct {
	ID        ID        `db:"id"`
	ArticleID ArticleID `db:"article_id"`
	WordID    WordID    `db:"word_id"`
	Count     uint32    `db:"word_count"`
}

// CreateArticleWordInput はArticleWord作成時の入力
type CreateArticleWordInput struct {
	ArticleID ArticleID
	WordID    WordID
	Count     uint32
}

// ArticleWordRepository はArticleWordのリポジトリ
type ArticleWordRepository interface {
	Create(ctx context.Context, input *CreateArticleWordInput) (*ArticleWord, error)
}

// CreateArticleWord は記事と単語の関係を作成する
func CreateArticleWord(articleID ArticleID, wordID WordID, count uint32) func(ctx context.Context, r Repository) (*ArticleWord, error) {
	return func(ctx context.Context, r Repository) (*ArticleWord, error) {
		return r.ArticleWord().Create(ctx, &CreateArticleWordInput{
			ArticleID: articleID,
			WordID:    wordID,
			Count:     count,
		})
	}
}
