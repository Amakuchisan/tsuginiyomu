package manager

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
)

// CreateWord は単語の登録を行う
func (m *Manager) CreateWord(ctx context.Context, noun string) (*domain.Word, error) {
	repo := repository.NewRepository(m.db)
	word, err := domain.CreateWord(noun)(ctx, repo)
	if err != nil {
		if err == domain.ErrAlreadyExists {
			return nil, ErrAlreadyRegistered
		}
		return nil, err
	}
	return word, nil
}

// GetWord はDBから単語の取得を行う
func (m *Manager) GetWord(ctx context.Context, hatenaID string) (map[string]uint32, error) {
	repo := repository.NewRepository(m.db)
	wordCount, err := domain.GetWord(hatenaID)(ctx, repo)
	if err != nil {
		return nil, err
	}
	return StructListToMap(wordCount), nil
}

func StructListToMap(data []domain.WordCount) map[string]uint32 {
	m := make(map[string]uint32)
	for _, value := range data {
		m[value.Name] = value.Count
	}
	return m
}
