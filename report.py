import pygsheets
import sys

def main(keyName, reportSheetName, trackingSheetName):
    # Create client
    client = pygsheets.authorize(service_account_file=keyName)

    print(client.spreadsheet_titles())

    reportSheet = client.open(reportSheetName)
    trackingSheet = client.open(trackingSheetName)


    try:
        finalRoster = reportSheet.add_worksheet("Final Roster")
        finalRoster.insert_rows(0, 1, ["Lifeguard Name:"], inherit=False)
        print("Please place final roster into Final Roster sheet")
        sys.exit(0)
    except:
        finalRoster = reportSheet.worksheet("title", "Final Roster")

    summaryWorksheet = trackingSheet.worksheet("title", "Summary")

    def _makeReport(finalRoster, summaryWorksheet, reportSheet):
        finalRosterCells = finalRoster.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
        summaryCells = summaryWorksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')

        finalRosterCells.pop(0)
        summaryCells.pop(0)
        
        #print(finalRosterCells)
        #print(summaryCells)

        summaryTable = {}
        finalRosterSummaryTable = {}

        for r in range(len(summaryCells)):
            summaryTable[summaryCells[r].pop(0)] = summaryCells[r]

        for r in range(len(finalRosterCells)):
            currLg = finalRosterCells[r][0]
            finalRosterSummaryTable[currLg] = [summaryTable[currLg][1], summaryTable[currLg][2]]
            try: 
                currLgReport = reportSheet.add_worksheet(currLg)
                currLgReport.insert_rows(0, 1, ["Number Challenges Completed:", "Number of Challenges"], inherit=False)
                currLgReport.insert_rows(1, 1, finalRosterSummaryTable[currLg], inherit=False)
            except:
                currLgReport = reportSheet.worksheet("title", currLg)
            currChart = currLgReport.add_chart(domain=None, ranges=[('A2', 'B2')], title=(currLg + " Challenge Report"))
            print(currChart.get_json())
            
        print(finalRosterSummaryTable)

    _makeReport(finalRoster, summaryWorksheet, reportSheet)

if __name__ == '__main__':
    main()
