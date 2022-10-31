import summary
import tracking

if __name__ == '__main__':
    keyName = "challenge-tracking-python-ca37993cfad5.json"
    masterSheetName = "Master Challenges Sheet Original"
    
    tracking.main(keyName, masterSheetName)
    summary.main(keyName, masterSheetName)
