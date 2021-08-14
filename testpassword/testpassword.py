import pika, sys, os
import time
import string

found = False
calctTime = 0

def guessPassword(minLen, maxLen, password):
    charList = []
    charList = list(string.ascii_letters) + list(string.digits)
    global found
    global calcTime
    n = len(charList)
    startTime = time.time()
    for x in range(minLen, maxLen+1):
        guessPasswordHelper(charList, "", n, x, password)
        if found == True:
            break
    if found == True:
        print("password found!")
        executionTime = (calcTime - startTime)
        print('Execution time in seconds: ' + str(executionTime))
    else:
        print("password not found!")
    found = False
    calcTime = 0
 
# The main recursive method
def guessPasswordHelper(set, prefix, n, maxLen, password):
     
    # Base case: maxLen is 0,
    # print prefix
    if (maxLen == 0) :
        if password == prefix:
            global found
            global calcTime
            calcTime = time.time()
            found = True
        return
 
    for i in range(n):
 
        # Next character of input added
        newPrefix = prefix + set[i]
         
        # k is decreased, because
        # we have added a new character
        guessPasswordHelper(set, newPrefix, n, maxLen - 1, password)

def main():

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('127.0.0.1',
                                   5672,
                                   '/',
                                   credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='pyData')
    channel.queue_declare(queue='pyResult')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='pyData', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
 
