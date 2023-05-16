# CBSE Result Finder Bot

The CBSE Result Finder Bot is a Python script designed to automate the process of finding CBSE class XII results for students(both commerce and science stream). It uses web scraping techniques to search for results based on student information and generates screenshots for found results.

## Features

- Searches for CBSE class X and XII results using trial and error.
- Automates the process of entering roll number, school number, and admit card ID.
- Captures screenshots of found results.
- Provides feedback on the search status (found or not found).

## Prerequisites

Before running the CBSE Result Finder Bot, ensure that you have the following:

- Python 3 installed on your system
- Selenium library installed (`pip install selenium`)

## Usage

1. Clone the repository:

```
git clone https://github.com/Kamalkoranga/CBSE-Result-Finder.git
```

2. Go inside `CBSE-Result-Finder` folder.

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Make a folder with this name `class12_results` inside `CBSE-Result-Finder`

5. Run the script:

```
python bot.py
```

6. The script will automate the search process and provide feedback on the search status for each combination of roll_no and therir admit_card_id.

## Configuration

- `SCHOOL_NO`: School number for the search (It will be same for a particular school)
- `initial_point`: Set the value from which you want to start finding results

Feel free to modify these options according to your specific requirements.

## Limitations

- The script relies on web scraping techniques, which are subject to changes in the target website's structure. Ensure that the script is compatible with the current version of the CBSE result website.
- The script performs a high number of automated requests, so it's essential to use it responsibly and avoid excessive usage that may strain the server or violate usage policies.

## Disclaimer

This script is intended for educational and personal use only. The developers are not responsible for any misuse or violations of policies by using this script. Use it responsibly and ensure compliance with relevant regulations and policies.