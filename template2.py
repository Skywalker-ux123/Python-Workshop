import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("🚀 Launching Auto-Speed Test...")

# 1. Open the browser
driver = webdriver.Chrome()

try:
    # 2. Go to the website
    # TODO: Tell the driver to 'get' https://fast.com
    driver.get("YOUR_CODE_HERE")
    
    print("⏳ Waiting for the internet speed test to finish...")

    # 3. Wait for the result
    wait = WebDriverWait(driver, 60)
    
    # TODO: Find the element where the final speed is displayed 
    # (Hint: the ID is 'speed-value' and it gets a class 'succeeded' when done)
    speed_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "YOUR_CSS_SELECTOR_HERE"))
    )

    print(f"\n🌐 Your Internet Speed is: {speed_element.text} Mbps")

finally:
    time.sleep(3)
    driver.quit()