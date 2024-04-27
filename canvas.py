import time
import hashlib
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.delivery_category import DeliveryCategory
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.gender import Gender
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.serverside.action_source import ActionSource

def toHash(email):
    hash_object = hashlib.sha256()
    # Converter o email em bytes e atualizar o objeto hash
    hash_object.update(email.encode())
    # Obter o hash final
    return hash_object.hexdigest()

access_token = 'EAAC89fkUGNEBABlJXKOZBjErJ1oWR0E7AmkeGZAhG3fZBDN2tDvl9VWOzPa7E5WuRw3mpG8NiPpfWClguG0bbwgMj9U1bwfqL0JjmIMbydHNLCCyetOyOlSqPQ2JSqBmErgpZCiJCnL2iBqZBm35MHQD3JDqfshRWJKUDvAV3qPpDRvh9QNLfnfQGa1QKu8AZD'
pixel_id = '2120259218170665'

def fb_pixel_request(price, email="", phone="", ip="186.206.45.225", agent="", event="Purchase", country="Brasil"):
    FacebookAdsApi.init(access_token=access_token)
    user_data_0 = UserData(
        country_codes=[toHash(country)],
        client_ip_address=ip,
        client_user_agent=agent,
        email=toHash(email),
        phones=[toHash(phone)]
    )
    custom_data_0 = CustomData(
        value=price,
        currency="BRL"
    )
    event_0 = Event(
        event_name=event,
        event_time=int(time.time()),
        user_data=user_data_0,
        custom_data=custom_data_0,
        action_source=ActionSource.WEBSITE
    )
    events = [event_0]
    event_request = EventRequest(
        events=events,
        pixel_id=pixel_id
    )
    return event_request.execute()


req = fb_pixel_request(price=30.00, email="luistiago.andrighetto@gmail.com", phone="41985311304", ip="186.206.45.225", agent="", event="Purchase")
print(req)