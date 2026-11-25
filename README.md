# 投資用ワンルーム（15〜30㎡）中古マンション取引価格データ 2026（区別・築年別）

東京・横浜・川崎・名古屋・大阪の主要区について、専有面積15〜30㎡の中古マンション等の取引価格を、区別・築年別（2010年以降築／2009年以前築）に集計したデータです。

- 作成：株式会社煌海プロパティ（横浜市西区、投資用ワンルームの売却仲介）https://koumi-p.com/
- 解説ページ：https://koumi-p.com/oneroom-torihiki-kakaku-2026.html
- 元データ：国土交通省「不動産情報ライブラリ」不動産取引価格情報・成約価格情報（https://www.reinfolib.mlit.go.jp/）
- 対象期間：2025年第3四半期〜2026年第2四半期
- 対象：種類「中古マンション等」、専有面積15〜30㎡（国の公開データの表示値）
- 件数：5,991件（重複推定除去後）
- 更新：四半期ごと（次回 2027年1月予定）

## 列
| 列名 | 内容 |
|---|---|
| エリア / 区 | 集計した市区 |
| 取引件数 | 15〜30㎡の取引件数 |
| 全体の中央値(万円) | 全築年の中央値 |
| 2010年以降築_件数 / 中央値 / 25%値 / 75%値 | 建築年2010年以降の取引 |
| 2009年以前築_件数 / 中央値 / 25%値 / 75%値 | 建築年2009年以前の取引 |

価格は万円、10万円単位に四捨五入。件数0の項目は空欄。

## 集計方法
- 不動産取引価格情報と成約価格情報の両方に同じ取引が載っている場合があるため、市区町村・地区名・面積・建築年・価格が一致し、取引時期が同じか1四半期違いのデータを、当社独自の基準で同じ取引と推定し、1対1で照合して1件として数えています（成約価格情報側を除外）。公開情報の性質上、重複を完全に判別できるものではありません。
- 集計コード：aggregate.py（Python / pandas）

## 注意
- 賃貸中の投資用ワンルームだけの統計ではありません。自己居住用など異なる目的の取引も含まれます。
- 個別物件の査定額や売却可能価格を示すものではありません。

## ライセンス・出典表記
このデータは国土交通省「不動産情報ライブラリ」のデータを加工して作成しています。利用の際は次のように出典を記載してください。

> 出典：株式会社煌海プロパティ「投資用ワンルーム取引価格データ2026」（国土交通省 不動産情報ライブラリを加工）https://koumi-p.com/oneroom-torihiki-kakaku-2026.html

ライセンス：CC BY 4.0（上記の出典表記を条件に、複製・加工・再配布できます）

---

# Japan studio-apartment (15–30 m²) resale price data 2026, by ward and building age

Median and interquartile resale prices of used condominium units of 15–30 m² in major wards of Tokyo, Yokohama, Kawasaki, Nagoya and Osaka, split by construction year (2010+ / 2009 and earlier). Period: 2025 Q3 – 2026 Q2. Source: MLIT Real Estate Information Library (transaction and contract price data), processed by Koumi Property Co., Ltd. (Yokohama). Likely duplicates between the two source datasets were matched one-to-one and removed. License: CC BY 4.0 with attribution.
