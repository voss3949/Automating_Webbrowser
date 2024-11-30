from selenium import webdriver
driver = webdriver.Chrome()

options = Options()
#make the browser invisible with a headless option
options.headless = True

driver.get("https://www.twitch.tv/directory/game/Art")


