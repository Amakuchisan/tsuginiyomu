package domain

import (
	"context"
	"strconv"
)

// WordID は単語にユニークに割り当てられる ID
type WordID uint64

func (id WordID) String() string {
	return strconv.FormatUint(uint64(id), 10)
}

// Word は単語を表す
type Word struct {
	ID   WordID `db:"id"`
	Name string `db:"name"`
}

// 単語返却時の形
type WordCount struct {
	Name  string `db:"name"`
	Count uint32 `db:"word_count"`
}

// CreateWordInput は単語作成時の入力
type CreateWordInput struct {
	Name string
}

// WordRepository はユーザーのリポジトリ
type WordRepository interface {
	Create(ctx context.Context, input *CreateWordInput) (*Word, error)
	FindByName(ctx context.Context, word string) (*Word, error)
	FindByHatenaID(ctx context.Context, hatenaID string) ([]WordCount, error)
}

// CreateWord は新規単語を作成する
func CreateWord(noun string) func(ctx context.Context, r Repository) (*Word, error) {
	return func(ctx context.Context, r Repository) (*Word, error) {
		_, err := r.Word().FindByName(ctx, noun)
		if err != ErrNotFound {
			if err != nil {
				return nil, err
			}
			return nil, ErrAlreadyExists
		}
		if err != nil {
			return nil, err
		}
		return r.Word().Create(ctx, &CreateWordInput{
			Name: noun,
		})
	}
}

// GetWord ははてなIDと関連する単語を取得する
func GetWord(hatenaID string) func(ctx context.Context, r Repository) ([]WordCount, error) {
	return func(ctx context.Context, r Repository) ([]WordCount, error) {
		wordCount, err := r.Word().FindByHatenaID(ctx, hatenaID)
		return wordCount, err
	}
}
