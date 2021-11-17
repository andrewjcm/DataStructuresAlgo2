class Package:
    def __init__(self, id: int, address: str, city: str, state: str, zip_code: str, deadline: str,
                 mass_kilo: float, notes: str) -> None:
        """
        Creates a package object.

        Space-Time: O(n)

        :param id: unique id
        :param address: street address
        :param city: city
        :param state: state
        :param zip_code: zip or postal code
        :param deadline: specified time or "EOD" (end of day)
        :param mass_kilo: package weight in kilos
        :param notes: any additional notes
        """
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.priority = False if deadline == "EOD" else True
        self.mass_kilo = float(mass_kilo)
        self.notes = notes
        self.status = "Delayed" if notes and ("Delayed" in notes or "Wrong" in notes) else "At hub"
        self.delayed = True if self.status == "Delayed" else False
        self.truck_2_only = True if self.notes and "truck 2" in self.notes else False
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
