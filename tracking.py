import pygsheets # need to import'
import datetime 
from collections import OrderedDict

def main():
    start = datetime.datetime.now()

    ## Create client
    client = pygsheets.authorize(service_account_file="challenge-tracking-python-ca37993cfad5.json")

    ## Print the title of the sheet to confirm it opened
    #print(client.spreadsheet_titles())
    print(client.spreadsheet_titles())

    ## Open spreadsheet by name/title
    #sheet = client.open("Python-Test")
    sheet = client.open("Master Challenges Sheet")

    def _makeTable(currResponsesWorksheet, trackingWorksheet, currPassword, listOfLifeguards): 
        challengeTable = {}

        cells = currResponsesWorksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
        end_row = len(cells)

        for lg in listOfLifeguards:
            currLg = lg[0].lower().title().strip()
            challengeTable[currLg] = [lg[1]]
        
        # Input: Column 1: lg name, 2: team num, 3: challenges completed, 6: password
        try:
            for r in range(end_row):
                # NEED TO KEEP PASSWORD COLLUMN CONSISTENT!
                if cells[r + 1][6].lower().replace(" ", "") == currPassword.lower(): 
                    # Can make this faster with getting entire matrix rather than checking cells one by one
                    currLifeguard = cells[r + 1][1].lower().title().strip()

                    if not currLifeguard.isspace():
                        currChallengesCompleted = cells[r + 1][3].split(',')
                        currChallengesCompleted = [x.strip(' ') for x in currChallengesCompleted]

                        try:
                            challengeTable[currLifeguard].extend(currChallengesCompleted)
                            challengeTable[currLifeguard] = list(OrderedDict.fromkeys(challengeTable[currLifeguard]))
                        except:
                            print(currLifeguard + " is not on lifeguard list")
        except:
            print("")
                    
            #print(currLifeguard)
            #print(currChallengesCompleted)

        #print(challengeTable)

        return challengeTable

    def _makeSheet(challengeTable, currAllChallenges, trackingWorksheet):
        # To update with new guards, just delete the A1 cell and it will recreate the form based on the updated lifeguard list
        trackingWorksheet.clear(fields="*")

        matrix = []

        # Output: Column 0: lg name, 1: team num, 2: challenges completed, 3: num completed, 4: challenges incomplete
        for keys in challengeTable.keys():
            currTeamNum = challengeTable[keys].pop(0)

            matrix.append([keys, currTeamNum, str(challengeTable[keys]), len(challengeTable[keys]), str(list(set(currAllChallenges) - set(challengeTable[keys])))])

        print(matrix)
        
        infoList = ["Lifeguard Name:",
                    "Team Number:",
                    "Challenges Completed:",
                    "Number of Challenges Completed:",
                    "Challenges Incomplete:", ]

        trackingWorksheet.insert_rows(0, 1, infoList, inherit=False) 

        trackingWorksheet.insert_rows(1, len(matrix), matrix, inherit=False) 

        trackingWorksheet.add_conditional_formatting("D2",f"D{len(matrix) + 1}", 'NUMBER_LESS', {'backgroundColor':{'red':1}}, '5')
        trackingWorksheet.add_conditional_formatting("D2",f"D{len(matrix) + 1}", 'NUMBER_GREATER', {'backgroundColor':{'red':1, 'green':1}}, '0')
        trackingWorksheet.add_conditional_formatting("D2",f"D{len(matrix) + 1}", 'NUMBER_EQ', {'backgroundColor':{'green':1}}, '5')

        #wks.add_conditional_formatting('A1', 'A4', 'NUMBER_BETWEEN', {'backgroundColor':{'red':1}}, ['1','5'])

    ## Open worksheet by name/title
    passwordSheet = sheet.worksheet("title", "Passwords")

    cycles = passwordSheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')

    numCycles = len(cycles) - 1
    print("Cycle number: " + str(numCycles))

    listOfLifeguards = sheet.worksheet("title", "LifeguardList").get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    listOfLifeguards.pop(0) 
    #print(listOfLifeguards)

    # Names of all challenges
    currAllChallenges = ['Physical', 'Recognition & Response', 'In-Water Skills', 'Social', 'CPR & First Aid']

    i = numCycles
    currPassword = str(passwordSheet.cell(f"B{i + 1}").value)
    print("Current password: " + currPassword)
    currResponsesWorksheet = sheet.worksheet("title", f"Cycle{i} Responses")
    trackingWorksheet = sheet.worksheet("title", f"Cycle{i} Tracking")

    currTable = _makeTable(currResponsesWorksheet, trackingWorksheet, currPassword, listOfLifeguards)
    _makeSheet(currTable, currAllChallenges, trackingWorksheet) 

    elapsed = datetime.datetime.now() - start
    print("\nTotal time in s: "+ str(round(elapsed.total_seconds(), 2))) # Full run took 1200 seconds!!! Only update takes around 600 s. 

if __name__ == '__main__':
    main()
