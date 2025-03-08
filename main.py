from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import time
import os
import shutil
from colorama import Fore, init
from itertools import cycle
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
    WebDriverException,
)
from selenium.webdriver.chrome.options import Options

init(autoreset=True)

csv_file_path = "ScratchAccountCSV.csv"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art_with_animation():
    art = r"""
  _________                    __         .__     __  .__               __                
 /   _____/ ________________ _/  |_  ____ |  |___/  |_|__|__  _______ _/  |_  ___________ 
 \_____  \_/ ___\_  __ \__  \\   __\/ ___\|  |  \   __\  \  \/ /\__  \\   __\/  _ \_  __ \
 /        \  \___|  | \// __ \|  | \  \___|   Y  \  | |  |\   /  / __ \|  | (  <_> )  | \/
/_______  /\___  >__|  (____  /__|  \___  >___|  /__| |__| \_/  (____  /__|  \____/|__|   
        \/     \/           \/          \/     \/                    \/                   
    """
    console_width = shutil.get_terminal_size().columns
    colors = cycle([Fore.RED, Fore.LIGHTRED_EX])

    for _ in range(10):
        clear_console()
        color = next(colors)
        for line in art.splitlines():
            print(color + line.center(console_width))
        time.sleep(0.2)

    print(Fore.RED + "Made by Kyra".center(console_width))
    time.sleep(3)

def progress_bar(current, total, last_checked_account="", bar_length=40):
    clear_console()
    percent = int(current / total * 100)
    bar = ('█' * int(bar_length * percent / 100)).ljust(bar_length)
    if last_checked_account:
        print(Fore.LIGHTRED_EX + f"[{bar}] {percent}% Complete - Last checked account: {last_checked_account}", end="\r")
    else:
        print(Fore.LIGHTRED_EX + f"[{bar}] {percent}% Complete", end="\r")

def activate_scratch_account(username, password):
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # disable chrome logs
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://scratch.mit.edu/login/")
    username_input = driver.find_element(By.ID, "id_username")
    password_input = driver.find_element(By.ID, "id_password")
    username_input.send_keys(username)
    password_input.send_keys(password.strip())

    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[style='margin-top:10px;'] button[type='submit']"))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[style='margin-top:10px;'] button[type='submit']"))
        )
        login_button.click()
    except TimeoutException:
        print(Fore.LIGHTRED_EX + f"Error: Login button not found or not clickable for {username}.")
        driver.quit()
        return
    except NoSuchElementException:
        print(Fore.LIGHTRED_EX + f"Error: Username or password field not found for {username}.")
        driver.quit()
        return
    except ElementNotInteractableException:
        print(Fore.LIGHTRED_EX + f"Error: Login button is not interactable for {username}.")
        driver.quit()
        return
    except WebDriverException as e:
        print(Fore.LIGHTRED_EX + f"Error: WebDriver error during login for {username}: {e}")
        driver.quit()
        return
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Unknown error during login for {username}: {e}")
        driver.quit()
        return

    time.sleep(3)
    if "complete_registration" in driver.current_url:
        try:
            driver.find_element(By.XPATH, "//button[@class='button card-button' and @type='submit']").click()
            time.sleep(1)
            month_select = Select(driver.find_element(By.NAME, "user.birth.month"))
            month_select.select_by_value("1")
            year_select = Select(driver.find_element(By.NAME, "user.birth.year"))
            year_select.select_by_value("2010")
            driver.find_element(By.XPATH, "//input[@type='radio' and @value='female']").click()
            country_select = Select(driver.find_element(By.NAME, "countryCode"))
            country_select.select_by_value("au")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[@class='button card-button' and @type='submit']").click()
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Error during activation for {username}: {e}")
    driver.quit()

def activate_accounts_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        accounts = list(reader)
        total_accounts = len(accounts)
        for index, row in enumerate(accounts):
            if len(row) == 2:
                username, password = row
                activate_scratch_account(username, password)
                progress_bar(index + 1, total_accounts, username)
            else:
                print(Fore.LIGHTRED_EX + f"Invalid CSV line: {row}")

def change_endpoint():
    global csv_file_path
    clear_console()
    print(Fore.LIGHTRED_EX + "Current CSV File Location: " + csv_file_path)
    new_path = input(Fore.RED + "Enter the new CSV file path: ")
    if os.path.exists(new_path):
        csv_file_path = new_path
        print(Fore.LIGHTRED_EX + "CSV file path updated successfully!")
    else:
        print(Fore.LIGHTRED_EX + "Invalid file path!")
    time.sleep(2)

def interactive_menu():
    while True:
        clear_console()
        print(Fore.RED + "Main Menu".center(shutil.get_terminal_size().columns, "-"))
        print(Fore.LIGHTRED_EX + "[1] Start Account Activator")
        print(Fore.LIGHTRED_EX + "[2] Change CSV location")
        print(Fore.LIGHTRED_EX + "[3] Exit")
        choice = input(Fore.RED + "Choose an option: ")
        if choice == "1":
            clear_console()
            activate_accounts_from_csv(csv_file_path)
            input(Fore.LIGHTRED_EX + "\nActivation complete. Press Enter to return to the menu...")
        elif choice == "2":
            change_endpoint()
        elif choice == "3":
            clear_console()
            print(Fore.RED + "Thanks for using my tool!".center(shutil.get_terminal_size().columns))
            time.sleep(2)
            exit()
        else:
            print(Fore.LIGHTRED_EX + "Invalid option!".center(shutil.get_terminal_size().columns))
            time.sleep(2)

display_ascii_art_with_animation()
interactive_menu()
