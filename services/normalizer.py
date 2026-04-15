# this class cleans the data before analyzing it 
# real data - messy values, wrong types, weird outlirs


class Normalizer : 
    def __init__(self, records):
        #records - full list of record objects from the repository 
        self.records = records 

    def clean (self): 
        # I will filter out any bad records and return a clean list 
        cleaned = []

        for record in self.records:
            #skip records where rush_attempts is missing or negative 
            if record.rush_attempts is None or record.rush_attempts < 0:
                continue

            #skip any record where the result is not W or L
            if record.result not in ("W","L"):
                continue


            # skip any record where team name is missing
            if not record.team:
                continue

            #if the record passed all check, keep it
            cleaned.append(record)

        print(f"Cleaned data: {len(cleaned)} valid records out of {len(self.records)} total.")
        return cleaned