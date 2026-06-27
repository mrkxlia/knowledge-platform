# ADR-0002: Adopt FastAPI

## Status

Accepted

## Context

このプロジェクトでは、AI Knowledge Platformのバックエンドフレームワークを選定する必要がある。

要件

- REST APIを簡単に作れること
- OpenAPI(Swagger)を自動生成できること
- 型ヒントを活用できること
- AWS Lambdaへデプロイしやすいこと
- AI関連ライブラリとの相性が良いこと

## Decision

FastAPIを採用する。

## Rationale

- 型ヒントベースで保守しやすい
- OpenAPIを自動生成する
- AIアプリで広く利用されている
- 非同期処理をサポート
- AWS Lambdaとの相性が良い

## Alternatives

### Flask

シンプルだがSwaggerや型のサポートが弱い。

### Django

高機能だが今回の用途ではオーバースペック。

## Consequences

### Positive

- API開発が高速
- Swaggerが利用できる
- AI開発で採用事例が多い

### Negative

- Djangoほど機能は多くない