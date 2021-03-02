FROM node:15-buster

WORKDIR /pb

RUN npm i rimraf -g
RUN curl -L -O https://github.com/protocolbuffers/protobuf/releases/download/v3.15.2/protoc-3.15.2-linux-x86_64.zip
RUN curl -L -O https://github.com/grpc/grpc-web/releases/download/1.2.1/protoc-gen-grpc-web-1.2.1-linux-x86_64
RUN unzip protoc-3.15.2-linux-x86_64.zip && cp ./bin/protoc /usr/local/bin/. && chmod +x /usr/local/bin/protoc
RUN cp protoc-gen-grpc-web-1.2.1-linux-x86_64 /usr/local/bin/protoc-gen-grpc-web && chmod +x /usr/local/bin/protoc-gen-grpc-web
