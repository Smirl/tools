# tools
Lightweight docker image for debugging kubernetes

Use it from docker hub https://hub.docker.com/repository/docker/smirl/tools

## Included tools

| Tool | Version | Description |
|------|---------|-------------|
| [`awscli`](https://aws.amazon.com/cli/) | latest | AWS command line interface |
| [`evans`](https://github.com/ktr0731/evans) | v0.10.11 | gRPC client |
| [`ghz`](https://ghz.sh/) | v0.120.0 | gRPC benchmarking tool |
| [`hey`](https://github.com/rakyll/hey) | latest | HTTP load generator |
| [`jq`](https://stedolan.github.io/jq/) | latest | JSON processor |
| [`yq`](https://github.com/mikefarah/yq) | latest | YAML/JSON/XML processor |
| [`bind-tools`](https://www.isc.org/bind/) | latest | DNS utilities (`dig`, `nslookup`, etc.) |
| `curl` | latest | HTTP client |

## Included proto files

There are some packaged proto files for gRPC services, etc. In case the servers do not have reflection enabled.

- [`thanos`](https://github.com/thanos-io/thanos)
- [`grpc.health.v1`](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)
- [`infrabin`](https://github.com/maruina/go-infrabin/)
- [`google.api.http`](https://cloud.google.com/endpoints/docs/grpc/transcoding)
