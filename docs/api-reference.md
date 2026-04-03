# freee 会計API リファレンス（照会系）

本プロジェクトで使用する freee 会計APIのエンドポイント一覧。
すべて `freee_api_get` ツール経由で呼び出す。`company_id` は全エンドポイントで必須。

---

## 帳表・レポート系

### 損益計算書（P/L）

| エンドポイント | 説明 |
|---|---|
| `GET /api/1/reports/trial_pl` | 当期の損益計算書 |
| `GET /api/1/reports/trial_pl_two_years` | 前年比較の損益計算書 |
| `GET /api/1/reports/trial_pl_three_years` | 3期間比較の損益計算書 |

**主なパラメータ:**
- `company_id`（必須）
- `fiscal_year` — 会計年度
- `start_month` / `end_month` — 月指定
- `start_date` / `end_date` — 日付指定
- `account_item_display_type` — `account_item`（勘定科目）/ `group`（決算書表示名）
- `breakdown_display_type` — 内訳表示（partner / item / section）

**レスポンス主要フィールド:**
- `closing_balance` — 期末残高（発生額）
- `debit_amount` / `credit_amount` — 借方/貸方金額
- `composition_ratio` — 構成比
- 前年比較版: `last_year_closing_balance`, `year_on_year`

### 貸借対照表（B/S）

| エンドポイント | 説明 |
|---|---|
| `GET /api/1/reports/trial_bs` | 当期の貸借対照表 |
| `GET /api/1/reports/trial_bs_two_years` | 前年比較の貸借対照表 |
| `GET /api/1/reports/trial_bs_three_years` | 3期間比較の貸借対照表 |

**レスポンス主要フィールド:**
- `opening_balance` — 期首残高
- `closing_balance` — 期末残高
- `debit_amount` / `credit_amount` — 借方/貸方金額

---

## 取引・仕訳系

### 取引一覧（Deals）

`GET /api/1/deals`

**主なパラメータ:**
- `type` — `income`（収入）/ `expense`（支出）
- `status` — `unsettled`（未決済）/ `settled`（決済済み）
- `partner_id` / `partner_code` — 取引先
- `account_item_id` — 勘定科目
- `start_issue_date` / `end_issue_date` — 発生日範囲
- `start_due_date` / `end_due_date` — 支払期日範囲
- `offset` / `limit`（最大100）

**レスポンス主要フィールド:**
- `id`, `issue_date`, `due_date`
- `amount` — 金額
- `due_amount` — 支払残額
- `type` — 収支区分
- `status` — 決済状況
- `partner` — 取引先情報
- `details[]` — 明細行

---

## マスターデータ系

### 口座一覧（Walletables）

`GET /api/1/walletables`

**主なパラメータ:**
- `with_balance=true` — 残高を含める
- `type` — `bank_account` / `credit_card` / `wallet`

**レスポンス主要フィールド:**
- `id`, `name`, `type`
- `walletable_balance` — 登録残高
- `last_balance` — 同期残高

### 勘定科目一覧（Account Items）

`GET /api/1/account_items`

**レスポンス主要フィールド:**
- `id`, `name`, `code`
- `account_category` — カテゴリー（売上高、販管費、etc.）
- `tax_code` — 税区分

### 取引先一覧（Partners）

`GET /api/1/partners`

**主なパラメータ:**
- `keyword` — 部分一致検索（名前・コード・カナ）
- `offset` / `limit`（最大3000）

### 事業所情報（Companies）

`GET /api/1/companies/{id}`

**主なパラメータ:**
- `details=true` — マスターデータ一括取得
- `account_items=true`, `taxes=true`, `partners=true` 等で個別指定可

---

## 注意事項

- `company_id` の取得: `freee_get_current_company` ツールで現在の事業所IDを確認
- 試算表API: レスポンスの `up_to_date` フラグが `false` の場合、集計が未完了の可能性あり
- ページネーション: deals は最大100件/回、partners は最大3000件/回
