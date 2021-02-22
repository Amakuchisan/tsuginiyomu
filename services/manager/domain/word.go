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

// WordCount 単語返却時の形
type WordCount struct {
	Name  string `db:"name"`
	Count uint32 `db:"SUM(word_count)"`
}

// CreateWordInput は単語作成時の入力
type CreateWordInput struct {
	Name []string
}

// WordRepository はユーザーのリポジトリ
type WordRepository interface {
	Create(ctx context.Context, input *CreateWordInput) ([]string, error)
	FindByName(ctx context.Context, word string) (*Word, error)
	FindByHatenaID(ctx context.Context, hatenaID string) ([]WordCount, error)
}

// CreateWord は新規単語を作成する
func CreateWord(wordCount map[string]uint32) func(ctx context.Context, r Repository) ([]string, error) {
	return func(ctx context.Context, r Repository) ([]string, error) {
		nouns := []string{}
		for noun := range wordCount {
			_, err := r.Word().FindByName(ctx, noun)
			if err != ErrNotFound {
				if err != nil {
					return nil, err
				}
			} else {
				nouns = append(nouns, noun)
			}
		}
		if len(nouns) > 0 {
			_, err := r.Word().Create(ctx, &CreateWordInput{
				Name: nouns,
			})
			if err != nil {
				return nil, err
			}
		}
		return nouns, nil
	}
}

// GetWord ははてなIDと関連する単語を取得する
func GetWord(hatenaID string) func(ctx context.Context, r Repository) ([]WordCount, error) {
	return func(ctx context.Context, r Repository) ([]WordCount, error) {
		wordCount, err := r.Word().FindByHatenaID(ctx, hatenaID)
		return wordCount, err
	}
}

// StructListToMap はWordCountの構造体をMapに変換する
func StructListToMap(data []WordCount) map[string]uint32 {
	m := make(map[string]uint32)
	for _, value := range data {
		m[value.Name] = value.Count
	}
	return m
}
