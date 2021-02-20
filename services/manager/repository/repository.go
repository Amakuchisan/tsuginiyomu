package repository

import (
	"github.com/Amakuchisan/tsuginiyomu/services/manager/domain"
	"github.com/jmoiron/sqlx"
)

// DB はデータベースのインターフェース
type DB interface {
	sqlx.Execer
	sqlx.ExecerContext
	sqlx.Queryer
	sqlx.QueryerContext
}

// Repository は domain.Repository に対するデータベースを使った実装
type Repository struct {
	user        *UserRepository
	article     *ArticleRepository
	articleWord *ArticleWordRepository
	word        *WordRepository
}

// NewRepository は Repository を作成する
func NewRepository(db DB) *Repository {
	return &Repository{
		user:        newUserRepository(db),
		article:     newArticleRepository(db),
		articleWord: newArticleWordRepository(db),
		word:        newWordRepository(db),
	}
}

// User はユーザーに対するリポジトリを返す
func (r *Repository) User() domain.UserRepository {
	return r.user
}

// Article は記事に対するリポジトリを返す
func (r *Repository) Article() domain.ArticleRepository {
	return r.article
}

// ArticleWord は記事と単語の関係に対するリポジトリを返す
func (r *Repository) ArticleWord() domain.ArticleWordRepository {
	return r.articleWord
}

// Word は単語に対するリポジトリを返す
func (r *Repository) Word() domain.WordRepository {
	return r.word
}
