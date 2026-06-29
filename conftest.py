import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = Options()
    
    # ADD this line to hide the browser UI
    options.add_argument('--headless')
    
    # Optional but recommended for headless stability:
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
