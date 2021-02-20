// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.13.0
// source: evaluator.proto

package evaluator

import (
	context "context"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type GetWordRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	HatenaId string `protobuf:"bytes,1,opt,name=hatena_id,json=hatenaId,proto3" json:"hatena_id,omitempty"`
}

func (x *GetWordRequest) Reset() {
	*x = GetWordRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_evaluator_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetWordRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetWordRequest) ProtoMessage() {}

func (x *GetWordRequest) ProtoReflect() protoreflect.Message {
	mi := &file_evaluator_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetWordRequest.ProtoReflect.Descriptor instead.
func (*GetWordRequest) Descriptor() ([]byte, []int) {
	return file_evaluator_proto_rawDescGZIP(), []int{0}
}

func (x *GetWordRequest) GetHatenaId() string {
	if x != nil {
		return x.HatenaId
	}
	return ""
}

type GetWordReply struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Message map[string]uint32 `protobuf:"bytes,1,rep,name=message,proto3" json:"message,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"varint,2,opt,name=value,proto3"`
}

func (x *GetWordReply) Reset() {
	*x = GetWordReply{}
	if protoimpl.UnsafeEnabled {
		mi := &file_evaluator_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetWordReply) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetWordReply) ProtoMessage() {}

func (x *GetWordReply) ProtoReflect() protoreflect.Message {
	mi := &file_evaluator_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetWordReply.ProtoReflect.Descriptor instead.
func (*GetWordReply) Descriptor() ([]byte, []int) {
	return file_evaluator_proto_rawDescGZIP(), []int{1}
}

func (x *GetWordReply) GetMessage() map[string]uint32 {
	if x != nil {
		return x.Message
	}
	return nil
}

var File_evaluator_proto protoreflect.FileDescriptor

var file_evaluator_proto_rawDesc = []byte{
	0x0a, 0x0f, 0x65, 0x76, 0x61, 0x6c, 0x75, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x09, 0x65, 0x76, 0x61, 0x6c, 0x75, 0x61, 0x74, 0x6f, 0x72, 0x22, 0x2d, 0x0a, 0x0e,
	0x47, 0x65, 0x74, 0x57, 0x6f, 0x72, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1b,
	0x0a, 0x09, 0x68, 0x61, 0x74, 0x65, 0x6e, 0x61, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x08, 0x68, 0x61, 0x74, 0x65, 0x6e, 0x61, 0x49, 0x64, 0x22, 0x8a, 0x01, 0x0a, 0x0c,
	0x47, 0x65, 0x74, 0x57, 0x6f, 0x72, 0x64, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x12, 0x3e, 0x0a, 0x07,
	0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x24, 0x2e,
	0x65, 0x76, 0x61, 0x6c, 0x75, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x47, 0x65, 0x74, 0x57, 0x6f, 0x72,
	0x64, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x2e, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x45, 0x6e,
	0x74, 0x72, 0x79, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x1a, 0x3a, 0x0a, 0x0c,
	0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03,
	0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14,
	0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0d, 0x52, 0x05, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x32, 0x4c, 0x0a, 0x09, 0x45, 0x76, 0x61, 0x6c,
	0x75, 0x61, 0x74, 0x6f, 0x72, 0x12, 0x3f, 0x0a, 0x07, 0x67, 0x65, 0x74, 0x57, 0x6f, 0x72, 0x64,
	0x12, 0x19, 0x2e, 0x65, 0x76, 0x61, 0x6c, 0x75, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x47, 0x65, 0x74,
	0x57, 0x6f, 0x72, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x17, 0x2e, 0x65, 0x76,
	0x61, 0x6c, 0x75, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x47, 0x65, 0x74, 0x57, 0x6f, 0x72, 0x64, 0x52,
	0x65, 0x70, 0x6c, 0x79, 0x22, 0x00, 0x42, 0x34, 0x5a, 0x32, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x41, 0x6d, 0x61, 0x6b, 0x75, 0x63, 0x68, 0x69, 0x73, 0x61, 0x6e,
	0x2f, 0x74, 0x73, 0x75, 0x67, 0x69, 0x6e, 0x69, 0x79, 0x6f, 0x6d, 0x75, 0x2f, 0x70, 0x62, 0x2f,
	0x67, 0x6f, 0x2f, 0x65, 0x76, 0x61, 0x6c, 0x75, 0x61, 0x74, 0x6f, 0x72, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_evaluator_proto_rawDescOnce sync.Once
	file_evaluator_proto_rawDescData = file_evaluator_proto_rawDesc
)

func file_evaluator_proto_rawDescGZIP() []byte {
	file_evaluator_proto_rawDescOnce.Do(func() {
		file_evaluator_proto_rawDescData = protoimpl.X.CompressGZIP(file_evaluator_proto_rawDescData)
	})
	return file_evaluator_proto_rawDescData
}

var file_evaluator_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_evaluator_proto_goTypes = []interface{}{
	(*GetWordRequest)(nil), // 0: evaluator.GetWordRequest
	(*GetWordReply)(nil),   // 1: evaluator.GetWordReply
	nil,                    // 2: evaluator.GetWordReply.MessageEntry
}
var file_evaluator_proto_depIdxs = []int32{
	2, // 0: evaluator.GetWordReply.message:type_name -> evaluator.GetWordReply.MessageEntry
	0, // 1: evaluator.Evaluator.getWord:input_type -> evaluator.GetWordRequest
	1, // 2: evaluator.Evaluator.getWord:output_type -> evaluator.GetWordReply
	2, // [2:3] is the sub-list for method output_type
	1, // [1:2] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_evaluator_proto_init() }
func file_evaluator_proto_init() {
	if File_evaluator_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_evaluator_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetWordRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_evaluator_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetWordReply); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_evaluator_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_evaluator_proto_goTypes,
		DependencyIndexes: file_evaluator_proto_depIdxs,
		MessageInfos:      file_evaluator_proto_msgTypes,
	}.Build()
	File_evaluator_proto = out.File
	file_evaluator_proto_rawDesc = nil
	file_evaluator_proto_goTypes = nil
	file_evaluator_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// EvaluatorClient is the client API for Evaluator service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type EvaluatorClient interface {
	GetWord(ctx context.Context, in *GetWordRequest, opts ...grpc.CallOption) (*GetWordReply, error)
}

