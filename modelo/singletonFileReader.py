class SingletonFileReader:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super(SingletonFileReader, cls).__new__(cls)
            cls._instance.filename = filename
        return cls._instance

    def read_lines(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        return lines