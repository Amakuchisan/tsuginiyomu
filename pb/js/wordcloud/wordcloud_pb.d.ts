import * as jspb from 'google-protobuf'



export class CreateWordCloudRequest extends jspb.Message {
  getHatenaId(): string;
  setHatenaId(value: string): CreateWordCloudRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateWordCloudRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateWordCloudRequest): CreateWordCloudRequest.AsObject;
  static serializeBinaryToWriter(message: CreateWordCloudRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateWordCloudRequest;
  static deserializeBinaryFromReader(message: CreateWordCloudRequest, reader: jspb.BinaryReader): CreateWordCloudRequest;
}

export namespace CreateWordCloudRequest {
  export type AsObject = {
    hatenaId: string,
  }
}

export class CreateWordCloudReply extends jspb.Message {
  getWordcloud(): Uint8Array | string;
  getWordcloud_asU8(): Uint8Array;
  getWordcloud_asB64(): string;
  setWordcloud(value: Uint8Array | string): CreateWordCloudReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateWordCloudReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateWordCloudReply): CreateWordCloudReply.AsObject;
  static serializeBinaryToWriter(message: CreateWordCloudReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateWordCloudReply;
  static deserializeBinaryFromReader(message: CreateWordCloudReply, reader: jspb.BinaryReader): CreateWordCloudReply;
}

export namespace CreateWordCloudReply {
  export type AsObject = {
    wordcloud: Uint8Array | string,
  }
}

