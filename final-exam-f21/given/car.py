
class Car:

    def __init__(self, make_name, model_name, model_year=2019, color_name="White"):

        self.make  = make_name
        self.model = model_name
        self.year  = model_year
        self.color = color_name


    def __str__(self):
        return "{} {} {} ({})".format(self.year, self.make, self.model, self.color)
