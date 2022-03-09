import pyautogui
import time
import sys


def autosnap(rep):
    """
    perform auto snap o running state via pyautogui module
    :param rep: int - the number of repetitions needed for execution
    :return: void
    """
    # local variables declaration
    wait_time = 0.1
    local_dir_path = "C:/Users/admin/PycharmProjects/SpotSizeExposureTimeAuto/"
    # png recipe
    session_NITVision = [
        ["recording.png", "recording_1.png", "recording_2.png","recording_on.png"],
        ["snap.png", "snap_1.png", "snap_2.png"]]

    # counter and trigger initializing
    set_ = 0
    flag = True
    repeat = int(rep)
    # no actual scan required although the scan algorithm initially finds the recording tab
    while set_ < len(session_NITVision) and flag:
        for pic in session_NITVision[set_]:
            try:
                cord = pyautogui.locateOnScreen(pic)
            except OSError:
                cord = pyautogui.locateOnScreen(local_dir_path+pic)
            if cord:
                pyautogui.moveTo(cord)
                # condition when snap button found
                if "snap" in pic:
                    # repeats clicks on snap
                    for count in range(repeat):
                        pyautogui.click()
                        #time.sleep(wait_time)
                else:
                    pyautogui.click()
                # snap execution triggered
                flag = False if "snap" in pic else True
        set_ += 1

# execution pre process
if __name__ == "__main__":
    rep = sys.argv[1]
    autosnap(rep)