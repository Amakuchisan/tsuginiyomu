package manager

import "errors"

// ErrInvalidArgument は引数が不正だったときに返される
var ErrInvalidArgument = errors.New("invalid argument")

// ErrAlreadyRegistered はユーザーが既に登録されているときに返される
var ErrAlreadyRegistered = errors.New("already registered")
