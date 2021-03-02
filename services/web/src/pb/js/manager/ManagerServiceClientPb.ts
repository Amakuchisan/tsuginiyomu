/**
 * @fileoverview gRPC-Web generated client stub for manager
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck


import * as grpcWeb from 'grpc-web';

import * as manager_pb from './manager_pb';


export class ManagerClient {
  client_: grpcWeb.AbstractClientBase;
  hostname_: string;
  credentials_: null | { [index: string]: string; };
  options_: null | { [index: string]: any; };

  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: any; }) {
    if (!options) options = {};
    if (!credentials) credentials = {};
    options['format'] = 'text';

    this.client_ = new grpcWeb.GrpcWebClientBase(options);
    this.hostname_ = hostname;
    this.credentials_ = credentials;
    this.options_ = options;
  }

  methodInfoCreateUser = new grpcWeb.AbstractClientBase.MethodInfo(
    manager_pb.CreateUserReply,
    (request: manager_pb.CreateUserRequest) => {
      return request.serializeBinary();
    },
    manager_pb.CreateUserReply.deserializeBinary
  );

  createUser(
    request: manager_pb.CreateUserRequest,
    metadata: grpcWeb.Metadata | null): Promise<manager_pb.CreateUserReply>;

  createUser(
    request: manager_pb.CreateUserRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: manager_pb.CreateUserReply) => void): grpcWeb.ClientReadableStream<manager_pb.CreateUserReply>;

  createUser(
    request: manager_pb.CreateUserRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: manager_pb.CreateUserReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/manager.Manager/CreateUser',
        request,
        metadata || {},
        this.methodInfoCreateUser,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/manager.Manager/CreateUser',
    request,
    metadata || {},
    this.methodInfoCreateUser);
  }

  methodInfoCreateArticle = new grpcWeb.AbstractClientBase.MethodInfo(
    manager_pb.CreateArticleReply,
    (request: manager_pb.CreateArticleRequest) => {
      return request.serializeBinary();
    },
    manager_pb.CreateArticleReply.deserializeBinary
  );

  createArticle(
    request: manager_pb.CreateArticleRequest,
    metadata: grpcWeb.Metadata | null): Promise<manager_pb.CreateArticleReply>;

  createArticle(
    request: manager_pb.CreateArticleRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: manager_pb.CreateArticleReply) => void): grpcWeb.ClientReadableStream<manager_pb.CreateArticleReply>;

  createArticle(
    request: manager_pb.CreateArticleRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: manager_pb.CreateArticleReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/manager.Manager/CreateArticle',
        request,
        metadata || {},
        this.methodInfoCreateArticle,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/manager.Manager/CreateArticle',
    request,
    metadata || {},
    this.methodInfoCreateArticle);
  }

  methodInfoCreateWord = new grpcWeb.AbstractClientBase.MethodInfo(
    manager_pb.CreateWordReply,
    (request: manager_pb.CreateWordRequest) => {
      return request.serializeBinary();
    },
    manager_pb.CreateWordReply.deserializeBinary
  );

  createWord(
    request: manager_pb.CreateWordRequest,
    metadata: grpcWeb.Metadata | null): Promise<manager_pb.CreateWordReply>;

  createWord(
    request: manager_pb.CreateWordRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: manager_pb.CreateWordReply) => void): grpcWeb.ClientReadableStream<manager_pb.CreateWordReply>;

  createWord(
    request: manager_pb.CreateWordRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: manager_pb.CreateWordReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/manager.Manager/CreateWord',
        request,
        metadata || {},
        this.methodInfoCreateWord,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/manager.Manager/CreateWord',
    request,
    metadata || {},
    this.methodInfoCreateWord);
  }

  methodInfoUpdateWordcloud = new grpcWeb.AbstractClientBase.MethodInfo(
    manager_pb.UpdateWordcloudReply,
    (request: manager_pb.UpdateWordcloudRequest) => {
      return request.serializeBinary();
    },
    manager_pb.UpdateWordcloudReply.deserializeBinary
  );

  updateWordcloud(
    request: manager_pb.UpdateWordcloudRequest,
    metadata: grpcWeb.Metadata | null): Promise<manager_pb.UpdateWordcloudReply>;

  updateWordcloud(
    request: manager_pb.UpdateWordcloudRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: manager_pb.UpdateWordcloudReply) => void): grpcWeb.ClientReadableStream<manager_pb.UpdateWordcloudReply>;

  updateWordcloud(
    request: manager_pb.UpdateWordcloudRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: manager_pb.UpdateWordcloudReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/manager.Manager/UpdateWordcloud',
        request,
        metadata || {},
        this.methodInfoUpdateWordcloud,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/manager.Manager/UpdateWordcloud',
    request,
    metadata || {},
    this.methodInfoUpdateWordcloud);
  }

  methodInfoGetWord = new grpcWeb.AbstractClientBase.MethodInfo(
    manager_pb.GetWordReply,
    (request: manager_pb.GetWordRequest) => {
      return request.serializeBinary();
    },
    manager_pb.GetWordReply.deserializeBinary
  );

  getWord(
    request: manager_pb.GetWordRequest,
    metadata: grpcWeb.Metadata | null): Promise<manager_pb.GetWordReply>;

  getWord(
    request: manager_pb.GetWordRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: manager_pb.GetWordReply) => void): grpcWeb.ClientReadableStream<manager_pb.GetWordReply>;

  getWord(
    request: manager_pb.GetWordRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: manager_pb.GetWordReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/manager.Manager/GetWord',
        request,
        metadata || {},
        this.methodInfoGetWord,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/manager.Manager/GetWord',
    request,
    metadata || {},
    this.methodInfoGetWord);
  }

}

