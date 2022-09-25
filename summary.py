# Adjusted for pygsheets, made efficient as possible, runs in arround 2 seconds!!!
import pygsheets

def main():
    def makeSummarySheet(summaryTable, summarySheet, numCycles):
        summarySheet.clear(fields="*")
        count = 1

        summarySheet.insert_rows(0, 1, ["Lifeguard Name:","Team Number:","Number Challenges Completed:","Total Number of Challenges:"], inherit=False)
        
        matrix = []

        for keys in summaryTable.keys():
            matrix.append([keys, summaryTable[keys][0], summaryTable[keys][1], numCycles * 5])

            count = count + 1

        summarySheet.insert_rows(1, len(matrix), matrix, inherit=False) 
        count = 2

    def makeTeamSummarySheet(teamSummarySheet, teamTable):
        teamSummarySheet.clear(fields="*")

        count = 1

        teamSummarySheet.cell("A1").set_text_format("bold", True).value = "Team Number:"
        teamSummarySheet.cell("B1").set_text_format("bold", True).value = "Number Challenges Completed:"

        teamMatrix = []

        for keys in teamTable.keys():
            teamMatrix.append([keys, teamTable[keys]])

        teamSummarySheet.insert_rows(count, len(teamMatrix), teamMatrix, inherit=False) 

    ## Create client
    client = pygsheets.authorize(service_account_file="challenge-tracking-python-ca37993cfad5.json")

    ## Print the title of the sheet to confirm it opened
    print(client.spreadsheet_titles())

    #sheet = client.open("Python-Test")
    sheet = client.open("Master Challenges Sheet")

    passwordSheet = sheet.worksheet("title", "Passwords")
    listOfLifeguards = sheet.worksheet("title", "LifeguardList")
    summarySheet = sheet.worksheet("title", "Summary")
    teamSummarySheet = sheet.worksheet("title", "Team Summaries")

    Cycles = passwordSheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    numCycles = len(Cycles) - 1

    print("Number of cycles: " + str(numCycles))

    summaryTable = {}

    # TODO: ADD VALUES TO TEAM TABLE AS YOU GO
    teamTable = {'Team 1': 0, 'Team 2': 0, 'Team 3': 0, 'Team 4': 0, 'Team 5': 0, 'Team 6': 0, 'HGL': 0}

    cells = listOfLifeguards.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    lg_list_end_row = len(cells)

    # Initial table with lg name and team number
    try:
        for r in range(lg_list_end_row):
            currLifeguard = cells[r + 1][0].lower().title().strip()

            if not currLifeguard.isspace():
                summaryTable[currLifeguard] = [cells[r + 1][1], 0] # Initial value 0 for number of challenges done
    except:
        print("")

    print(summaryTable)

    for i in range(1, numCycles + 1):
        print(f"Cycle{i}")
        try:
            currCycleTrackingSheet = sheet.worksheet("title", f"Cycle{i} Tracking")
            cells = currCycleTrackingSheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')

            curr_cycle_end_row = len(cells)

            for r in range(curr_cycle_end_row): # cells[r] -> 0 = name, 1 = team num, 2 = challenges completed, 3 = num challenges complete, 4 = chal incomplete
                try:
                    currLg = str(cells[r + 1][0]).lower().title().strip()
                    currValue = int(cells[r + 1][3])
                    currTeam = summaryTable[currLg][0]
                    summaryTable[currLg][1] = summaryTable[currLg][1] + currValue
                    teamTable[currTeam] = teamTable[currTeam] + currValue
                except Exception as e:
                    print(e)
                    print("Spell error: " + currLg)
                    pass
        except:
            print("Current cycle doesn't have responses yet")


    print(summaryTable)
    print(teamTable)

    makeSummarySheet(summaryTable, summarySheet, numCycles)
    makeTeamSummarySheet(teamSummarySheet, teamTable)

if __name__ == '__main__':
    main()
