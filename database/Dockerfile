# FROM postgres:16

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     git \
#     postgresql-server-dev-16

# RUN git clone https://github.com/pgvector/pgvector.git && \
#     cd pgvector && \
#     make && \
#     make install

# CMD ["postgres"]
# RUN echo "CREATE EXTENSION IF NOT EXISTS vector;" > /docker-entrypoint-initdb.d/init-vector.sql
FROM postgres:latest

# alternative: https://raw.githubusercontent.com/run-llama/llama_index/main/llama-index-legacy/tests/initialization/postgres/Dockerfile

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    postgresql-server-dev-all \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
# installing the pgvector extension for postgres
RUN git clone https://github.com/pgvector/pgvector.git

WORKDIR /tmp/pgvector
RUN make
RUN make install