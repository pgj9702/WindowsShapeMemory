import screeninfo
import wx
import os
from time import sleep
import ctypes


class ScreenControl:
    do_detect_monitors: bool = False
    do_detect_window_lock: bool = False

    def detect_monitor_count(self):

        while self.do_detect_monitors or self.do_detect_window_lock :
            pass


if __name__ == '__main__':
    for m in screeninfo.get_monitors():
        print(type(m), m)

    wx1 = wx.App()

    print(wx.Display.GetCount())
    # os.getenv

    # ctypes.windll.user32.LockWorkStation()
    ctypes.windll.user32.state()


"""
$lockAppProcess = Get-Process LockApp

for($i = 0; $i -lt 60; $i++)
{
    $process = [System.Diagnostics.Process]::GetProcessById($lockAppProcess.Id)

    $threads = $process.Threads

    if($threads[0].WaitReason -eq "Suspended")
    {
        "윈도우즈 잠금 해제"
    }
    else
    {
        "윈도우즈 잠금"
    }

    Sleep 1
}

GetRemoteLogonStatus 'localhost'

GetRemoteLogonStatus '127.0.0.1'

function GetRemoteLogonStatus($computer = 'localhost')
{
    if(Test-Connection $computer -Count 2 -Quiet)
    {
        try
        {
            $user = $null

            $user = Get-WmiObject -Class win32_computersystem -ComputerName $computer | select -ExpandProperty username -ErrorAction Stop
        }
        catch
        {
            "Not logged on";

            return
        }

        try
        {
            if((Get-Process logonui -ComputerName $computer -ErrorAction Stop) -and ($user))
            {
                "Workstation locked by $user"
            }
        }
        catch
        {
            if($user)
            {
                "$user logged on"
            }
        }
    }
    else
    {
        "$computer Offline"
    }
}
"""