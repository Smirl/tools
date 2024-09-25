# tools
Lightweight docker image for debugging kubernetes

Use it from docker hub https://hub.docker.com/repository/docker/smirl/tools

## Included tools

- [`awscli`](https://aws.amazon.com/cli/)
- [`evans`](https://github.com/ktr0731/evans)
- [`ghz`](https://ghz.sh/)
- [`hey`](https://github.com/rakyll/hey)
- [`jq`](https://stedolan.github.io/jq/)
- [`yq`](https://github.com/mikefarah/yq)
- `bind-tools` - (`dig`, etc.)
- `curl`

## Included proto files

There are some packaged proto files for gRPC services, etc. In case the servers do not have reflection enabled.

- [`thanos`](https://github.com/thanos-io/thanos)
- [`grpc.health.v1`](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)
- [`infrabin`](https://github.com/maruina/go-infrabin/)
- [`google.api.http`](https://cloud.google.com/endpoints/docs/grpc/transcoding)
