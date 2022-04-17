started = False
while True:
    instuction = input('> ')
    if instuction.lower() == 'help':
        help = '''
            start - to start the car
            stop - to stop the car
            exit - to exit
        '''
        print(help)
    elif instuction.lower() == 'start':
        if started == False:
            print('Car started.. Ready to go!')
        else: 
            print('Car already started')
        started = True
    elif instuction.lower() == 'stop':
        if not started:
            print('Car already stopped!')
        else:
            print('Car stopped.')
        started = False
    elif instuction.lower() == 'exit':
        break
    else: 
        print("I don't understand that..")