# VoiceOS Hackathon Tokyo 2026-04-03

## イベント情報

- **日時**: 2026年4月3日（木）18:30〜22:00
- **会場**: 六本木（株式会社メルカリ）
- **テーマ**: VoiceOS Agent Mode - 声だけで開発する音声コマンド/ワークフロー

## チーム: PACSO

- メンバー:

## 開発テーマ: カスタム連携機能

VoiceOS Agent Modeで、**MCP（Model Context Protocol）を使ったカスタム連携機能**を開発します。

### 機能概要

ユーザーが声だけで外部サービスやツールとカスタム連携できる機能を構築。

### 実装アイデア

- MCPサーバー経由で外部APIと連携
- 音声コマンドで連携設定を実行
- 既存のMCPサーバーを活用した拡張

## 技術スタック

- [VoiceOS Agent Mode](https://www.voiceos.com/guide/build-mcp-integration)
- MCP（Model Context Protocol）
- Claude API

## アーキテクチャ

```
音声 → VoiceOS → 拡張機能 → MCPサーバー → 外部サービス
```

### MCPサーバーの役割

- VoiceOSからの音声コマンドを受け取る
- 外部サービスのAPIを呼び出す
- 結果をVoiceOSに返す

## セットアップ

1. VoiceOSを最新バージョンにアップデート
2. VoiceOSダッシュボードの「Agent Mode」を確認
3. Integrations ページで本拡張機能を接続
4. 音声でテスト実行

> 拡張機能の作り方: https://www.voiceos.com/guide/build-mcp-integration

## 開発ルール

1. **音声のみで操作**: タイピングなしで完結
2. **MCP準拠**: Model Context Protocolに従う
3. **シンプルに**: 2.5時間で実装できる範囲
4. **デモ重視**: 1分以内で伝わるデモ

## 提出物

- [x] GitHubリポジトリ
- [ ] 1分以内のデモ動画（画面録画）
- [ ] 短い説明文

> 提出先: https://vibecode.tokyo/voice-os-submit

### デモ動画で示すこと

- VoiceOSで拡張機能を呼び出し
- 音声コマンドを実行
- 外部サービス連携の結果を表示

## 開発ログ

- [x] リポジトリセットアップ
- [x] READMEルール策定
- [ ] MCPサーバー実装
- [ ] 外部サービス連携
- [ ] 動画撮影
- [ ] 審査

## リンク

- Discord: https://discord.gg/jGXasb3eme (`#voiceos-hackathon`)
- VoiceOS 拡張機能ガイド: https://www.voiceos.com/guide/build-mcp-integration
- 提出フォーム: https://vibecode.tokyo/voice-os-submit

---

VoiceOS Hackathon Tokyo 2026 / Team PACSO
