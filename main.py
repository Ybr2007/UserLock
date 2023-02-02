import UserLock


if __name__ == "__main__":
    # try to change PC Id
    pcId = UserLock.GetPcId()
    userlockCode = UserLock.UserLock(pcId + "AnyOtherKeys", len=18)
    print(pcId, userlockCode)
