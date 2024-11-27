import pytest
import requests
import json


# Load test data from JSON file
def load_test_data(file_path, test_case):
    with open(file_path, 'r') as file:
        return json.load(file)[test_case]


def assert_successful_get_request(response, expected_values):
    data = response.json()
    assert response.status_code == 200, "Response status code is not 200 OK."
    assert isinstance(data, dict), "Response body is not an object."
    assert "guids" in data, "Key 'guids' is missing."
    assert len(data) == 1, "There are more than one keys."
    assert isinstance(data["guids"], list), "Key 'guids' is not array."
    assert data["guids"] == expected_values, "Key 'guids' values are not as expected."


def assert_successful_put_request(body, response):
    data = response.json()
    expected_keys = ["new_body", "new_status_code"]
    assert response.status_code == 200, "Response status code is not 200 OK."
    assert isinstance(data, dict), "Response is not a JSON object."
    for key in expected_keys:
        assert key in data, f"Key '{key}' is missing in response."
    assert data["new_body"] == body["body"], "'body' keys don't match."
    assert data["new_status_code"] == body["status_code"], "'status_code' keys don't match."


def send_and_assert_get_request_after_put_request(put_response, endpoints_dev, ca_bundle):
    data = put_response.json()
    get_response = requests.get(endpoints_dev["guids"], verify=ca_bundle)
    get_data = get_response.json()
    assert get_data == data["new_body"], "Body of GET request was not changed."
    try:
        new_status_code = int(data["new_status_code"])
        assert get_response.status_code == new_status_code, "Status code of GET request was not changed."
    except (ValueError, TypeError):
        # If the status_code is not valid, the server sets default status code ot GET request
        assert get_response.status_code == put_response.status_code, \
            "Status code should remain the same when 'new_status_code' is invalid."


def test_retrieving_guids_list(base_url, endpoints_dev, ca_bundle):
    """TC_INV_09"""
    # act
    response = requests.get(endpoints_dev["guids"], verify=ca_bundle)
    expected_values = []
    # assert
    assert_successful_get_request(response, expected_values)


@pytest.fixture(scope="session")
def expected_values():
    """Fixture to store expected values across tests"""
    return []


@pytest.mark.parametrize("add_guid", ["7777", 7777, "sometext", "123!abc", "77.77", "77-+/!^_+77"], indirect=True)
def test_adding_valid_value_to_guids_list(base_url, add_guid, ca_bundle, expected_values):
    """TC_INV_10"""
    # act
    response = requests.post(add_guid, verify=ca_bundle)

    # Add the guid to expected values list
    guid_added = add_guid.split(base_url + "/")[1].split("/add")[0]  # Extract the GUID from the endpoint
    expected_values.append(guid_added)

    # assert
    assert_successful_get_request(response, expected_values)


@pytest.mark.parametrize("add_guid", ["#", "/", "", "?"], indirect=True)
def test_adding_invalid_value_to_guids_list(base_url, add_guid, ca_bundle):
    """TC_INV_11"""
    # act
    response = requests.post(add_guid, verify=ca_bundle)

    # assert
    assert response.status_code == 404, "Response status code is not 404 NOT FOUND."
    assert "404 Not Found" in response.text, "Response does not contain '404 Not Found'."
    assert response.headers.get("Content-Type", "").startswith("text/html"), "Response is not HTML."


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_12"))
def test_changing_response_of_get_req(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_12"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    send_and_assert_get_request_after_put_request(response, endpoints_dev, ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_13"))
def test_behavior_when_key_is_missing(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_13"""
    # arrange
    body = test_data

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)

    # assert
    assert response.status_code == 500, "Response status code is not 500 Internal Server Error."
    assert "Internal Server Error" in response.text, "Response does not contain 'Internal Server Error'."
    assert response.headers.get("Content-Type", "").startswith("text/html"), "Response is not HTML."


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_14"))
def test_behavior_when_status_code_is_sent_as_an_array_or_float(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_14"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)
    response_get = requests.get(endpoints_dev["guids"], verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    assert response_get.status_code == 500, "Status code of GET is not 500 Internal Server Error."
    assert "Internal Server Error" in response_get.text, \
        "Response of GET request does not contain 'Internal Server Error'."
    assert response_get.headers.get("Content-Type", "").startswith("text/html"), "Response of GET request is not HTML."


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_15"))
def test_behavior_when_status_code_is_sent_as_an_object(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_15"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    send_and_assert_get_request_after_put_request(response, endpoints_dev, ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_16"))
def test_behavior_when_status_code_is_sent_as_an_invalid_string(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_16"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(endpoints_dev["guids"], verify=ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_17"))
def test_behavior_when_status_code_is_an_integer_with_invalid_code(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_17"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(endpoints_dev["guids"], verify=ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data/test_data_inv.json", "TC_INV_18"))
def test_behavior_when_status_code_is_an_integer_with_valid_code(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_18"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["guids"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    send_and_assert_get_request_after_put_request(response, endpoints_dev, ca_bundle)
