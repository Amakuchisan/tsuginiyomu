FROM golang:1.15-alpine

RUN apk --update add git protoc

WORKDIR /pb
COPY go.mod go.sum ./
RUN go install github.com/golang/protobuf/protoc-gen-go
