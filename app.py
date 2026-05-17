import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ① ページ設定
st.set_page_config(page_title="在庫管理", layout="wide")

st.title("COBOL × Python 在庫管理システム")

# 説明
st.write("COBOLで在庫更新を行い、Pythonで分析・可視化しています。")

# GitHubリンク
st.markdown(
    "[GitHubはこちら](https://github.com/gannoji88-cloud/stock-management-app.git)"
)

st.subheader("在庫データ分析ダッシュボード")

st.markdown("""
### 使用技術
- COBOL
- Python
- pandas
- matplotlib
- Streamlit
""")

st.divider()

# データ読み込み
df = pd.read_fwf(
    "master_new.dat",
    widths=[5, 20, 5],
    names=["id", "name", "stock"]
)

df["name"] = df["name"].str.strip()

# ② KPI表示
col1, col2, col3 = st.columns(3)
col1.metric("商品数", len(df))
col2.metric("在庫合計", df["stock"].sum())
col3.metric("最小在庫", df["stock"].min())

# ⑤ フィルタ
threshold = st.slider("在庫しきい値", 0, 200, 80)

st.subheader("在庫一覧")
st.dataframe(df)

# フィルタ結果
st.subheader("在庫不足商品")
filtered = df[df["stock"] < threshold]
st.dataframe(filtered)

# ③ グラフ
st.subheader("在庫グラフ")
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(df["name"], df["stock"])
ax.set_title("在庫状況")
st.pyplot(fig)

# ④ CSVダウンロード
st.download_button(
    "CSVダウンロード",
    df.to_csv(index=False),
    "stock.csv"
)
