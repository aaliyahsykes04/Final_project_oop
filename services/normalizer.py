# this class cleans the data before analyzing it 
# real data - messy values, wrong types, weird outlirs


class Normalizer : 
    def __init__(self, records):
        #records - full list of record objects from the repository 
        self.records = records 

        def clean (sel f)