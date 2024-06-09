class Band:
    def __init__(self, name, hometown):
        self._name = name
        if not isinstance(hometown, str):
            raise Exception("Hometown must be a string")
        self._hometown = hometown
        self._concerts = []

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
        raise Exception("The band's homet own is immutable. You can't change it.")


    # band has many concerts
    def concerts(self):
        return self._concerts

    def venues(self):
        venues = set()
        for concert in self._concerts:
            venues.add(concert.venue)
        return list(venues)

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        introductions = []
        for concert in self._concerts:
            introductions.append(concert.introduction())
        return introductions
class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        if len(value) == 0:
            raise Exception("Date cannot be empty")
        self._date = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise Exception("Venue must be of type Venue")
        self._venue = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise Exception("Band must be of type Band")
        self._band = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) == 0:
            raise Exception("Name cannot be empty")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise Exception("City must be a string")
        if len(value) == 0:
            raise Exception("City cannot be empty")
        self._city = value

    def concerts(self):
        concerts = []
        for concert in Concert.all:
            if concert.venue == self:
                concerts.append(concert)
        return concerts

    def bands(self):
        bands = set()
        for concert in self.concerts():
            bands.add(concert.band)
        return list(bands)
    


band = Band(name="boygenius", hometown="NYC")
venue = Venue(name="Theatre", city="NYC")
concert = band.play_in_venue(venue=venue, date="Nov 22")
print(concert.introduction())