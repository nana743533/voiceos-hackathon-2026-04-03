from mcp.server.fastmcp import FastMCP

mcp = FastMCP("freee-accounting-voice")

# --- Mock Data ---
# 架空の事業所「株式会社テックスタート」（IT企業・従業員10名）
# freee APIを1回呼び出した想定のリアルなレスポンスデータ

COMPANY_NAME = "株式会社テックスタート"

MOCK_PROFIT_LOSS = {
    "売上高": 3_200_000,
    "売上原価": 1_200_000,
    "売上総利益": 2_000_000,
    "販売費及び一般管理費": {
        "合計": 1_500_000,
        "内訳": {
            "給料手当": 800_000,
            "法定福利費": 120_000,
            "地代家賃": 200_000,
            "通信費": 50_000,
            "広告宣伝費": 150_000,
            "消耗品費": 30_000,
            "旅費交通費": 80_000,
            "雑費": 70_000,
        },
    },
    "営業利益": 500_000,
    "営業外収益": 5_000,
    "営業外費用": 15_000,
    "経常利益": 490_000,
}

MOCK_PROFIT_LOSS_LAST_MONTH = {
    "売上高": 2_800_000,
    "売上原価": 1_050_000,
    "売上総利益": 1_750_000,
    "販売費及び一般管理費": {"合計": 1_450_000},
    "営業利益": 300_000,
    "経常利益": 290_000,
}

MOCK_WALLETABLES = [
    {"name": "三井住友銀行 渋谷支店", "type": "bank_account", "balance": 4_500_000},
    {"name": "住信SBIネット銀行", "type": "bank_account", "balance": 1_200_000},
    {"name": "事業用カード（VISA）", "type": "credit_card", "balance": -350_000},
    {"name": "現金", "type": "wallet", "balance": 80_000},
]

MOCK_UNSETTLED_DEALS = [
    {
        "partner": "株式会社ABC商事",
        "amount": 300_000,
        "issue_date": "2026-02-15",
        "due_date": "2026-03-31",
        "days_overdue": 3,
    },
    {
        "partner": "合同会社デザインワークス",
        "amount": 450_000,
        "issue_date": "2026-03-01",
        "due_date": "2026-04-30",
        "days_overdue": 0,
    },
    {
        "partner": "株式会社フューチャーテック",
        "amount": 120_000,
        "issue_date": "2026-03-10",
        "due_date": "2026-04-10",
        "days_overdue": 0,
    },
]


def _format_yen(amount: int) -> str:
    if amount < 0:
        return f"マイナス{abs(amount):,}円"
    return f"{amount:,}円"


@mcp.tool()
def get_profit_loss() -> str:
    """今月の損益計算書（P/L）の概況を取得します。売上高、売上原価、販管費、営業利益、経常利益がわかります。"""
    pl = MOCK_PROFIT_LOSS
    lines = [
        f"【{COMPANY_NAME}】2026年4月 損益概況",
        "",
        f"売上高:           {_format_yen(pl['売上高'])}",
        f"売上原価:         {_format_yen(pl['売上原価'])}",
        f"売上総利益:       {_format_yen(pl['売上総利益'])}",
        f"販管費合計:       {_format_yen(pl['販売費及び一般管理費']['合計'])}",
        f"営業利益:         {_format_yen(pl['営業利益'])}",
        f"経常利益:         {_format_yen(pl['経常利益'])}",
    ]
    return "\n".join(lines)


@mcp.tool()
def get_profit_loss_detail() -> str:
    """今月の損益計算書（P/L）の詳細を取得します。販管費の内訳が含まれます。"""
    pl = MOCK_PROFIT_LOSS
    lines = [
        f"【{COMPANY_NAME}】2026年4月 損益詳細",
        "",
        f"売上高:           {_format_yen(pl['売上高'])}",
        f"売上原価:         {_format_yen(pl['売上原価'])}",
        f"売上総利益:       {_format_yen(pl['売上総利益'])}",
        "",
        "【販売費及び一般管理費の内訳】",
    ]
    for name, amount in pl["販売費及び一般管理費"]["内訳"].items():
        lines.append(f"  {name}: {_format_yen(amount)}")
    lines.append(f"  ─────────────────")
    lines.append(f"  合計: {_format_yen(pl['販売費及び一般管理費']['合計'])}")
    lines.append("")
    lines.append(f"営業利益:         {_format_yen(pl['営業利益'])}")
    lines.append(f"経常利益:         {_format_yen(pl['経常利益'])}")
    return "\n".join(lines)


@mcp.tool()
def get_account_balances() -> str:
    """口座残高の一覧を取得します。銀行口座、クレジットカード、現金の残高がわかります。"""
    lines = [f"【{COMPANY_NAME}】口座残高一覧", ""]
    total = 0
    for w in MOCK_WALLETABLES:
        label = {"bank_account": "銀行", "credit_card": "カード", "wallet": "現金"}[
            w["type"]
        ]
        lines.append(f"[{label}] {w['name']}: {_format_yen(w['balance'])}")
        total += w["balance"]
    lines.append("")
    lines.append(f"合計残高: {_format_yen(total)}")
    return "\n".join(lines)


@mcp.tool()
def get_unsettled_deals() -> str:
    """未決済（未回収）の売上取引の一覧を取得します。取引先、金額、期日がわかります。"""
    lines = [f"【{COMPANY_NAME}】未決済の売上取引", ""]
    total = 0
    for deal in MOCK_UNSETTLED_DEALS:
        overdue = (
            f"（{deal['days_overdue']}日超過）" if deal["days_overdue"] > 0 else ""
        )
        lines.append(
            f"・{deal['partner']}: {_format_yen(deal['amount'])} "
            f"（期日: {deal['due_date']}）{overdue}"
        )
        total += deal["amount"]
    lines.append("")
    lines.append(f"合計: {len(MOCK_UNSETTLED_DEALS)}件 / {_format_yen(total)}")
    return "\n".join(lines)


@mcp.tool()
def compare_profit_loss() -> str:
    """今月と先月の損益を比較します。売上高、営業利益、経常利益の前月比がわかります。"""
    curr = MOCK_PROFIT_LOSS
    prev = MOCK_PROFIT_LOSS_LAST_MONTH
    lines = [f"【{COMPANY_NAME}】損益 前月比較（4月 vs 3月）", ""]

    for key in ["売上高", "営業利益", "経常利益"]:
        diff = curr[key] - prev[key]
        rate = (diff / prev[key]) * 100 if prev[key] != 0 else 0
        sign = "+" if diff >= 0 else ""
        lines.append(
            f"{key}: {_format_yen(curr[key])}（前月: {_format_yen(prev[key])}、"
            f"{sign}{_format_yen(diff)}、{sign}{rate:.1f}%）"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
