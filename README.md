# tools
Lightweight docker image for debugging kubernetes

Use it from docker hub https://hub.docker.com/repository/docker/smirl/tools

## Included tools

- `curl`
- `bind-tools` - (`dig`, etc.)
- [`jq`](https://stedolan.github.io/jq/)
- [`evans`](https://github.com/ktr0731/evans)
- [`awscli`](https://aws.amazon.com/cli/)

## Included proto files

There are some packaged proto files for gRPC services, etc. In case the servers do not have reflection enabled.

- [`thanos`](https://github.com/thanos-io/thanos)
- [`grpc.health.v1`](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)
- [`infrabin`](https://github.com/maruina/go-infrabin/)
- [`google.api.http`](https://cloud.google.com/endpoints/docs/grpc/transcoding)
