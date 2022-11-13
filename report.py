import pygsheets
import sys
import inspect

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
            currLg = finalRosterCells[r][0].lower().title()

            try:
                finalRosterSummaryTable[currLg] = [summaryTable[currLg][1], int(summaryTable[currLg][2]) - int(summaryTable[currLg][1])]
                try: 
                    currLgReport = reportSheet.add_worksheet(currLg)
                    # currLgReport.insert_rows(0, 1, ["Number Challenges Completed:", "Number of Challenges Not Completed"], inherit=False)
                    # currLgReport.insert_rows(1, 1, finalRosterSummaryTable[currLg], inherit=False)
                    # currChart = currLgReport.add_chart(domain=None, ranges=[('A2', 'B2')], title=(currLg + " Challenge Report"))
                except:
                    currLgReport = reportSheet.worksheet("title", currLg)
                    currLgReport.clear(fields="*")

                currLgReport.insert_rows(0, 1, ["Challenges Completed:", "Challenges Not Completed"], inherit=False)
                currLgReport.insert_rows(1, 1, finalRosterSummaryTable[currLg], inherit=False)
            except:
                print("Error: " + currLg)
            # This code only adds the necessary data. Need to run creatPieChart function inside Google Sheets.

            #currChart = currLgReport.add_chart(domain=None, ranges=[('A2', 'B2')], title=(currLg + " Challenge Report"))
            #print(inspect.getargspec(currChart.chart_type).args) # Dont know how to convert from column chart to pie chart
            

        print(finalRosterSummaryTable)

    _makeReport(finalRoster, summaryWorksheet, reportSheet)

if __name__ == '__main__':
    main()
