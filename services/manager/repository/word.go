package repository

import (
	"context"
	"database/sql"
	"fmt"
	"strings"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/jmoiron/sqlx"
)

// WordRepository は domain.WordRepository に対するデータベースを使った実装
type WordRepository struct {
	db DB
}

func newWordRepository(db DB) *WordRepository {
	return &WordRepository{db}
}

// Create は新規単語を作成し, リポジトリに保存する
func (r *WordRepository) Create(ctx context.Context, input *domain.CreateWordInput) ([]string, error) {
	query := fmt.Sprintf("INSERT INTO word(name) VALUES (\"%s\")", strings.Join(input.Name, "\"), (\""))
	_, err := r.db.ExecContext(
		ctx,
		query,
	)
	if err != nil {
		return nil, err
	}
	return input.Name, nil
}

// FindByName はリポジトリから名前で単語を検索する
// BINARYを指定することで、大文字小文字の区別をつける
func (r *WordRepository) FindByName(ctx context.Context, noun string) (*domain.Word, error) {
	var word domain.Word
	err := sqlx.GetContext(
		ctx,
		r.db,
		&word,
		`
			SELECT id FROM word
				WHERE name = BINARY ? LIMIT 1
		`,
		noun,
	)
	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return &word, nil
}

// FindByHatenaID はリポジトリからはてなIDと関連する名詞を検索する
// BINARYを指定することで、大文字小文字の区別をつける
func (r *WordRepository) FindByHatenaID(ctx context.Context, hatenaID string) ([]domain.WordCount, error) {
	wordCount := []domain.WordCount{}
	err := sqlx.SelectContext(
		ctx,
		r.db,
		&wordCount,
		`
		SELECT word.name, SUM(word_count) FROM user
			JOIN user_article ON user.id=user_article.user_id
			JOIN article ON user_article.article_id=article.id
			JOIN article_word ON article.id=article_word.article_id
			JOIN word ON article_word.word_id=word.id
			WHERE hatena_id = BINARY ? GROUP BY word.name
		`,
		hatenaID,
	)

	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return wordCount, nil
}
