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
    "invalid parameters": "Invalid parameters",
    "invalid id": "The requested URL was not found on the server."
                  " If you entered the URL manually please check your "
                  "spelling and try again."
}

INVALID_DATA = [
    ("Empty payload", {}),
    (
        "Absent 'name' field",
        {"data": {
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }}
    ),
    (
        "Empty 'name' field",
        {"name": "", "data": {
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }}
    ),
    (
        "Integer in a 'name' field",
        {"name": 123, "data": {
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }}
    ),
    (
        "Absent 'data' field",
        {"name": fake.name()}
    ),
    (
        "Empty string in 'data' field",
        {"name": fake.name(), "data": ""}
    ),
    (
        "Integer in a 'data' field",
        {"name": fake.name(), "data": 123}
    ),
]

PATCH_DATA = [
    (
        "Update 'name' field",
        {"name": fake.name()}
    ),
    (
        "Update 'data' field",
        {"data": {
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }}
    ),
]

INVALID_PATCH_DATA = [
    ("Empty payload", {}),
    (
        "Empty 'name' field",
        {"name": ""}
    ),
    (
        "Integer in a 'name' field",
        {"name": 123}
    ),
    (
        "Empty string in 'data' field",
        {"data": ""}
    ),
    (
        "Integer in a 'data' field",
        {"data": 123}
    ),
]
