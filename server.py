import pika
import sys
import json
import ConfigParser
import io
from os import environ
from django.conf import settings
sys.path.append('C:\Users\Serban\Documents\cloudbase')
environ['DJANGO_SETTINGS_MODULE'] = 'statistics.settings'
sample_config = open('config.ini', 'r').read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': config.get("settingsConfigure", "ENGINE"),
            'NAME': config.get("settingsConfigure", "NAME"),
            'USER': config.get("settingsConfigure", "USER"),
            'PASSWORD': config.get("settingsConfigure", "PASSWORD"),
            'HOST': config.get("settingsConfigure", "HOST"),
            'PORT': config.get("settingsConfigure", "PORT"),
        }
    }
)


from statistics.models import PC, Statistic
PCobj = PC()
StatisticObj = Statistic()


class myServer(object):

    def __init__(self):
        super(myServer, self).__init__()

    def startServer(self):
        sample_config = open('config.ini', 'r').read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(sample_config))

        credentials = pika.PlainCredentials(config.get("credentials", "user"), config.get("credentials", "pass"))
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.get("serverconn", "host"), port=config.getint("serverconn", "port"),
                                                                       credentials=credentials))
        channel = connection.channel()

        channel.exchange_declare(exchange='logs',
                                 type='fanout')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='logs',
                           queue=queue_name)

        print ' [*] Waiting for logs. To exit press CTRL+C'

        channel.basic_consume(self.callback,
                              queue=queue_name,
                              no_ack=True)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        message = json.loads(body)
        pc = PC.objects.create(name=message['PC'])
        del message['PC']
        for pid in message:
            processInfo = message[pid]
            Statistic.objects.create(pid=pid, PC=pc, processName=processInfo["processName"], processStatus=processInfo["processStatus"],
                                     processPercent=processInfo["CPU"], numberOfThreads=processInfo["numberOfThreads"], memoryPercent=processInfo["memoryPercent"])
            print json.dumps(processInfo, indent=4)

myObject = myServer()
myObject.startServer()
