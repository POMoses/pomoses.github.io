from datetime import datetime, date

def qtrDetails():
    mthQtr = {1:1, 2:1, 3:1,
              4:2, 5:2, 6:2,
              7:3, 8:3, 9:3,
              10:4, 11:4, 12:4}
    qtrStartMth = {1:1, 2:4, 3:7, 4:10}
    qtrEndMth = {1:3, 2:6, 3:9, 4:12}
    qtrEndMthDay = {3:31, 6:30, 9:30, 12:31}

    inputDate = input('Enter entry/exit date (dd/mm/yyyy): ')
    try:
        entryExitDate = datetime.strptime(inputDate, '%d/%m/%Y').date()
    except ValueError:
        print('Enter a correct entry/exit date in the format dd/mm/yyyy')
        return qtrDetails()

    mm, yyyy = entryExitDate.month, entryExitDate.year
    entryExitQtr = mthQtr[mm]
    entryExitQtrStartDate = date(yyyy, qtrStartMth[entryExitQtr], 1)
    entryExitQtrEndDate = date(yyyy, qtrEndMth[entryExitQtr], qtrEndMthDay[qtrEndMth[entryExitQtr]])

    return (entryExitDate, entryExitQtr, entryExitQtrStartDate, entryExitQtrEndDate)
    

def svcChgAdj(case,annualSvcChg):
    caseMultiplier = {'entry':1, 'exit':-1}
    entryExitDate, qtr, qtrStartDate, qtrEndDate = qtrDetails()
    daysTillQE = (qtrEndDate - entryExitDate).days + 1
    daysInQtr = (qtrEndDate - qtrStartDate).days + 1
    residentSvcChgAdj = int(round(annualSvcChg * daysTillQE / daysInQtr / 1000, 0) * 1000)
    landlordSvcChgAdj = int(residentSvcChgAdj * 0.5)
    caseMsg = {'entry':f'Bill N{residentSvcChgAdj:,} to resident;\nRefund N{landlordSvcChgAdj:,} to landlord.',
               'exit':f'Refund N{residentSvcChgAdj:,} to resident;\nBill N{landlordSvcChgAdj:,} to landlord.'}
    print(caseMsg[case])
    
    
if __name__ == '__main__':
    print(svcChgAdj('entry', 250000))
    