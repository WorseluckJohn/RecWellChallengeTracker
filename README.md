# RecWellChallengeTracker
Instructions:
* To use code please download latest version of Python (https://www.python.org/downloads/) and pygsheets.
  * To download pygsheets, open command prompt by searching up cmd or pressing "Windows"+"R" keys and typing cmd. If on Mac open terminal.
  * If on Windows, paste "py -m ensurepip --upgrade" into command prompt. If on Mac "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py" and, then "python3 get-pip.py". Do not include quation marks. 
  * Then for both Windows and Mac, paste "pip install pygsheets". 
  * This code will require you to download Google API's private key for Google Sheets. Make sure you are using the purdueheadguard@gmail.com for the following. Please follow the instructions below.
  * If creating a new Google Sheet, please add lifeguard-challenges@challenge-tracking-python.iam.gserviceaccount.com as an editor to the Google Sheet that will be used.
  * Go to https://console.cloud.google.com  
  * Click on the project "Challenge-Tracking-Python".
  * Go to the project settings, within the "Dashboard" tab, under "Project Info".
  * From there, go to "Service accounts" on the left dropdown menu.
  * Click the email that starts with lifeguard-challenges.
  * Click the "Keys" tab.
  * Then, click on "Add Key", and "Create new key".
  * Select JSON format and create. The private key will be added to your computer.
  * Add the key into the folder containing all of the .py files. You can download the .py files by clicking on the green button "Code" at the top, and click download zip. Make sure all the files and the key are in the same folder; ideally, create a new folder and place the key and the .py files there.   
  * Open main_tracking.py to edit and paste the key file name into the autherization part in the main_tracking.py code, on line 5, after keyName = . So, you would copy the name of the file and paste it inside quotation marks. So it would look: keyName = "YOURPRIVATEKEY.json"
  * Similarly, on the next line (line 6), write the name of the master sheet using. So it would look like masterSheetName = "YOURSHEETNAME". If the name has blank spaces, include them.
  * If using main_report.py for the end of year charts, follow the previous two procedures on main_report.py.
* Finally run tracking_main.py by pressing (F5) or using the run tab on IDLE. Running it the first time will create the sheets needed to operate the code. Add the names of lifeguards to LifeguardList. The number of teams can be changed accordingly without changing anything in the code. Likewise, using the first time main_report.py will create a final roster sheet, where you will need to add the names of lifeguards. After adding the names, run the main function again.
* Please refer to the original master sheet as an example when needed. 
