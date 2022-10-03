# RecWellChallengeTracker
Instructions:
* To use code please download latest version of Python (https://www.python.org/downloads/) and pygsheets.
  * To download pygsheets, open command prompt by searching up cmd or pressing "Windows"+"R" keys and typing cmd. If on Mac open terminal.
  * If on Windows, paste "py -m ensurepip --upgrade" into command prompt, then paste "pip install pygsheets" as well. If on Mac "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py" and, then "python3 get-pip.py". Do not include quation marks.
  * Will require you to download Google API's private key for Google Sheets. Make sure you are using the purdueheadguard@gmail.com for the following. Please follow the instructions bellow. 
  * If creating a new Google Sheet, please add lifeguard-challenges@challenge-tracking-python.iam.gserviceaccount.com as an editor to the Google Sheet planning to use.
  * Go to https://console.cloud.google.com  
  * Click on the project "Challenge-Tracking-Python".
  * Go to the project settings, within the "Dashboard" tab, under "Project Info".
  * From there, go to "Service accounts" on the left dropdown menu.
  * Click the email that starts with lifeguard-challenges.
  * Click the "Keys" tab.
  * Then, click on "Add Key", and "Create new key".
  * Select JSON format and create. The private key will be added to your computer.
  * Add the key into the folder containing all of the .py files. Make sure all the files and the key are in the same folder. 
  * Please paste the key file name into the autherization parts on code, in summary.py (line 37) and tracking.py (line 9). The format should be "PRIVATEKEYNAME.json". 
  * Finally make sure the correct sheet title is in place in summary.py (line 43) and tracking.py (line 17). If the name is different, change it to the name of the sheet to be used (ex. if the name of the sheet is Master Challenges Sheet, put Master Challenges Sheet between the quotation marks.)
* Finally run main.py by pressing (F5) or using the run tab on IDLE.
