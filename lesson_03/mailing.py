from address import address


class Mailing:
    to_address: address
    from_address: address
    cost: int
    track: str

    def __init__(self, to_address, from_address, track, cost):
        self.to_address = to_address
        self.from_address = from_address
        self.track = track
        self.cost = cost
