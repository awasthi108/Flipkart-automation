from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def launch_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def close_login_popup(driver):
    try:
        close_button = driver.find_element(By.XPATH, "//button[text()='✕']")
        close_button.click()
    except:
        pass 

def search_product(driver, query):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

def test_valid_search():
    driver = launch_browser()
    driver.get("https://www.flipkart.com")
    time.sleep(2)

    close_login_popup(driver)
    search_product(driver, "laptop")
    time.sleep(5)

    driver.save_screenshot("valid_search.png")

    if "results" in driver.page_source.lower():
        print("✅ TC01 - Valid Search: Passed")
    else:
        print("❌ TC01 - Valid Search: Failed")

    driver.quit()

def test_invalid_search():
    driver = launch_browser()
    driver.get("https://www.flipkart.com")
    time.sleep(2)

    close_login_popup(driver)
    search_product(driver, "xyz123@!!")
    time.sleep(5)

    driver.save_screenshot("invalid_search.png")

    if "no results found" in driver.page_source.lower():
        print("✅ TC02 - Invalid Search: Passed")
    else:
        print("❌ TC02 - Invalid Search: Failed")

    driver.quit()

def test_filter_application():
    driver = launch_browser()
    driver.get("https://www.flipkart.com")
    time.sleep(2)

    close_login_popup(driver)
    search_product(driver, "laptop")
    time.sleep(5)

    driver.execute_script("window.scrollBy(0, 300)")
    time.sleep(2)

    try:
        hp_checkbox = driver.find_element(By.XPATH, "//div[text()='Brand']/following::div[text()='HP'][1]")
        hp_checkbox.click()
        time.sleep(5)

        driver.save_screenshot("filter_applied.png")

        if "hp" in driver.page_source.lower():
            print("✅ TC03 - Brand Filter: Passed")
        else:
            print("❌ TC03 - Brand Filter: Failed (Filter applied but not reflected in results)")
    except:
        print("❌ TC03 - Brand Filter: Failed (Error applying filter)")

    driver.quit()

if __name__ == "__main__":
    print("🚀 Flipkart Automation Tests Starting...\n")
    test_valid_search()
    test_invalid_search()
    test_filter_application()
    print("\n✅ All tests completed.")
