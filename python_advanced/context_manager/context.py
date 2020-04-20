class Context(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Open!')
        print('hello: ' + self.name)
        print('goodbye: ' + self.name)


    def __exit__(self, exc_type, exc_value, traceback):
        print('Close!')


