import psutil
import json

psutil.cpu_times()


class ProcessStats(object):

    def __init__(self):
        super(ProcessStats, self).__init__()
        #self.arg = arg

    def getStats(self):
        pids = psutil.pids()
        infoS = {}
        for pid in pids:
            p = psutil.Process(pid)
            try:
                if pid in (0, 4) or not p.name():
                    continue
                infoS[pid] = {"processName": p.name(), "processStatus": p.status(),
                              "CPU": p.cpu_percent(), "memoryPercent": p.memory_percent(), "numberOfThreads": p.num_threads()}
            except psutil.AccessDenied:
                pass
        return infoS

if __name__ == '__main__':

    printer = ProcessStats()
    print json.dumps(printer.getStats(), indent=4)
