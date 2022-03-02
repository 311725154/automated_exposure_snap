import pywinauto
import pyautogui
from subprocess import Popen
from pywinauto import Desktop
from pywinauto import application
#import lackey
import time

class Robot:

    def __init__(self, exposure_time, dest_folder, file_name,session):

        self.wait_time = 1
        self.session_NITVision = [["icon.png", "icon_1.png", "icon_2.png", "icon_3.png"],
                                  ["camera_link.png", "camera_link_1.png", "camera_link_2.png"],
                                  ["ok_btn.png", "ok_btn_1.png", "ok_btn_2.png"],
                                  ["CL_CAM_LNK.png", "CL_CAM_LNK_1.png", "CL_CAM_LNK_2.png"],
                                  ["ok_btn.png", "ok_btn_1.png", "ok_btn_2.png"],
                                  ["exp_time_a.png", "ex_time_b.png", "ex_time_c.png", "ex_time_e.png", "exposure_time.png", "exposure_time_1.png", "exposure_time_2.png"],
                                  ["play.png", "play_1.png", "play_2.png"],
                                  ["recording.png", "recording_1.png", "recording_2.png"],
                                  ["raw.png", "raw_1.png", "raw_2.png"],
                                  ["tifff.png", "tifff_1.png", "tifff_2.png"],
                                  ["directory.png", "directory_1.png", "directory_2.png"],
                                  ["name.png", "name_1.png", "name_2.png"],
                                  ["snap.png", "snap_1.png", "snap_2.png"]]

        if session == 'NITVision':

            pyautogui.hotkey('win', 'd')
            time.sleep(self.wait_time)
            pyautogui.click()
            set_ = 0

            while set_ < len(self.session_NITVision):
                for pic in self.session_NITVision[set_]:
                    cord = pyautogui.locateOnScreen(pic)
                    if cord:
                        if "raw" in pic or "tifff" in pic:
                            break
                            # pay attention that if one of the identifiers are not checked there no procedure to engage those
                        pyautogui.moveTo(cord)
                        if "time" in pic or "directory" in pic or "name" in pic:
                            pyautogui.move(0, 10 if "time" in pic else 20)
                            time.sleep(self.wait_time)
                            pyautogui.click()
                            pyautogui.typewrite(str(exposure_time) if "time" in pic else (str(dest_folder) if "directory" in pic else str(file_name)))
                            if "time" in pic:
                                pyautogui.move(100, 10)
                                time.sleep(self.wait_time)
                                pyautogui.click()
                                time.sleep(self.wait_time)
                                pyautogui.press('u')
                                time.sleep(self.wait_time)
                            pyautogui.press('enter')
                            break
                        else:
                            time.sleep(self.wait_time)
                            pyautogui.click(clicks=2 if "icon" in pic else 1)
                            time.sleep(self.wait_time)
                            break
                    if not cord and "CL_CAM_LNK" in pic:
                        n_dev = ["no_device.png", "no_device_1.png", "no_device_2.png"]
                        for atm in n_dev:
                            cord_n = pyautogui.locateOnScreen(atm)
                            if cord_n:
                                rty_b = ["retry_btn.png", "retry_btn_1.png", "retry_btn_2.png"]
                                for atm_ in rty_b:
                                    cord_n = pyautogui.locateOnScreen(atm_)
                                    if cord_n:
                                        pyautogui.moveTo(cord_n)
                                        pyautogui.click()
                                        set_= set_-1
                                        time.sleep(self.wait_time)
                                        break
                    if not cord and "time" in pic:
                        cam_control = ["camera_control_off.png", "camera_control_off_1.png", "camera_control_off_2.png"]
                        for atm in cam_control:
                            cord_n = pyautogui.locateOnScreen(atm)
                            if cord_n:
                                pyautogui.moveTo(cord_n)
                                time.sleep(self.wait_time)
                                pyautogui.click()
                                set_ = set_ - 1
                                break

                    else:
                        assert "image detection failure"

                set_ += 1


