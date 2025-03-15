# Flask - creating API part 3

## About

This repository is my third homework assignment from the Python Pro course. 

My task was to create a POST requests to the database. Also i needed to add 'session' to the project. 

 - Added `POST` methods to all possible endpoints except for the **cart**, which only supports `GET`. 
 - Added session to the start_page() function in view.py file.
 - Updated db_methods.py, added class SQLiteDB to the db_methods.py
 - Added static folder with images
 - Updated templates

## How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/OleksiiUzu/Third_Homework.git
   cd Third_Homework
2.(Optional) Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate

3.Install dependencies:
  pip install -r requirements.txt

4.Run the application:
  python app.py
