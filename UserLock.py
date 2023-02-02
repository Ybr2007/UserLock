import uuid
import wmi
import hashlib


randSeed = 0

def SetSeed(seed: int) -> None:
    global randSeed
    randSeed = seed


def Rand() -> int:
    global randSeed
    randSeed = (randSeed * 2354 + 85094) & 0xffffffff
    return randSeed >> 16


def GetMac() -> str:
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return mac


def GetCpuId() -> str:
    cpuId = wmi.WMI().Win32_Processor()[0].ProcessorId.strip()
    return cpuId


def GetDiskId() -> str:
    diskId = wmi.WMI().Win32_DiskDrive()[0].SerialNumber.strip()
    return diskId


def GetmMainboardId() -> str:
    mainboardId = wmi.WMI().Win32_BaseBoard()[0].SerialNumber.strip()
    return mainboardId


def GetPcId() -> str:
    return hashlib.md5((GetMac() + GetCpuId() + GetDiskId() + GetmMainboardId()).encode('utf-8')).hexdigest()


def UserLock(key: str, len: int = 6) -> str:
    SetSeed(int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16))

    returnVlaue = ''

    for _ in range(len):
        r = Rand()
        returnVlaue += chr(r % 26 + ord('A'))

    return returnVlaue
