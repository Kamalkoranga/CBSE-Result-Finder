from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

start_time = time.time()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Chrome driver

driver.get('https://testservices.nic.in/cbseresults/class_xii_2023/ClassTwelfth_c_2023.htm')  # Result URL
time.sleep(2)

SCHOOL_NO: int = 92733  # Write your own school code here

initial_point: int = 25656525  # Set the value from which number you want to start finding result
data: int = 1  # This variable is for distinguish between results's screenshot name
mothers_first_letter: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
students_first_letter: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

last_found = 65  # Here I used ASCII representation, for eg: 65 means A check https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html for full table
while True:
    for student in students_first_letter:
        found: bool = False
        for mother in mothers_first_letter:
            roll_no_input = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input")
            roll_no_input.send_keys(initial_point)
            school_no_input = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input")
            school_no_input.send_keys(SCHOOL_NO)
            admit_card_id_input = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td[2]/input")
            admit_card_id = chr(last_found) + mother + str(initial_point)[5:7] + str(8142)
            admit_card_id_input.send_keys(admit_card_id)
            admit_card_id_input.send_keys(Keys.ENTER)

            result_table = driver.find_elements(By.XPATH, "/html/body/div/div/center/table")
            if result_table:
                driver.save_screenshot(f"class12_results/result_{data}.png")  # capture the screenshot and put inside 'class12_results' folder
                print(f"Roll no:'{initial_point}'.................................. Found ✅")
                driver.get('https://testservices.nic.in/cbseresults/class_xii_2023/ClassTwelfth_c_2023.htm')
                time.sleep(2)
                data += 1
                found = True
                break
            else:
                print(f"Roll no:'{initial_point}'      -> Not Found")
                driver.get('https://testservices.nic.in/cbseresults/class_xii_2023/ClassTwelfth_c_2023.htm')
                time.sleep(2)
        if found:
            initial_point += 1
            break
        else:
            last_found += 1
        if student == "Z":
            initial_point += 1
    if initial_point == 25656600:  # Enter number when this program will be stoped
        break

driver.close()

print("--- %s seconds ---" % (time.time() - start_time))
