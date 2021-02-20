package domain

import (
	"context"
	"strconv"
)

// UserID はユーザーにユニークに割り当てられる ID
type UserID uint64

func (id UserID) String() string {
	return strconv.FormatUint(uint64(id), 10)
}

// User はユーザーを表す
type User struct {
	ID        UserID `db:"id"`
	HatenaID  string `db:"hatena_id"`
	Wordcloud []byte `db:"wordcloud"`
}

// CreateUserInput はユーザー作成時の入力
type CreateUserInput struct {
	HatenaID string
}

// UserRepository はユーザーのリポジトリ
type UserRepository interface {
	Create(ctx context.Context, input *CreateUserInput) (*User, error)
	FindByHatenaID(ctx context.Context, hatenaID string) (*User, error) // WordCloudも
	UpdateWordcloud(ctx context.Context, hatenaID string, wordcloud []byte) (*User, error)
}

// CreateUser は新規ユーザーを作成する
func CreateUser(hatenaID string) func(ctx context.Context, r Repository) (*User, error) {
	return func(ctx context.Context, r Repository) (*User, error) {
		user, err := r.User().FindByHatenaID(ctx, hatenaID)
		if err != ErrNotFound {
			if err != nil {
				return nil, err
			}
			// Userが既に作成されていた場合、見つかったuserの情報を返却する
			return user, ErrAlreadyExists
		}
		return r.User().Create(ctx, &CreateUserInput{
			HatenaID: hatenaID,
		})
	}
}

// UpdateWordcloud はユーザのwordcloudを更新する
func UpdateWordcloud(hatenaID string, wordcloud []byte) func(ctx context.Context, r Repository) (*User, error) {
	return func(ctx context.Context, r Repository) (*User, error) {
		_, err := r.User().FindByHatenaID(ctx, hatenaID)
		if err != nil {
			return nil, err
		}
		return r.User().UpdateWordcloud(ctx, hatenaID, wordcloud)
	}
}
