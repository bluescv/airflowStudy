from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


if __name__ == '__main__':

    try:
        print(Color.RED,Color.RED.name,Color.RED.value)

    except KeyboardInterrupt:
        print("exception")

    pass
