import * as jspb from 'google-protobuf'



export class LearnRequest extends jspb.Message {
  getHatenaId(): string;
  setHatenaId(value: string): LearnRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LearnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: LearnRequest): LearnRequest.AsObject;
  static serializeBinaryToWriter(message: LearnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LearnRequest;
  static deserializeBinaryFromReader(message: LearnRequest, reader: jspb.BinaryReader): LearnRequest;
}

export namespace LearnRequest {
  export type AsObject = {
    hatenaId: string,
  }
}

export class LearnReply extends jspb.Message {
  getLearned(): boolean;
  setLearned(value: boolean): LearnReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LearnReply.AsObject;
  static toObject(includeInstance: boolean, msg: LearnReply): LearnReply.AsObject;
  static serializeBinaryToWriter(message: LearnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LearnReply;
  static deserializeBinaryFromReader(message: LearnReply, reader: jspb.BinaryReader): LearnReply;
}

export namespace LearnReply {
  export type AsObject = {
    learned: boolean,
  }
}

export class GetSuggestionRequest extends jspb.Message {
  getHatenaId(): string;
  setHatenaId(value: string): GetSuggestionRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSuggestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSuggestionRequest): GetSuggestionRequest.AsObject;
  static serializeBinaryToWriter(message: GetSuggestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSuggestionRequest;
  static deserializeBinaryFromReader(message: GetSuggestionRequest, reader: jspb.BinaryReader): GetSuggestionRequest;
}

export namespace GetSuggestionRequest {
  export type AsObject = {
    hatenaId: string,
  }
}

export class GetHotentrySuggestionRequest extends jspb.Message {
  getHatenaId(): string;
  setHatenaId(value: string): GetHotentrySuggestionRequest;

  getCategory(): string;
  setCategory(value: string): GetHotentrySuggestionRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHotentrySuggestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHotentrySuggestionRequest): GetHotentrySuggestionRequest.AsObject;
  static serializeBinaryToWriter(message: GetHotentrySuggestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHotentrySuggestionRequest;
  static deserializeBinaryFromReader(message: GetHotentrySuggestionRequest, reader: jspb.BinaryReader): GetHotentrySuggestionRequest;
}

export namespace GetHotentrySuggestionRequest {
  export type AsObject = {
    hatenaId: string,
    category: string,
  }
}

export class Suggestion extends jspb.Message {
  getLink(): string;
  setLink(value: string): Suggestion;

  getTitle(): string;
  setTitle(value: string): Suggestion;

  getScore(): number;
  setScore(value: number): Suggestion;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Suggestion.AsObject;
  static toObject(includeInstance: boolean, msg: Suggestion): Suggestion.AsObject;
  static serializeBinaryToWriter(message: Suggestion, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Suggestion;
  static deserializeBinaryFromReader(message: Suggestion, reader: jspb.BinaryReader): Suggestion;
}

export namespace Suggestion {
  export type AsObject = {
    link: string,
    title: string,
    score: number,
  }
}

export class GetSuggestionReply extends jspb.Message {
  getSuggestionsList(): Array<Suggestion>;
  setSuggestionsList(value: Array<Suggestion>): GetSuggestionReply;
  clearSuggestionsList(): GetSuggestionReply;
  addSuggestions(value?: Suggestion, index?: number): Suggestion;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSuggestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetSuggestionReply): GetSuggestionReply.AsObject;
  static serializeBinaryToWriter(message: GetSuggestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSuggestionReply;
  static deserializeBinaryFromReader(message: GetSuggestionReply, reader: jspb.BinaryReader): GetSuggestionReply;
}

export namespace GetSuggestionReply {
  export type AsObject = {
    suggestionsList: Array<Suggestion.AsObject>,
  }
}

export class ExistsHatenaIDRequest extends jspb.Message {
  getHatenaId(): string;
  setHatenaId(value: string): ExistsHatenaIDRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ExistsHatenaIDRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ExistsHatenaIDRequest): ExistsHatenaIDRequest.AsObject;
  static serializeBinaryToWriter(message: ExistsHatenaIDRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ExistsHatenaIDRequest;
  static deserializeBinaryFromReader(message: ExistsHatenaIDRequest, reader: jspb.BinaryReader): ExistsHatenaIDRequest;
}

export namespace ExistsHatenaIDRequest {
  export type AsObject = {
    hatenaId: string,
  }
}

export class ExistsHatenaIDReply extends jspb.Message {
  getExisted(): boolean;
  setExisted(value: boolean): ExistsHatenaIDReply;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ExistsHatenaIDReply.AsObject;
  static toObject(includeInstance: boolean, msg: ExistsHatenaIDReply): ExistsHatenaIDReply.AsObject;
  static serializeBinaryToWriter(message: ExistsHatenaIDReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ExistsHatenaIDReply;
  static deserializeBinaryFromReader(message: ExistsHatenaIDReply, reader: jspb.BinaryReader): ExistsHatenaIDReply;
}

export namespace ExistsHatenaIDReply {
  export type AsObject = {
    existed: boolean,
  }
}

