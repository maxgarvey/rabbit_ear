#!/usr/bin/env python
import pika
import time
import subprocess

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='sound_queue', durable=True)
print 'exit [ctrl]-C'

def callback(ch, method, properties, body):
    print("received: {0}".format(body))
    subprocess.call(["ffplay", "-nodisp", "-autoexit", body])
    print "done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='sound_queue')

channel.start_consuming()