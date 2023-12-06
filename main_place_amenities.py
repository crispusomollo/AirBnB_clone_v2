#!/usr/bin/python3
""" Test link for Amenity
"""
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
# Create a State
state = State(name="California")
state.save()

# Create a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# Create a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# Create 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# Create 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# Link a place with the amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# Link place with amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK") 

