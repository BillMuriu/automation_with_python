from selenium import webdriver
import time

with open('socket_type_scraping.csv', 'w') as file:
    file.write("Turbo_speed \n")

driver=webdriver.Chrome()


driver.get('https://pcbuilder.net/product/processor/')
time.sleep(1)


product_titles=driver.find_elements("xpath", "(//div[@class='table_title'])")
price=driver.find_elements("xpath", "(//td[@class='price'])")
brand=driver.find_elements("xpath", "(//div[@class='detail__value f_brand'])")
cores=driver.find_elements("xpath", "(//div[@class='detail__value f_cores'])")
base_speed=driver.find_elements("xpath", "(//div[@class='detail__value f_maximum_speed'])")
threads=driver.find_elements("xpath", "(//div[@class='detail__value f_threads'])")
model=driver.find_elements("xpath", "(//div[@class='detail__value f_model'])")
socket_type=driver.find_elements("xpath", "(//div[@class='detail__value f_socket_type'])")
turbo_speed=driver.find_elements("xpath", "(//div[@class='detail__value f_maximum_speed'])")

with open('socket_type_scraping.csv', 'a') as file:
    for i in range(len(product_titles)):
        file.write(socket_type[i].text + "\n")
