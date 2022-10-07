import summary
import tracking

if __name__ == '__main__':
    keyName = "YOURKEYFILENAME.json"
    masterSheetName = "Master Challenges Sheet Original"
    
    tracking.main(keyName, masterSheetName)
    summary.main(keyName, masterSheetName)
