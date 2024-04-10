# Inventory Assistant with Web Interface

## Introduction
This is a simple inventory assistant implemented in Python using Pandas for data manipulation and Django frameworks for Web development. The system allows users to perform various operations such as adding, updating, searching, and printing inventory data.

## Requirements
- Python 3.x
- Dependencies (Install using `pip install -r requirements.txt`):
  - matplotlib
  - pandas
  - numpy

## Installation
1. **Clone the repository:**
   Clone this repository to your local machine
   ```bash
   git clone https://github.com/puttavivek/Project3
   cd inventory_project
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main application file:**
   ```bash
   Change directory to inventory_project
   run command "python manage.py runserver"
   wait till it opens a web page with the below buttons.
   ```

## User Input Details

### Add Inventory: 
When the user provides input, data validation happens and the input data is appended to the excel file.
- Part Name: String
- Part No: String
- Model: String
- Stock Location: Integer (Between 0 and 100)
- Quantity: Integer (Between 1 and 10000)

### Edit Inventory: 
This option is used to Update the quantity field based on the Part No and data validation happens as add inventory option.
- Part No: String
- Quantity: Integer (Between 1 and 10000)

### Search Inventory:
When this is selected, it prompts user to enter Part No, and it fetches the details from the excel sheet and display it on GUI window.
- Part No: String

### View Inventory:
When user selects this option, a new window is opened displaying all the excel data.

### Print Inventory:
When this option is selected user is prompted to select the folder location and entire excel data is saved as a pdf in that location.


### Follow the on-screen instructions to perform inventory management tasks.

## Features:
- Click on the inventory logo to go to homepage.
- Add new inventory items or update existing ones.
- Search for items based on part numbers.
- View the entire inventory list.
- Print the inventory data to a PDF file.
- Bulk entry of inventory data from a file.

### Project Report and Video Presentation:
For Project Report and a video presentation, visit the https://youtu.be/lF9V7HtzpcQ
