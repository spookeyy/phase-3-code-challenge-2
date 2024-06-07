class Band:
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception
        if len(value) == 0:
            raise Exception
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if isinstance(self._hometown, str):
            raise AttributeError(
                "Band.hometown is immutable. "
                "If you want to change the hometown, "
                "change the name instead."
            )
        self._hometown = value
    def concerts(self):
        pass

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def concerts(self):
        pass

    def bands(self):
        pass
