from faker import Faker

fake = Faker()


def get_object_data():
    return {
        "name": fake.name(),
        "data": {
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }
    }


OBJECT_DATA = get_object_data()

UPD_OBJECT_DATA = get_object_data()

OBJECTS_DATA = [get_object_data() for _ in range(5)]

MESSAGES = {
    "invalid object creation": "Invalid parameters"
}

INVALID_DATA_OBJECTS = [
    ("Create object with empty payload", {}),
    (
        "Create object without 'name' field",
        {"data": {"address": "Test address"}}
    ),
    (
        "Create object with empty 'name' field",
        {"name": "", "data": {"address": "Test address"}}
    ),
    (
        "Create object with integer in a 'name' field",
        {"name": 123, "data": {"address": "Test address"}}
    ),
    (
        "Create object without 'data' field",
        {"name": "Test Name"}
    ),
    (
        "Create object with empty string 'data' field",
        {"name": "Test Name", "data": ""}
    ),
    (
        "Create object with integer in a 'data' field",
        {"name": "Test Name", "data": 123}
    ),
]
