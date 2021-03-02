import * as jspb from 'google-protobuf'



export class CreateUserRequest extends jspb.Message {
  getHatenaid(): string;
  setHatenaid(value: string): CreateUserRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateUserRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateUserRequest): CreateUserRequest.AsObject;
  static serializeBinaryToWriter(message: CreateUserRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateUserRequest;
  static deserializeBinaryFromReader(message: CreateUserRequest, reader: jspb.BinaryReader): CreateUserRequest;
}

export namespace CreateUserRequest {
  export type AsObject = {
    hatenaid: string,
  }
}

export class CreateUserReply extends jspb.Message {
  getHatenaid(): string;
  setHatenaid(value: string): CreateUserReply;

  getWordcloud(): Uint8Array | string;
  getWordcloud_asU8(): Uint8Array;
  getWordcloud_asB64(): string;
  setWordcloud(value: Uint8Array | string): CreateUserReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateUserReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateUserReply): CreateUserReply.AsObject;
  static serializeBinaryToWriter(message: CreateUserReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateUserReply;
  static deserializeBinaryFromReader(message: CreateUserReply, reader: jspb.BinaryReader): CreateUserReply;
}

export namespace CreateUserReply {
  export type AsObject = {
    hatenaid: string,
    wordcloud: Uint8Array | string,
  }
}

export class CreateArticleRequest extends jspb.Message {
  getHatenaid(): string;
  setHatenaid(value: string): CreateArticleRequest;

  getUrlList(): Array<string>;
  setUrlList(value: Array<string>): CreateArticleRequest;
  clearUrlList(): CreateArticleRequest;
  addUrl(value: string, index?: number): CreateArticleRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateArticleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateArticleRequest): CreateArticleRequest.AsObject;
  static serializeBinaryToWriter(message: CreateArticleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateArticleRequest;
  static deserializeBinaryFromReader(message: CreateArticleRequest, reader: jspb.BinaryReader): CreateArticleRequest;
}

export namespace CreateArticleRequest {
  export type AsObject = {
    hatenaid: string,
    urlList: Array<string>,
  }
}

export class CreateArticleReply extends jspb.Message {
  getNewCreatedUrlList(): Array<string>;
  setNewCreatedUrlList(value: Array<string>): CreateArticleReply;
  clearNewCreatedUrlList(): CreateArticleReply;
  addNewCreatedUrl(value: string, index?: number): CreateArticleReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateArticleReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateArticleReply): CreateArticleReply.AsObject;
  static serializeBinaryToWriter(message: CreateArticleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateArticleReply;
  static deserializeBinaryFromReader(message: CreateArticleReply, reader: jspb.BinaryReader): CreateArticleReply;
}

export namespace CreateArticleReply {
  export type AsObject = {
    newCreatedUrlList: Array<string>,
  }
}

export class Article extends jspb.Message {
  getUrl(): string;
  setUrl(value: string): Article;

  getWordCountMap(): jspb.Map<string, number>;
  clearWordCountMap(): Article;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Article.AsObject;
  static toObject(includeInstance: boolean, msg: Article): Article.AsObject;
  static serializeBinaryToWriter(message: Article, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Article;
  static deserializeBinaryFromReader(message: Article, reader: jspb.BinaryReader): Article;
}

export namespace Article {
  export type AsObject = {
    url: string,
    wordCountMap: Array<[string, number]>,
  }
}

export class CreateWordRequest extends jspb.Message {
  getArticleList(): Array<Article>;
  setArticleList(value: Array<Article>): CreateWordRequest;
  clearArticleList(): CreateWordRequest;
  addArticle(value?: Article, index?: number): Article;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateWordRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateWordRequest): CreateWordRequest.AsObject;
  static serializeBinaryToWriter(message: CreateWordRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateWordRequest;
  static deserializeBinaryFromReader(message: CreateWordRequest, reader: jspb.BinaryReader): CreateWordRequest;
}

export namespace CreateWordRequest {
  export type AsObject = {
    articleList: Array<Article.AsObject>,
  }
}

export class CreateWordReply extends jspb.Message {
  getCreated(): boolean;
  setCreated(value: boolean): CreateWordReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateWordReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateWordReply): CreateWordReply.AsObject;
  static serializeBinaryToWriter(message: CreateWordReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateWordReply;
  static deserializeBinaryFromReader(message: CreateWordReply, reader: jspb.BinaryReader): CreateWordReply;
}

export namespace CreateWordReply {
  export type AsObject = {
    created: boolean,
  }
}

export class UpdateWordcloudRequest extends jspb.Message {
  getHatenaid(): string;
  setHatenaid(value: string): UpdateWordcloudRequest;

  getWordcloud(): Uint8Array | string;
  getWordcloud_asU8(): Uint8Array;
  getWordcloud_asB64(): string;
  setWordcloud(value: Uint8Array | string): UpdateWordcloudRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateWordcloudRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateWordcloudRequest): UpdateWordcloudRequest.AsObject;
  static serializeBinaryToWriter(message: UpdateWordcloudRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateWordcloudRequest;
  static deserializeBinaryFromReader(message: UpdateWordcloudRequest, reader: jspb.BinaryReader): UpdateWordcloudRequest;
}

export namespace UpdateWordcloudRequest {
  export type AsObject = {
    hatenaid: string,
    wordcloud: Uint8Array | string,
  }
}

export class UpdateWordcloudReply extends jspb.Message {
  getHatenaid(): string;
  setHatenaid(value: string): UpdateWordcloudReply;

  getWordcloud(): Uint8Array | string;
  getWordcloud_asU8(): Uint8Array;
  getWordcloud_asB64(): string;
  setWordcloud(value: Uint8Array | string): UpdateWordcloudReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateWordcloudReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateWordcloudReply): UpdateWordcloudReply.AsObject;
  static serializeBinaryToWriter(message: UpdateWordcloudReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateWordcloudReply;
  static deserializeBinaryFromReader(message: UpdateWordcloudReply, reader: jspb.BinaryReader): UpdateWordcloudReply;
}

export namespace UpdateWordcloudReply {
  export type AsObject = {
    hatenaid: string,
    wordcloud: Uint8Array | string,
  }
}

export class GetWordRequest extends jspb.Message {
  getHatenaid(): string;
  setHatenaid(value: string): GetWordRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetWordRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetWordRequest): GetWordRequest.AsObject;
  static serializeBinaryToWriter(message: GetWordRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetWordRequest;
  static deserializeBinaryFromReader(message: GetWordRequest, reader: jspb.BinaryReader): GetWordRequest;
}

export namespace GetWordRequest {
  export type AsObject = {
    hatenaid: string,
  }
}

export class GetWordReply extends jspb.Message {
  getWordcountMap(): jspb.Map<string, number>;
  clearWordcountMap(): GetWordReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetWordReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetWordReply): GetWordReply.AsObject;
  static serializeBinaryToWriter(message: GetWordReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetWordReply;
  static deserializeBinaryFromReader(message: GetWordReply, reader: jspb.BinaryReader): GetWordReply;
}

export namespace GetWordReply {
  export type AsObject = {
    wordcountMap: Array<[string, number]>,
  }
}

