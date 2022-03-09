import autoexposure
import os
import random
import math
import getpass
from datetime import datetime
start_time = datetime.now()
test_length = 1


runFolder = "C:\\Users\\SpotAutomation\\PycharmProjects\\SpotSizeExposureTimeAuto\\"
dest_folder = "C:/Users/SpotAutomation/autoTest/"
file_name_temp = "test_file_"
flag = 1

random.seed(0)
for num in range(test_length):
    rdn = math.floor(1000*random.random())
    print("test ="+str(rdn)+" "+ dest_folder+" "+file_name_temp+" "+str(num)+" "+str(flag))
    os.system(runFolder+"autoexposure.py "+str(rdn)+" "+dest_folder+" "+file_name_temp+"_"+str(rdn)+" "+str(num)+" "+str(flag))
    #autoexposure.autoexposure(str(rdn), dest_folder, file_name_temp+"_"+str(rdn)+"_", num, 0 )#if rdn <= 500 else 1)
end_time = datetime.now()
print("end_time= "+str(end_time)+" start_time= "+str(start_time))
