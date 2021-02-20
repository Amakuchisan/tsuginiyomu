package repository

import (
	"context"
	"database/sql"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/jmoiron/sqlx"
)

// UserRepository は domain.UserRepository に対するデータベースを使った実装
type UserRepository struct {
	db DB
}

func newUserRepository(db DB) *UserRepository {
	return &UserRepository{db}
}

// Create は新規ユーザーを作成し, リポジトリに保存する
func (r *UserRepository) Create(ctx context.Context, input *domain.CreateUserInput) (*domain.User, error) {
	user := &domain.User{
		HatenaID: input.HatenaID,
	}
	_, err := r.db.ExecContext(
		ctx,
		`
			INSERT INTO user (hatena_id)
				VALUES (?)
		`,
		user.HatenaID,
	)
	if err != nil {
		return nil, err
	}
	return user, nil
}

// FindByHatenaID はリポジトリから名前でユーザーを検索する
// BINARYを指定することで、大文字小文字の区別をつける
func (r *UserRepository) FindByHatenaID(ctx context.Context, hatenaID string) (*domain.User, error) {
	var user domain.User
	err := sqlx.GetContext(
		ctx,
		r.db,
		&user,
		`
			SELECT id, hatena_id, wordcloud FROM user
				WHERE hatena_id = BINARY ? LIMIT 1
		`,
		hatenaID,
	)
	if err != nil {
		if err == sql.ErrNoRows {
			return nil, domain.ErrNotFound
		}
		return nil, err
	}
	return &user, nil
}

// UpdateWordcloud はWordcloudを作成し、ユーザの辞書に登録する
func (r *UserRepository) UpdateWordcloud(ctx context.Context, hatenaID string, wordcloud []byte) (*domain.User, error) {
	user := &domain.User{
		HatenaID:  hatenaID,
		Wordcloud: wordcloud,
	}
	_, err := r.db.ExecContext(
		ctx,
		`
			UPDATE user SET wordcloud = ?
			WHERE hatena_id = ?
		`,
		user.Wordcloud,
		user.HatenaID,
	)
	if err != nil {
		return nil, err
	}
	return user, nil
}
