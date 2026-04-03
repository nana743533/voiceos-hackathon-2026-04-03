# アーキテクチャ設計

## システム構成

```
┌─────────┐     ┌──────────┐     ┌───────────────────────────────┐
│  ユーザー │────▶│  VoiceOS  │────▶│  カスタム拡張機能 (MCP Server) │
│ （音声）  │◀────│  Agent    │◀────│  Mockデータで freee 会計を再現  │
└─────────┘     └──────────┘     └───────────────────────────────┘
```

> **注**: ハッカソンの時間制約により、freee API への実接続（OAuth認証）は行わない。
> freee APIを1回呼び出した想定のリアルなMockデータを返すMCPサーバーを実装する。
> 本番化する際は、Mockレイヤーを freee-mcp（`https://mcp.freee.co.jp/mcp`）への接続に差し替える。

## データフロー

1. ユーザーが音声で質問（例：「今月の売上は？」）
2. VoiceOS Agent Mode が音声を解釈し、MCPサーバーの適切なツールを呼び出す
3. MCPサーバーが **Mockデータ**（freee APIレスポンス形式）を返す
4. VoiceOS がユーザーに音声で読み上げる

## MCPサーバーが提供するツール

### コア機能（P0）

| ツール名 | 説明 | Mock元のAPI |
|---------|------|------------|
| `get_profit_loss` | 今月の損益概況を取得 | `GET /api/1/reports/trial_pl` |
| `get_account_balances` | 口座残高一覧を取得 | `GET /api/1/walletables?with_balance=true` |

### 拡張機能（P1）

| ツール名 | 説明 | Mock元のAPI |
|---------|------|------------|
| `get_unsettled_deals` | 未決済の取引一覧を取得 | `GET /api/1/deals?status=unsettled` |

### オプション（P2）

| ツール名 | 説明 | Mock元のAPI |
|---------|------|------------|
| `compare_profit_loss` | 前月比較の損益を取得 | `GET /api/1/reports/trial_pl_two_years` |
| `get_account_item_amount` | 特定科目の発生額を取得 | `GET /api/1/reports/trial_pl` + フィルタ |

## Mockデータ方針

- freee APIのレスポンス形式に準拠したリアルなデータ
- 架空の事業所「株式会社テックスタート」（IT企業、従業員10名規模）を想定
- 2026年4月時点の当月・前月データを用意
- 金額は中小企業として自然な範囲

## 技術スタック

- **ランタイム**: Node.js (TypeScript)
- **MCP SDK**: `@modelcontextprotocol/sdk`
- **トランスポート**: Streamable HTTP（VoiceOS連携用）
