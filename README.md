# 🚀 Scratchtivator 🎨  

This Python script automates the activation of Scratch student accounts created via a CSV file. It streamlines the process by automating login and registration completion.  

## ✨ Features ✨  

✅ **Automates Scratch account activation** – Automatically logs in and completes the registration process.  
📂 **Reads account credentials from a CSV file** – Easily imports usernames and passwords from a CSV file.  
📊 **Displays a progress bar** – Shows activation progress with the last checked account.  
🎨 **Colorful and user-friendly console interface** – Features ASCII art and color-coded messages.  
⚙️ **Allows changing the CSV file location** – Easily switch between different CSV files.  
🛠️ **Handles Selenium exceptions** – Provides user-friendly error messages for common issues.  

---  

## 🔧 Installation 🔧  

1️⃣ **Clone the repository:**  

```bash  
git clone https://github.com/kyrazzx/scratchtivator/
cd scratchtivator 
```  

2️⃣ **Install dependencies:**  

```bash  
pip install selenium colorama  
```  

3️⃣ **Download ChromeDriver:**  

🔹 Download the appropriate ChromeDriver for your Chrome version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).  
🔹 Place the executable in a directory included in your system's **PATH**.  

---  

## 🚀 Usage 🚀  

1️⃣ **Prepare your CSV file:**  

📄 Create a file named **`ScratchAccountCSV.csv`** (or specify a different name).  
📌 Format each line as follows:  

```
username,password
```  

2️⃣ **Run the script:**  

```bash  
python main.py  
```  

3️⃣ **Follow the interactive menu:**  

🔹 **[1] Start Account Activator** – Begin the activation process.  
🔹 **[2] Change CSV location** – Modify the CSV file path.  
🔹 **[3] Exit** – Quit the program.  

---  

## ⚙️ Configuration ⚙️  

- The default CSV file path is **`ScratchAccountCSV.csv`**. You can change this via the interactive menu.  
- The script automatically handles common Selenium exceptions and displays user-friendly error messages.  

---  

## ⚠️ Important Notes ⚠️  

- Ensure **ChromeDriver** is compatible with your **Chrome version**.  
- The script assumes a specific HTML structure of the Scratch login and registration pages. Changes to Scratch's website might require updates to the script.  
- Use this script responsibly and ethically, respecting Scratch's terms of service.  

---  

## 🤝 Contribution 🤝  

Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.  

---  

## 📜 License 📜  

This project is licensed under the **MIT License**.  

---  

## 👩‍💻 Author 👨‍💻  

Made with ❤️ by **Kyra**  
