import requests


def get_object_by_id(url: str, object_id: int) -> tuple[requests.Response, dict]:
    """
    Fetch a specific object by its ID.

    :param url: Base URL of the API.
    :param object_id: ID of the object to retrieve.
    :return: A tuple containing:
        - The Response object from the GET request.
        - A dictionary with the parsed JSON response.
    """
    response = requests.get(f"{url}/{object_id}")
    response_data = response.json()
    return response, response_data


def update_object(
        url: str,
        object_id: int,
        payload: dict,
        method: str
) -> tuple[requests.Response, dict]:
    """
    Update an existing object using either the PUT or PATCH method.

    :param url: Base URL of the API.
    :param object_id: ID of the object to update.
    :param payload: A dictionary containing the updated data.
    :param method: HTTP method to use, either "PUT" or "PATCH".
                 Raises an exception if an invalid method is provided.
    :return: A tuple containing:
        - The Response object from the request.
        - A dictionary with the parsed JSON response.
    :raises ValueError: If `method` is not "PUT" or "PATCH".
    """
    if method == "PUT":
        response = requests.put(f"{url}/{object_id}", json=payload)
    elif method == "PATCH":
        response = requests.patch(f"{url}/{object_id}", json=payload)
    else:
        raise ValueError("Invalid method. Use 'PUT' or 'PATCH'.")

    response_data = response.json()
    return response, response_data
