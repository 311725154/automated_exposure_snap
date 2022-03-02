import pyautogui
import time
import sys


def autoexposure(exposure_time, dest_folder, file_name, num):
    """
    function gets the parameters and using pyautogui module automates snap procedure
    :param exposure_time: int - exposure time in us
    :param dest_folder: string - save destination path
    :param file_name: string - file name
    :param num: int - additional elemen to file name for counting and indexing the output files
    :return: void
    """

    # local internal variables declaration
    wait_time = 1
    # png frame recipe
    session_NITVision = [["exp_time_a.png", "ex_time_b.png", "ex_time_c.png", "ex_time_e.png",
                          "exposure_time.png", "exposure_time_1.png", "exposure_time_2.png", "exposure_time_4.png",
                          "exposure_time_5.png", "exposure_time_6.png"],
                         ["play.png", "play_1.png", "play_2.png"],
                         ["recording.png", "recording_1.png", "recording_2.png"],
                         ["raw.png", "raw_1.png", "raw_2.png"],
                         ["tifff.png", "tifff_1.png", "tifff_2.png"],
                         ["directory.png", "directory_1.png", "directory_2.png"],
                         ["name.png", "name_1.png", "name_2.png"],
                         ["initial_counter.png", "initial_counter_1.png", "initial_counter_2.png"],
                         ["snap.png", "snap_1.png", "snap_2.png"]]
    # checking if the num value is legal
    if int(exposure_time) >= 0:
        set_ = 0

        # scanning samples of png object from recipe
        while set_ < len(session_NITVision):
            for pic in session_NITVision[set_]:
                # attempts to find coordinates
                cord = pyautogui.locateOnScreen(pic)
                if cord:
                    if "raw" in pic or "tifff" in pic:
                        break
                        # pay attention that if one of the identifiers are not checked there no procedure to engage those
                    pyautogui.moveTo(cord)

                    # special conditions that stands for special treatment
                    if "initial" in pic:
                        pyautogui.move(0, 15)
                        time.sleep(wait_time)
                        pyautogui.click()
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.press('del')
                        pyautogui.typewrite(str(num))
                        break
                    if "directory" in pic:
                        pyautogui.move(0, 15)
                        time.sleep(wait_time)
                        pyautogui.click()
                        pyautogui.typewrite(str(dest_folder))
                        break
                    if "name" in pic:
                        pyautogui.move(0, 15)
                        time.sleep(wait_time)
                        pyautogui.click()
                        pyautogui.typewrite(str(file_name))
                        break
                    if "time" in pic:
                        act_cord = pyautogui.locateOnScreen("real_fps.png")
                        spacer = 0
                        while act_cord:
                            act_cord = pyautogui.locateOnScreen("real_fps.png")
                            if act_cord:
                                spacer += 1
                                pyautogui.move(0, 2)
                                time.sleep(wait_time)
                                pyautogui.click()
                                pyautogui.typewrite(str(exposure_time))

                        mus_cord = pyautogui.locateOnScreen("mus.png")
                        if mus_cord:
                            pyautogui.moveTo(mus_cord)
                        else:
                            pyautogui.move(111, 0)
                        time.sleep(wait_time)
                        pyautogui.click()
                        time.sleep(wait_time)
                        pyautogui.press('u')
                        time.sleep(wait_time)
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        break
                    else:
                        time.sleep(wait_time)
                        pyautogui.click()
                        time.sleep(wait_time)
                        break
                # condition when coordinates of exposure time label not found
                if not cord and "time" in pic:
                    print("cam_control acheved")
                    cam_control = ["camera_control_off.png", "camera_control_off_1.png", "camera_control_off_2.png"]
                    for atm in cam_control:
                        cord_n = pyautogui.locateOnScreen(atm)
                        if cord_n:
                            pyautogui.moveTo(cord_n)
                            time.sleep(wait_time)
                            pyautogui.click()
                            set_ = set_ - 1
                            break
                if not cord and "play" in pic:
                    break

                else:
                    assert "image detection failure"

            set_ += 1


# execution pre process
if __name__ == "__main__":
    exposure_time = sys.argv[1]
    dest_folder = sys.argv[2]
    file_name = sys.argv[3]
    num = sys.argv[4]
    autoexposure(str(exposure_time), str(dest_folder), str(file_name), num)
