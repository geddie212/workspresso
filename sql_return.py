import main

class SQLReturn:

    def __init__(self):
        self.db_all = main.Cafe.query.all()

    def all_locations(self):
        locations = []
        for loc in self.db_all:
            if loc.location not in locations:
                locations.append(loc.location)
        return locations