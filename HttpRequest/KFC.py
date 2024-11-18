class KfcError(BaseException):
    """KFC Crazy Thursday,no more work!!"""
    pass


if __name__ == '__main__':
    try:
        raise KfcError("Ops,unknown error in your code,v me 50 let me see see and try some help,deadline at KFC Crazy Thursday")
    except KfcError as e:
        raise KfcError