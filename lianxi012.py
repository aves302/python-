"""
使用 requests 库来发起 GET 请求，获取网页内容
"""
import requests

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to retrieve webpage. Status code: {response.status_code}"

# 示例：获取一个网页内容
url = "https://www.example.com"
page_content = fetch_webpage(url)
print(page_content[:200])  # 输出前 200 个字符
