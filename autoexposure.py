import pyautogui
import time
import sys
import getpass
from datetime import datetime

#sys.path.append(r'C:\Users\admin\PycharmProjects\SpotSizeExposureTimeAuto')
start_time = None
end_time = None
debbuger_switch = { "all": False, "picture pick": False, "general": False,"explicit": False,"explicit_time":False}
part_switch = {"exposure_time": [True, True], "play": [True, True]}

def autoexposure(exposure_time, dest_folder, file_name, num, flag):
    """
    function gets the parameters and using pyautogui module automates snap procedure
    :param exposure_time: int - exposure time in us
    :param dest_folder: string - save destination path
    :param file_name: string - file name
    :param  flag: 0 - all precess , 1 - ignore the exposure time
    :param num: int - additional element to file name for counting and indexing the output files
    :return: void
    """
    #print("flag = "+str(flag))
    pyautogui.PAUSE = 0.0008
    # local internal variables declaration
    wait_time = 0.6

    local_dir_path = "C:/Users/SpotAutomation/PycharmProjects/SpotSizeExposureTimeAuto/"
    # png frame recipe
    session_NITVision = [["exposure_time_4.png", "exposure_time_2.png"], #, "exposure_time_5.png", "exposure_time_6.png"
                         #["play.png", "play_1.png", "play_2.png"],
                         ["recording.png", "recording_1.png", "recording_2.png"],
                         #["raw.png", "raw_1.png", "raw_2.png"],
                         #["tifff.png", "tifff_1.png", "tifff_2.png"],
                         ["directory.png", "directory_1.png", "directory_2.png"],
                         ["name.png", "name_1.png", "name_2.png"],
                         ["initial_counter.png", "initial_counter_1.png", "initial_counter_2.png"],
                         ["snap.png", "snap_1.png", "snap_2.png"]]
    # checking if the num value is legal
    if int(exposure_time) >= 0:
        set_ = int(flag)


        # scanning samples of png object from recipe
        while set_ < len(session_NITVision):
            for pic in session_NITVision[set_]:
                # if debbuger_switch["all"] or debbuger_switch["general"]:
                #     print(">> pic= "+pic)
                # attempts to find coordinates
                try:
                    cord = pyautogui.locateOnScreen(pic)
                    #pyautogui.click()
                except OSError:
                    cord = pyautogui.locateOnScreen(local_dir_path+pic)
                    #pyautogui.click()
                if cord:
                    # if debbuger_switch["all"] or debbuger_switch["general"]:
                    #     print(">> cord= " + str(cord))
                    if "raw" in pic or "tifff" in pic:
                        break
                        # pay attention that if one of the identifiers are not checked there no procedure to engage those
                    pyautogui.moveTo(cord)

                    # special conditions that stands for special treatment
                    if "initial" in pic:
                        # if debbuger_switch["all"] or debbuger_switch["explicit"]:
                        #     print("initial")
                        pyautogui.move(0, 20)
                        #time.sleep(wait_time)
                        pyautogui.click()
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.press('del')
                        pyautogui.typewrite(str(num))
                        break
                    if "directory" in pic:
                        # if debbuger_switch["all"] or debbuger_switch["explicit"]:
                        #     print("directory")
                        pyautogui.move(0, 20)
                        pyautogui.click()
                        pyautogui.typewrite(str(dest_folder))
                        break
                    if "name" in pic:
                        # if debbuger_switch["all"] or debbuger_switch["explicit"]:
                        #     print("name")
                        pyautogui.move(0, 20)
                        #time.sleep(wait_time)
                        pyautogui.click()
                        pyautogui.typewrite(str(file_name))
                        break
                    if "time" in pic:
                        # if debbuger_switch["all"] or debbuger_switch["explicit"]:
                        #     print("time")
                        pyautogui.click()
                        # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                        #     print("click()")
                        pyautogui.move(0, 21+len(session_NITVision)-set_)
                       # print("move(0, 17)")
                        #time.sleep(wait_time+1)
                        pyautogui.click()
                        # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                        #     print("click()")
                        pyautogui.press('del')
                        # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                        #     print("press('del')")

                        pyautogui.typewrite(str(exposure_time))
                        # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                        #     print("typewrite(str({}))".format(str(exposure_time)))

                        idx = 0

                        mus_png = ["mus_1.png"] #, "mus_2.png", "mus_4.png"
                        while idx < len(mus_png):
                            try:
                                mus_cord = pyautogui.locateOnScreen(mus_png[idx])
                            except OSError:
                                mus_cord = pyautogui.locateOnScreen(local_dir_path+mus_png[idx])
                            if mus_cord:
                                # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                                #     print("ex time mus_cord detected")
                                pyautogui.moveTo(mus_cord)
                                pyautogui.click()
                                #time.sleep(wait_time)
                                pyautogui.press('u')
                                #time.sleep(wait_time+2)
                                pyautogui.press('enter')
                                #time.sleep(wait_time)
                                pyautogui.press('enter')


                            else:
                                # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                                #     print("ex time mus_cord not detected -> manual")

                                #print("cord exception")C:/Users/SpotAutomation/autoTest/
                                pyautogui.move(120+3*idx, 13)
                                # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                                #     print("move(120+{}, 13)".format(str(3*idx)))
                                #time.sleep(wait_time)
                                pyautogui.click()
                                # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                                #     print("click()")
                                #time.sleep(wait_time)
                                pyautogui.press('u')
                                # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                                #     print("press('u')")
                                #time.sleep(wait_time)
                                pyautogui.press('enter')
                                # if debbuger_switch["all"] or debbuger_switch["explicit_time"]:
                                #     print("press('enter'")
                            pyautogui.press('enter')
                            idx += 1

                    else:
                        #time.sleep(wait_time)
                        pyautogui.click()
                        pyautogui.press('enter')
                        break
                    #pyautogui.press('enter')
                # condition when coordinates of exposure time label not found
                if not cord and "time" in pic:
                    cam_control = ["camera_control_off.png",  "camera_control_off_2.png"]
                    for atm in cam_control:
                        try:
                            cord_n = pyautogui.locateOnScreen(atm)
                        except OSError:
                            cord_n = pyautogui.locateOnScreen(local_dir_path+atm)
                        if cord_n:
                            pyautogui.moveTo(cord_n)
                            #time.sleep(wait_time)
                            pyautogui.click()
                            set_ = set_ - 1
                            break

                

            set_ += 1


# execution pre process
if __name__ == "__main__":

    exposure_time = sys.argv[1]
    dest_folder = sys.argv[2]
    file_name = sys.argv[3]
    num = sys.argv[4]
    flag_number = sys.argv[5]
    autoexposure(str(exposure_time), str(dest_folder), str(file_name), num, int(flag_number))

