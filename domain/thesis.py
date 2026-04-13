# this class holds my thesis and the variables i am testing 


class Thesis:
    def __init__(self, statement, independent_var, dependent_var, filter_note):
        # statement - the full sentence of my thesis 
        # independent_var - the thing i am measuring (rush_attempts)
        # dependent_var -  the outcome i'm watching (win or loss)
        #filter_note - limits on the data ( i want regular season)

        self.statement = statement
        self.independent_var = independent_var
        self.dependent_var = dependent_var
        self.filter_note = filter_note

    def __repr__(self):
        # This prints a clean summary of your thesis when you need to see it
        return (
            f"Thesis: {self.statement}\n"
            f"  Testing: {self.independent_var} vs {self.dependent_var}\n"
            f"  Filter: {self.filter_note}"
        )