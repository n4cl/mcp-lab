# mcp-lab

このリポジトリは、FastMCPプロトコルを使用した時間サーバーの実装とテストを含んでいます。

## ディレクトリ構造

プロジェクトのコードベースは、以下のディレクトリ構造に整理されています。

- `src/`: アプリケーションのソースコードが含まれています。
  - `time_server.py`: FastMCP時間サーバーのメインロジック。
- `tests/`: テストコードが含まれています。
  - `test_time_server.py`: `pytest`を使用した時間サーバーのテスト。

## テストの実行

テストは`pytest`フレームワークを使用しています。テストを実行するには、以下のコマンドを使用します。

```bash
pytest tests/
```

## Dockerについて

このプロジェクトはDockerを使用してコンテナ化されています。

- `Dockerfile`: アプリケーションとテスト環境を構築するためのDockerイメージの定義。
- `docker-compose.yml`: Docker Composeを使用して、時間サーバーを起動するための設定。

### Dockerイメージのビルド

```bash
docker build -t fastmcp-time-server .
```

### Docker Composeを使用したサーバーの起動

```bash
docker-compose up
```