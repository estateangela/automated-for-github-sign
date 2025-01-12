import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)


# 加載環境變數
load_dotenv()

# 取得環境變數中的搜尋關鍵字
SEARCH_KEYWORD = os.getenv("SEARCH_KEYWORD")

if not SEARCH_KEYWORD:
    raise ValueError("環境變數 SEARCH_KEYWORD 未設置，請在 .env 文件中配置")

# 初始化 WebDriver
driver = webdriver.Chrome()

try:
    # 1. 開啟 Google 首頁
    driver.get("https://www.google.com")

    # 等待頁面載入完成
    time.sleep(2)

    # 2. 找到搜尋框並輸入關鍵字
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(SEARCH_KEYWORD)
    search_box.send_keys(Keys.RETURN)

    # 3. 驗證搜尋結果頁面是否正確載入
    time.sleep(3)  # 等待搜尋結果頁面載入
    assert SEARCH_KEYWORD in driver.title, f"搜尋關鍵字未出現在頁面標題中：{driver.title}"

    print("搜尋測試成功！")

except Exception as e:
    print(f"測試失敗：{e}")

finally:
    # 關閉瀏覽器
    driver.quit()
