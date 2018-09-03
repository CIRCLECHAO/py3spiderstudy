import time
from multiprocessing import Process
from cookiespool.show import app
from cookiespool.Genetator import *


class Scheduler(object):
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print('cookies检测进程开始')
            try:
                for website, cls in TESTER_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    # print(tester)
                    tester.run()
                    print('cookies检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)
                break

    @staticmethod
    def generate_cookie(cycle=CYCLE):
        while True:
            print('cookies生成开始')
            # try:
            for website, cls in GENERATOR_MAP.items():
                print(website)
                generator = eval(cls + '(website= "' + website + '")')
                generator.run()
                print('cookies生成完成')
                generator.close()
                time.sleep(cycle)
            # except Exception as e:
            #     print(e.args)
            #     break

    @staticmethod
    def api():
        print("api接口开始运行")
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        if API_PROCESS:
            api_process = Process(target=Scheduler.api())
            api_process.run()

        if GENERATOR_PROCESS:
            gene_process = Process(target=Scheduler.generate_cookie())
            gene_process.run()

        if VALID_PROCESS:
            va_process = Process(target=Scheduler.valid_cookie())
            va_process.run()


if __name__ == "__main__":
    s = Scheduler()
    s.run()