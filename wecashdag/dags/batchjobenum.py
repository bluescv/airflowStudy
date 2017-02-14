import datetime
from enum import Enum

class BatchJobEnum(Enum):
    JinShangMeltStatusCancel = 1


if __name__ == '__main__':

    try:
        print(BatchJobEnum.JinShangMeltStatusCancel.value)
        taskid =  datetime.timedelta().strftime('%Y%m%d')
        print(taskid)

    except KeyboardInterrupt:
        print("exception")

    pass
