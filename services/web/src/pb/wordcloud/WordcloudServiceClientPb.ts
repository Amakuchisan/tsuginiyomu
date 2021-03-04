/**
 * @fileoverview gRPC-Web generated client stub for wordcloud
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck


import * as grpcWeb from 'grpc-web';

import * as wordcloud_pb from './wordcloud_pb';


export class WordcloudClient {
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

  methodInfoCreateWordCloud = new grpcWeb.AbstractClientBase.MethodInfo(
    wordcloud_pb.CreateWordCloudReply,
    (request: wordcloud_pb.CreateWordCloudRequest) => {
      return request.serializeBinary();
    },
    wordcloud_pb.CreateWordCloudReply.deserializeBinary
  );

  createWordCloud(
    request: wordcloud_pb.CreateWordCloudRequest,
    metadata: grpcWeb.Metadata | null): Promise<wordcloud_pb.CreateWordCloudReply>;

  createWordCloud(
    request: wordcloud_pb.CreateWordCloudRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: wordcloud_pb.CreateWordCloudReply) => void): grpcWeb.ClientReadableStream<wordcloud_pb.CreateWordCloudReply>;

  createWordCloud(
    request: wordcloud_pb.CreateWordCloudRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: wordcloud_pb.CreateWordCloudReply) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/wordcloud.Wordcloud/CreateWordCloud',
        request,
        metadata || {},
        this.methodInfoCreateWordCloud,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/wordcloud.Wordcloud/CreateWordCloud',
    request,
    metadata || {},
    this.methodInfoCreateWordCloud);
  }

}

