except ValueError:
        return 'not supported data'
    if x < 0 or y >= 0:
        return 'not supported data'
    else:
        return x ** y