type evaluatorClient struct {
	cc grpc.ClientConnInterface
}

func NewEvaluatorClient(cc grpc.ClientConnInterface) EvaluatorClient {
	return &evaluatorClient{cc}
}

func (c *evaluatorClient) GetWord(ctx context.Context, in *GetWordRequest, opts ...grpc.CallOption) (*GetWordReply, error) {
	out := new(GetWordReply)
	err := c.cc.Invoke(ctx, "/evaluator.Evaluator/getWord", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EvaluatorServer is the server API for Evaluator service.
type EvaluatorServer interface {
	GetWord(context.Context, *GetWordRequest) (*GetWordReply, error)
}

// UnimplementedEvaluatorServer can be embedded to have forward compatible implementations.
type UnimplementedEvaluatorServer struct {
}

func (*UnimplementedEvaluatorServer) GetWord(context.Context, *GetWordRequest) (*GetWordReply, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetWord not implemented")
}

func RegisterEvaluatorServer(s *grpc.Server, srv EvaluatorServer) {
	s.RegisterService(&_Evaluator_serviceDesc, srv)
}

func _Evaluator_GetWord_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetWordRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EvaluatorServer).GetWord(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/evaluator.Evaluator/GetWord",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EvaluatorServer).GetWord(ctx, req.(*GetWordRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Evaluator_serviceDesc = grpc.ServiceDesc{
	ServiceName: "evaluator.Evaluator",
	HandlerType: (*EvaluatorServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "getWord",
			Handler:    _Evaluator_GetWord_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "evaluator.proto",
}
