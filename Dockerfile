FROM frolvlad/alpine-glibc:alpine-3.12
WORKDIR /opt/
RUN apk add --no-cache curl bind-tools jq groff && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    wget https://github.com/ktr0731/evans/releases/download/0.9.0/evans_linux_amd64.tar.gz && \
    tar -xvf evans_linux_amd64.tar.gz &&    \
    mv ./evans /bin/ && \
    rm -rf ./aws/ awscliv2.zip evans_linux_amd64.tar.gz
COPY ./proto/ ./proto/
