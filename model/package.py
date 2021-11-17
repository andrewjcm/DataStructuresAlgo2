class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, mass_kilo, notes):
        self.id: int = int(id)
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code
        self.deadline: str = deadline
        self.priority: bool = False if deadline == "EOD" else True
        self.mass_kilo: float = mass_kilo
        self.notes: str = notes
        self.status: str = "Delayed" if notes and ("Delayed" in notes or "Wrong" in notes) else "At hub"
        self.delayed: bool = True if self.status == "Delayed" else False
        self.truck_2_only: bool = True if self.notes and "truck 2" in self.notes else False
        self.time_delivered = None

    def __str__(self):
        return f"Package(id={self.id}," \
               f"address={self.address}," \
               f"deadline={self.deadline}," \
               f"weight={self.mass_kilo}," \
               f"notes={self.notes}," \
               f"status={self.status})"

    def __repr__(self):
        return f"Package(id={self.id}," \
               f"address={self.address}," \
               f"deadline={self.deadline}," \
               f"weight={self.mass_kilo}," \
               f"notes={self.notes}," \
               f"status={self.status})"
