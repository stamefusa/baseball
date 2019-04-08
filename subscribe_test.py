import boto3
 
name = 'baseball'
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=name)
while True:
    # メッセージを取得
    msg_list = queue.receive_messages(MaxNumberOfMessages=10)
    if msg_list:
        for message in msg_list:
            print(message.body)
            message.delete()
