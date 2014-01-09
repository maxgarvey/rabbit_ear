#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='sound_queue', durable=True)

message = " ".join(sys.argv[1:])
channel.basic_publish(exchange='', routing_key='sound_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2))

print("sent: {0}".format(message))

connection.close()