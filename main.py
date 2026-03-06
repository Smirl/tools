#!/usr/bin/env python3
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Kubernetes debugging tools helper"
    )
    subparsers = parser.add_subparsers(dest="command")

    # grpc subcommand
    grpc_parser = subparsers.add_parser("grpc", help="gRPC utilities")
    grpc_parser.add_argument("host", help="Target host (e.g. localhost:50051)")
    grpc_parser.add_argument("--proto-dir", default="/proto", help="Proto files directory")

    # http subcommand
    http_parser = subparsers.add_parser("http", help="HTTP utilities")
    http_parser.add_argument("url", help="Target URL")
    http_parser.add_argument("-n", "--requests", type=int, default=100, help="Number of requests")
    http_parser.add_argument("-c", "--concurrency", type=int, default=10, help="Concurrency level")

    # info subcommand
    subparsers.add_parser("info", help="Show available tools and proto files")

    args = parser.parse_args()

    if args.command == "info":
        print("Available tools: awscli, evans, ghz, hey, jq, yq, curl, dig")
        print("Proto files: /proto/thanos, /proto/grpc.health.v1, /proto/infrabin")
    elif args.command == "grpc":
        print(f"evans --host {args.host} --path {args.proto_dir}")
    elif args.command == "http":
        print(f"hey -n {args.requests} -c {args.concurrency} {args.url}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