class AutoMeasure:
    def __init__(self, exposure_time, dest_folder, file_name, num):

        self.wait_time = 1
        self.session_NITVision = [["exp_time_a.png", "ex_time_b.png", "ex_time_c.png", "ex_time_e.png",
                                   "exposure_time.png", "exposure_time_1.png", "exposure_time_2.png", "exposure_time_4.png", "exposure_time_5.png", "exposure_time_6.png"],
                                  ["play.png", "play_1.png", "play_2.png"],
                                  ["recording.png", "recording_1.png", "recording_2.png"],
                                  ["raw.png", "raw_1.png", "raw_2.png"],
                                  ["tifff.png", "tifff_1.png", "tifff_2.png"],
                                  ["directory.png", "directory_1.png", "directory_2.png"],
                                  ["name.png", "name_1.png", "name_2.png"],
                                  ["initial_counter.png", "initial_counter_1.png", "initial_counter_2.png"],
                                  ["snap.png", "snap_1.png", "snap_2.png"]]
        if num >= 0:
            set_ = 0

            while set_ < len(self.session_NITVision):
                for pic in self.session_NITVision[set_]:
                    cord = pyautogui.locateOnScreen(pic)
                    if cord:
                        if "raw" in pic or "tifff" in pic:
                            break
                            # pay attention that if one of the identifiers are not checked there no procedure to engage those
                        pyautogui.moveTo(cord)

                        if "initial" in pic:
                            pyautogui.move(0, 15)
                            time.sleep(self.wait_time)
                            pyautogui.click()
                            pyautogui.hotkey('ctrl', 'a')
                            pyautogui.press('del')
                            pyautogui.typewrite(str(num))
                            break
                        if "directory" in pic:
                            pyautogui.move(0, 15)
                            time.sleep(self.wait_time)
                            pyautogui.click()
                            pyautogui.typewrite(str(dest_folder))
                            break
                        if "name" in pic:
                            pyautogui.move(0, 15)
                            time.sleep(self.wait_time)
                            pyautogui.click()
                            pyautogui.typewrite(str(file_name))
                            break
                        if "time" in pic:
                            act_cord = pyautogui.locateOnScreen("real_fps.png")
                            spacer = 0
                            while act_cord:
                                act_cord = pyautogui.locateOnScreen("real_fps.png")
                                if act_cord:
                                    spacer+=1
                                    pyautogui.move(0, 2)
                                    time.sleep(self.wait_time)
                                    pyautogui.click()
                                    pyautogui.typewrite(str(exposure_time))

                            mus_cord = pyautogui.locateOnScreen("mus.png")
                            if mus_cord:
                                pyautogui.moveTo(mus_cord)
                            else:
                                pyautogui.move(111, 0)
                            time.sleep(self.wait_time)
                            pyautogui.click()
                            time.sleep(self.wait_time)
                            pyautogui.press('u')
                            time.sleep(self.wait_time)
                            pyautogui.press('enter')
                            pyautogui.press('enter')
                            break
                        else:
                            time.sleep(self.wait_time)
                            pyautogui.click()
                            time.sleep(self.wait_time)
                            break

                    if not cord and "time" in pic:
                        print("cam_control acheved")
                        cam_control = ["camera_control_off.png", "camera_control_off_1.png", "camera_control_off_2.png"]
                        for atm in cam_control:
                            cord_n = pyautogui.locateOnScreen(atm)
                            if cord_n:
                                pyautogui.moveTo(cord_n)
                                time.sleep(self.wait_time)
                                pyautogui.click()
                                set_ = set_ - 1
                                break
                    if not cord and "play" in pic:
                        break

                    else:
                        assert "image detection failure"

                set_ += 1

class AutoSnap:

    def __init__(self):
        self.wait_time = 1
        self.session_NITVision = [
                                  ["recording.png", "recording_1.png", "recording_2.png"],
                                  ["snap.png", "snap_1.png", "snap_2.png"]]

        set_ = 0

        flag = True
        while set_ <len(self.session_NITVision) and flag:
            for pic in self.session_NITVision[set_]:
                cord = pyautogui.locateOnScreen(pic)
                if cord:
                    pyautogui.moveTo(cord)
                    pyautogui.click()

                    flag = False if "snap" in pic else True



