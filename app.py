import streamlit as st
import sqlite3
import pandas as pd
from duckduckgo_search import DDGS
from datetime import datetime

# ===========================
# 1. 数据库部分
# ===========================
def init_db():
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (title TEXT, link TEXT UNIQUE, source TEXT, category TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(data_list):
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()
    count = 0
    for item in data_list:
        try:
            c.execute("INSERT OR IGNORE INTO articles VALUES (?, ?, ?, ?, ?)",
                      (item['title'], item['link'], item['source'], item['category'], item['date']))
            if c.rowcount > 0:
                count += 1
        except Exception as e:
            print(f"Error: {e}")
    conn.commit()
    conn.close()
    return count

def load_data():
    conn = sqlite3.connect('my_data.db')
    try:
        df = pd.read_sql_query("SELECT * FROM articles ORDER BY date DESC", conn)
    except:
        df = pd.DataFrame(columns=["title", "link", "source", "category", "date"])
    conn.close()
    return df

# ===========================
# 2. 核心逻辑部分
# ===========================
def simple_classify(text):
    text = text.lower()
    if any(k in text for k in ['ai', 'gpt', '模型', '智能']):
        return "人工智能"
    elif any(k in text for k in ['价格', '股市', '基金', '赚钱', '财经']):
        return "财经"
    elif any(k in text for k in ['python', '代码', '开发', 'web']):
        return "技术编程"
    else:
        return "其他资讯"

def fetch_gzh_data():
    # 模拟数据
    return [
        {"title": "公众号文章：AI的新趋势", "link": "http://wx.qq.com/1", "source": "公众号API", "category": "", "date": str(datetime.now())},
        {"title": "公众号文章：Python入门教程", "link": "http://wx.qq.com/2", "source": "公众号API", "category": "", "date": str(datetime.now())}
    ]

def search_public_web(keyword, num_results=5):
    results = []
    try:
        with DDGS() as ddgs:
            search_gen = ddgs.text(f"{keyword}", region='cn-zh', max_results=num_results)
            if search_gen:
                for r in search_gen:
                    results.append({
                        "title": r['title'],
                        "link": r['href'],
                        "source": "全网搜索",
                        "category": "",
                        "date": str(datetime.now())
                    })
    except Exception as e:
        st.error(f"搜索出错: {e}")
    return results

# ===========================
# 3. 网站界面部分
# ===========================
init_db()
st.set_page_config(page_title="我的情报收集站", layout="wide")
st.title("🕵️‍♂️ 个人情报聚合系统")

with st.sidebar:
    st.header("操作面板")
    st.subheader("1. 公众号采集")
    if st.button("运行公众号API抓取"):
        with st.spinner('正在连接API...'):
            raw_data = fetch_gzh_data()
            for item in raw_data:
                item['category'] = simple_classify(item['title'])
            saved_num = save_to_db(raw_data)
        st.success(f"成功保存 {saved_num} 篇公众号文章！")

    st.markdown("---")
    st.subheader("2. 全网关键词搜索")
    keyword = st.text_input("输入关键词", "人工智能")
    count = st.slider("抓取数量", 1, 10, 5)
    
    if st.button("开始全网搜索"):
        with st.spinner(f'正在全网搜索 "{keyword}" ...'):
            web_data = search_public_web(keyword, count)
            if web_data:
                for item in web_data:
                    item['category'] = simple_classify(item['title'] + " " + keyword)
                saved_num = save_to_db(web_data)
                st.success(f"搜索完成，新入库 {saved_num} 条信息！")
            else:
                st.warning("未搜索到相关内容，请稍后再试。")

st.header("📚 已归档的信息库")
df = load_data()
if not df.empty:
    cat_filter = st.selectbox("按分类筛选", ["全部"] + list(df['category'].unique()))
    if cat_filter != "全部":
        df_show = df[df['category'] == cat_filter]
    else:
        df_show = df
    
    st.dataframe(
        df_show, 
        column_config={
            "link": st.column_config.LinkColumn("文章链接"),
            "date": st.column_config.DatetimeColumn("抓取时间")
        },
        use_container_width=True
    )
else:
    st.info("数据库目前是空的，请在左侧进行抓取。")
