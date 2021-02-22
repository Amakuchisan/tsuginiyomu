package manager

import (
	"context"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/Amakuchisan/tsuginiyomu/services/manager/repository"
	// pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
)

// CreateWord は単語の登録を行う
func (m *Manager) CreateWord(ctx context.Context, wordCount map[string]uint32) ([]string, error) {
	repo := repository.NewRepository(m.db)
	word, err := domain.CreateWord(wordCount)(ctx, repo)
	if err != nil {
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
	return domain.StructListToMap(wordCount), nil
}
