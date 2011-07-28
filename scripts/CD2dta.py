__copyright__   = "Copyright 2011 SFCTA"
__license__     = ""
    



import dta
import countdracula
import datetime

        

if __name__ == '__main__':
    
    dta.setupLogging("dtaInfo.log", "dtaDebug.log", logToConsole=True)
    
    # The Geary network was created in an earlier Phase of work, so it already exists as
    # a Dynameq DTA network.  Initialize it from the Dynameq text files.
    gearyScenario = dta.DynameqScenario(startTime=datetime.time(hour=0),
                                        endTime=datetime.time(hour=1))
    gearyScenario.read(dir="C:\Documents and Settings\Varun\Desktop\GIT\dtaFILES", file_prefix="Base_Final")
    #gearyScenario.write(dir="C:\Documents and Settings\Varun\Desktop\GIT\dtaFILES\countsTest", file_prefix="geary")
    
    gearynetDta = dta.DynameqNetwork(scenario=gearyScenario)
    gearynetDta.read(dir="C:\Documents and Settings\Varun\Desktop\GIT\dtaFILES", file_prefix="Base_Final")
    #gearynetDta.write(dir="C:\Documents and Settings\Varun\Desktop\GIT\dtaFILES\countsTest", file_prefix="geary")
    #attach counts ?!
    starttime = datetime.time(00,00)
    period = datetime.timedelta(minutes = 15)
    
    number = 96
    tolerance = 5 #feet
    
    countDraculaReader = countdracula.ReadFromCD("172.30.1.120","countdracula", "cdreader", "ReadOnly")
    
    gearynetDta.retrieveCountListFromCountDracula(countDraculaReader, starttime, period, number, tolerance)
    
    
    gearynetDta.writeCountListToFile(dir="C:\Documents and Settings\Varun\Desktop\GIT\dtaFILES")
    
    
    