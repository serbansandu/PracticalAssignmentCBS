import pika
import getProcess
import json
import ConfigParser
import io
import time
import platform

processObj = getProcess.ProcessStats()
message = processObj.getStats()
message['PC'] = platform.node()
message = json.dumps(message)


class Stats(object):

    def __init__(self):
        super(Stats, self).__init__()

    def sendMessage(self):
        sample_config = open('config.ini', 'r').read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(sample_config))

        credentials = pika.PlainCredentials(config.get("credentials", "user"), config.get("credentials", "pass"))
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.get("connection", "host"), port=config.getint("connection", "port"),
                                                                       credentials=credentials))

        channel = connection.channel()

        channel.exchange_declare(exchange='logs',
                                 type='fanout')

        channel.basic_publish(exchange='logs',
                              routing_key='',
                              body=message)
        # print " [x] Sent %r" % (message)
        connection.close()

sender = Stats()
# while True:
sender.sendMessage()
#     time.sleep(2)
