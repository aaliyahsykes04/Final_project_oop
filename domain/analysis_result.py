# this class holds the results after the math is done 

class AnaysisResult: 
    def __init__(self, metric_name, value, grouped_data, conclusion):
        # metric_name - what was measures (average rush attempt per win )
        # value - the actual number computed 
        # grouped_data - a dictionary grouping results by team
        # conclusion - sentence about what we found 

        self.metric_name = metric_name
        self.value = value
        self.grouped_data = grouped_data
        self.conclusion - conclusion

    def __repr__(self):
        # prints a summary of the results 
        return( 
            f"Metric: {self.metric_name}\n"
            f"Overall Values: {self.value}\n"
            f"Conclusion: {self.conclusion}"
        )