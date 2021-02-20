package manager

import (
	"github.com/jmoiron/sqlx"
)

// Manager はアプリケーションを表す
type Manager struct {
	db *sqlx.DB
}

// NewManager は Manager を作成する
func NewManager(db *sqlx.DB) *Manager {
	return &Manager{db}
}
