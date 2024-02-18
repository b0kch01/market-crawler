from typing import List

class FoodHall:
    class Demographic:
        def __init__(self, race: List[str], age_range: List[str]):
            self.race = race
            self.age_range = age_range

    class LeaseRates:
        def __init__(self, average_per_square_foot: float, range_per_square_foot: str):
            self.average_per_square_foot = average_per_square_foot
            self.range_per_square_foot = range_per_square_foot

    class RenovationHistory:
        def __init__(self, year: int, details: str):
            self.year = year
            self.details = details

    class Owner:
        def __init__(self, name: str, contact_info: str):
            self.name = name
            self.contact_info = contact_info

    class ManagementCompany:
        def __init__(self, name: str, contact_info: str):
            self.name = name
            self.contact_info = contact_info

    def __init__(self, name: str, city: str, state: str, square_footage: int, number_food_stalls: int,
                 types_of_food_stalls: List[str], demographic: 'Demographic', local_area_composition: List[str],
                 public_transport: bool, parking_availability: bool, foot_traffic_estimates: int,
                 annual_visitor_count: int, lease_rates: 'LeaseRates', occupancy_rate: float, year_established: int,
                 renovation_history: List['RenovationHistory'], owner: 'Owner', management_company: 'ManagementCompany'):

        # pass this in
        self.name = name
        self.city = city
        self.state = state
        self.square_footage = square_footage
        self.number_food_stalls = number_food_stalls
        self.types_of_food_stalls = types_of_food_stalls
        self.demographic = demographic
        self.local_area_composition = local_area_composition
        self.public_transport = public_transport
        self.parking_availability = parking_availability
        self.foot_traffic_estimates = foot_traffic_estimates
        self.annual_visitor_count = annual_visitor_count
        self.lease_rates = lease_rates
        self.occupancy_rate = occupancy_rate
        self.year_established = year_established
        self.renovation_history = renovation_history
        self.owner = owner
        self.management_company = management_company