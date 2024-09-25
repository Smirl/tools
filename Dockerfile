FROM --platform=linux/amd64 alpine:3.20.3
WORKDIR /opt/
ENV ENV="/root/.profile"
RUN apk add --no-cache curl bind-tools jq yq hey aws-cli && \
    wget https://github.com/ktr0731/evans/releases/download/v0.10.11/evans_linux_amd64.tar.gz && \
    tar -xvf evans_linux_amd64.tar.gz &&    \
    mv ./evans /bin/ && \
    wget https://github.com/bojand/ghz/releases/download/v0.120.0/ghz-linux-x86_64.tar.gz && \
    tar -xvf ghz-linux-x86_64.tar.gz &&    \
    mv ./ghz /bin/ && \
    rm -rf evans_linux_amd64.tar.gz ghz-linux-x86_64.tar.gz LICENSE ghz-web
COPY .profile /root/.profile
COPY ./proto/ ./proto/
COPY README.md .
