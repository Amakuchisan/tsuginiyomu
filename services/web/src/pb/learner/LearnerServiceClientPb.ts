/**
 * @fileoverview gRPC-Web generated client stub for learner
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck


import * as grpcWeb from 'grpc-web';

import * as learner_pb from './learner_pb';


export class LearnerClient {
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

  methodInfoLearn = new grpcWeb.AbstractClientBase.MethodInfo(
    learner_pb.LearnReply,
    (request: learner_pb.LearnRequest) => {
      return request.serializeBinary();
    },
    learner_pb.LearnReply.deserializeBinary
  );

  learn(
    request: learner_pb.LearnRequest,
    metadata: grpcWeb.Metadata | null): Promise<learner_pb.LearnReply>;

  learn(
    request: learner_pb.LearnRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: learner_pb.LearnReply) => void): grpcWeb.ClientReadableStream<learner_pb.LearnReply>;

  learn(
    request: learner_pb.LearnRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: learner_pb.LearnReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/learner.Learner/Learn',
        request,
        metadata || {},
        this.methodInfoLearn,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/learner.Learner/Learn',
    request,
    metadata || {},
    this.methodInfoLearn);
  }

  methodInfoGetSuggestion = new grpcWeb.AbstractClientBase.MethodInfo(
    learner_pb.GetSuggestionReply,
    (request: learner_pb.GetSuggestionRequest) => {
      return request.serializeBinary();
    },
    learner_pb.GetSuggestionReply.deserializeBinary
  );

  getSuggestion(
    request: learner_pb.GetSuggestionRequest,
    metadata: grpcWeb.Metadata | null): Promise<learner_pb.GetSuggestionReply>;

  getSuggestion(
    request: learner_pb.GetSuggestionRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: learner_pb.GetSuggestionReply) => void): grpcWeb.ClientReadableStream<learner_pb.GetSuggestionReply>;

  getSuggestion(
    request: learner_pb.GetSuggestionRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: learner_pb.GetSuggestionReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/learner.Learner/GetSuggestion',
        request,
        metadata || {},
        this.methodInfoGetSuggestion,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/learner.Learner/GetSuggestion',
    request,
    metadata || {},
    this.methodInfoGetSuggestion);
  }

  methodInfoExistsHatenaID = new grpcWeb.AbstractClientBase.MethodInfo(
    learner_pb.ExistsHatenaIDReply,
    (request: learner_pb.ExistsHatenaIDRequest) => {
      return request.serializeBinary();
    },
    learner_pb.ExistsHatenaIDReply.deserializeBinary
  );

  existsHatenaID(
    request: learner_pb.ExistsHatenaIDRequest,
    metadata: grpcWeb.Metadata | null): Promise<learner_pb.ExistsHatenaIDReply>;

  existsHatenaID(
    request: learner_pb.ExistsHatenaIDRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: learner_pb.ExistsHatenaIDReply) => void): grpcWeb.ClientReadableStream<learner_pb.ExistsHatenaIDReply>;

  existsHatenaID(
    request: learner_pb.ExistsHatenaIDRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: learner_pb.ExistsHatenaIDReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/learner.Learner/ExistsHatenaID',
        request,
        metadata || {},
        this.methodInfoExistsHatenaID,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/learner.Learner/ExistsHatenaID',
    request,
    metadata || {},
    this.methodInfoExistsHatenaID);
  }

}

