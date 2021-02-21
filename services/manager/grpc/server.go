package grpc

import (
	"crypto/ecdsa"

	"github.com/Amakuchisan/tsuginiyomu/services/manager/manager"
	pb "github.com/Amakuchisan/tsuginiyomu/services/manager/pb/manager"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
)

// Config はサーバーの設定
type Config struct {
	Manager         *manager.Manager
	ECDSAPrivateKey *ecdsa.PrivateKey
}

// Server は pb.ManagerServer に対する実装
type Server struct {
	pb.UnimplementedManagerServer
	healthpb.UnimplementedHealthServer

	manager         *manager.Manager
	ecdsaPrivateKey *ecdsa.PrivateKey
}

// NewServer は gRPC サーバーを作成する
func NewServer(conf *Config) *Server {
	return &Server{
		manager:         conf.Manager,
		ecdsaPrivateKey: conf.ECDSAPrivateKey,
	}
}
