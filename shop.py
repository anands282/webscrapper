from dataclasses import dataclass


@dataclass
class Shop:
    shop_name: str = None
    shop_location: str = None
    contact_number: str = None
    website: str = None
    average_review_count: str = None
    average_review_points: str = None

