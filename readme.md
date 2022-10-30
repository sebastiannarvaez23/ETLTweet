### What is this program about?
This program simulates the behavior of an ETL, it makes the connection to a MySQL database and at the same time makes some consumptions to the tweeter APIs. A data feed job is carried out to later be displayed in a Dashboard built in Power BI.

## Before the execution
1. Execute the archive `api/db.sql` in a mysql shell or an a program sql development.

### Instructions for execute:
1. Create a virtual environment with the command `$ py -m venv vevn`
2. Activate the virtual environment with source:
For linux `$ venv/bin/activate`
For Windows `$ venv/Scripts/activate`.
3. Install the requiriments.txt dependencies with the `$ pip install -r requiriments.txt` command. This must be done taking into account that the virtual environment is turned on in the terminal where the aforementioned command is executed.
4. run command `python -m textblob.download_corpora`
5. Run the main.py file to run the program with the `$ python main.py` command

### End
