import boto3
import serial
import time

print('start to play baseball')
ser = serial.Serial('/dev/cu.usbmodemFA131', 9600)
time.sleep(3)
print('arduino is ready')
 
name = 'baseball'
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=name)
print('ready for subscribe')

while True:
    # subscribe messages
    msg_list = queue.receive_messages(MaxNumberOfMessages=1)
    if msg_list:
        for message in msg_list:
            print(message.body)
            if message.body == 'pitch':
                ser.write('1'.encode())
            elif message.body == 'magic':
                ser.write('2'.encode())
            elif message.body == 'swing':
                ser.write('3'.encode())
            elif message.body == 'reset':
                ser.write('0'.encode())
            message.delete()

    #if readchar.readchar() == 'q':
    #    print('bye')
    #    break

time.sleep(1)
ser.close()
