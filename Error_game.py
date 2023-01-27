class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooBigError(Error):
    pass

number = int(input('write number: '))

while True:
    try:
        unumber = int(input('write real number: '))

        if unumber < number:
            raise ValueTooSmallError
        elif unumber > number:
            raise ValueTooBigError
        break
    
    except ValueTooSmallError:
        print('its Small.try again')
        
    except ValueTooBigError:
        print('its Big.try again')
        
print('congratulation')