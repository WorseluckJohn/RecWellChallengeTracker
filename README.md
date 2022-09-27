# RecWellChallengeTracker
Instructions:
* To use code please download latest version of Python (https://www.python.org/downloads/) and pygsheets.
  * To download pygsheets, open command prompt by searching up cmd or pressing <Windows><R> keys and typing cmd. 
  * Then, paste "py -m ensurepip --upgrade" into command prompt. If on Mac "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py" and, then "python3 get-pip.py".
  * Afterwards, paste "pip install pygsheets" as well. 
* Will require you to download Google API's private key for Google Sheets. If you are creating a new account, follow the link https://www.geeksforgeeks.org/how-to-automate-google-sheets-with-python/. If you are using purdueheadguard@gmail.com, please follow the instructions bellow. 
  * If creating a new Google Sheet, please add lifeguard-challenges@challenge-tracking-python.iam.gserviceaccount.com as an editor to the sheet.
  * Click on the project "Challenge-Tracking-Python".
  * Go to the project settings, within the "Dashboard" tab, under "Project Info".
  * From there, go to "Service accounts" on the left dropdown menu.
  * Click the email that starts with lifeguard-challenges.
  * Click the "Keys" tab.
  * Then, click on "Add Key", and "Create new key".
  * Select JSON format and create. The private key will be added to your computer.
  * Add the key into the folder containing all of the .py files. 
  * Please paste the key file name into the autherization parts on code, in summary.py (line 37) and tracking.py (line 9). The format should be "PRIVATEKEYNAME.json". 
* Finally run main.py by pressing (F5) or using the run tab on IDLE.
