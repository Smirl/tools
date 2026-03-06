# Contributing

Contributions are welcome! This project is a lightweight Docker image for debugging Kubernetes, bundling useful CLI tools and proto files.

## Ways to contribute

- **Add a new tool** — suggest or add a tool useful for Kubernetes/gRPC debugging
- **Update tool versions** — bump a pinned version in the `Dockerfile`
- **Add proto files** — include proto definitions for additional gRPC services
- **Fix bugs or improve docs**

## Getting started

1. Fork the repository and create a branch from `main`.
2. Make your changes.
3. Test locally by building the image:
   ```sh
   docker build -t tools:local .
   ```
4. Verify the tools you changed or added work as expected inside the container:
   ```sh
   docker run --rm -it tools:local sh
   ```
5. Open a pull request against `main`.

## Adding a tool

- Prefer tools available via `apk` (Alpine packages) to keep the image small.
- If a binary must be downloaded, pin an explicit version and use the official release URL, as done for `evans` and `ghz` in the `Dockerfile`.
- Remove any unnecessary files (archives, licenses, extra binaries) after installation.
- Update the **Included tools** section in `README.md`.

## Adding proto files

Place new `.proto` files under the appropriate subdirectory of `proto/`, mirroring the upstream package structure. Update the **Included proto files** section in `README.md` with a link to the upstream source.

## Commit style

Use short, descriptive commit messages in the imperative mood (e.g., `Add grpc-health-probe tool`, `Bump evans to v0.10.12`).

## License

By contributing you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
