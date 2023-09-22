import random
import string
from selenium import webdriver
import os

def generate_token():
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(32))

    full_link = "https://127.0.0.1:8000/thank_you/?token=" + unique_id

    # Webbrowser - only works on local environment - doesn't work on Heroku
    import webbrowser
    webbrowser.open_new_tab(full_link)

    # Trying Tkinter Library
    # Import tkinter and webview libraries
    # import webview

    # define an instance of tkinter
    # tk = Tk()

    #  size of the window where we show our website
    # tk.geometry("800x450")

    # Open website
    # webview.create_window('Connect Your Ad Data to Contrast', full_link)
    # webview.start()

    # Trying Selenium
    # selenium 4 - only works locally - doesn't work in Heroku environment
    #from selenium import webdriver
    #from selenium.webdriver.chrome.service import Service as ChromeService
    #from webdriver_manager.chrome import ChromeDriverManager

    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #driver.get(full_link)

    # Revised Selenium Code to work on Heroku environment - Code works - need to investigate how to tackle H12 error on Heroku
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument("window-size=1920x1480")
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver.get(full_link)
    # Fix Selenium browser to stay open until user finishes the action
    #while (True):
    #    pass

#    time.sleep(2)
#    driver.close()
    # Fix Selenium browser to stay open until user finishes the action
#    while (True):
#        pass
#    from selenium.webdriver import PhantomJS
#    from selenium.webdriver import DesiredCapabilities
#    import selenium.webdriver.support.ui as ui
    from selenium.common.exceptions import TimeoutException

#    dcap = dict(DesiredCapabilities.PHANTOMJS)
#    dcap["phantomjs.page.settings.userAgent"] = (
#        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")


#    phantomjs_path = "\.app\bin\phantomjs.exe"
#    browser = PhantomJS(executable_path=phantomjs_path, desired_capabilities=dcap)
#    wait = ui.WebDriverWait(browser, 20)
#    browser.get(full_link)
#    time.sleep(3)