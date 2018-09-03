# encoding utf-8
from multiprocessing import Process
from proxypool.testflask import app
from proxypool.Getter import Getter
from proxypool.Tester import Tester
import time


TESTER_CYCLE = 20
GETTER_CYCLE = 1
TESTER_ENABLED = True
GETTER_ENABLED = False
API_ENABLED = False
API_HOST = 'localhost'
API_PORT = '8888'


# 进程管理类
class Scheduler:
    def schedule_tester(self, cycle=TESTER_CYCLE):
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        getter = Getter()
        while True:
            print('获取器开始运行')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()


if __name__ == '__main__':
    s = Scheduler()
    s.run()