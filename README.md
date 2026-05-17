# 在庫管理システム（COBOL × Python）

## 概要
COBOLで在庫更新バッチを構築し、
Pythonで分析・可視化を行う在庫管理システムです。

## 使用技術
- COBOL（GnuCOBOL）
- Python
- pandas
- matplotlib
- Streamlit

## 機能
- 在庫更新バッチ
- 在庫分析
- グラフ表示
- ダッシュボード表示

## 画面イメージ
![stock](stock.png)

## システム構成図
```text
+------------------+
| COBOL Batch      |
| update_stock.cob |
+------------------+
          |
          v
+------------------+
| master_new.dat   |
| Inventory Data   |
+------------------+
          |
          v
+------------------+
| Python Analysis  |
| pandas/matplotlib|
+------------------+
          |
          v
+------------------+
| Streamlit UI     |
| Dashboard        |
+------------------+
          |
          v
+------------------+
| Browser          |
| Web Application  |
+------------------+
```