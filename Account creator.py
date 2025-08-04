

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import random
NUM_ACCOUNTS = 50
fake = Faker()
driver = webdriver.Chrome()
signup_url = "https://app.heyclyra.com/register" 
email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

for i in range(NUM_ACCOUNTS):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name + last_name
    email = f"{username}@{random.choice(email_domains)}"
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

    try:
        driver.get(signup_url)
        time.sleep(2)
        driver.find_element(By.XPATH, '//input[@placeholder="First name"]').send_keys(first_name)
        driver.find_element(By.XPATH, '//input[@placeholder="Last name"]').send_keys(last_name)
        driver.find_element(By.XPATH, '//input[@placeholder="john@gmail.com"]').send_keys(email)
        driver.find_element(By.XPATH, '//input[@placeholder="••••••"]').send_keys(password)
        driver.find_element(By.XPATH, '//input[@placeholder="Re-enter password"]').send_keys(password)
        driver.find_element(By.XPATH, '//button[text()="Register"]').click()

        print(f"[{i+1}/{NUM_ACCOUNTS}] An account has been created: {first_name} {last_name} / {email} / {password}")
        time.sleep(random.uniform(2, 5))

    except Exception as e:
        print(f"[{i+1}]A proplem While Singnning in . {e}")
        continue

driver.quit()
print("All Accounts have been created")