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
	Count     float64    `db:"word_count"`
}

// CreateArticleWordInput はArticleWord作成時の入力
type CreateArticleWordInput struct {
	ArticleID ArticleID
	WordID    WordID
	Count     float64
}

// ArticleWordRepository はArticleWordのリポジトリ
type ArticleWordRepository interface {
	Create(ctx context.Context, input *CreateArticleWordInput) (*ArticleWord, error)
	FindByArticleAndWordID(ctx context.Context, articleID ArticleID, wordID WordID) (*ArticleWord, error)
}

// CreateArticleWord は記事と単語の関係を作成する
func CreateArticleWord(articleID ArticleID, wordCount map[string]float64) func(ctx context.Context, r Repository) error {
	return func(ctx context.Context, r Repository) error {
		for noun, count := range wordCount {
			word, err := r.Word().FindByName(ctx, noun)
			if err != nil {
				return err
			}
			_, err = r.ArticleWord().FindByArticleAndWordID(ctx, articleID, word.ID)
			if err != ErrNotFound {
				if err != nil {
					return err
				}
			} else {
				_, err := r.ArticleWord().Create(ctx, &CreateArticleWordInput{
					ArticleID: articleID,
					WordID:    word.ID,
					Count:     count,
				})
				if err != nil {
					return err
				}
			}
		}
		return nil
	}
}
