# меня не хватило на графику и красивости. Вот все что смог придумать
import time


class TrafficLight:
    __color = 0

    def running(self):
        while True:
            self.__color = 'RED'
            print("\r\033[41m\033[30m{}".format(self.__color), end="      ")
            time.sleep(7)
            self.__color = 'YELLOW'
            print("\r\033[43m\033[30m{}".format(self.__color), end="   ")
            time.sleep(2)
            self.__color = 'GREEN'
            text = self.__color
            print("\r\033[42m\033[30m{}".format(self.__color), end="    ")
            time.sleep(6)


col = TrafficLight()
col.running()
