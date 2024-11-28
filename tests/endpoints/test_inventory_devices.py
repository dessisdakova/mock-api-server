import pytest
import requests
from common.data_loader import load_test_data


def assert_successful_get_request(response, expected_keys, sub_key_name, expected_sub_keys):
    assert response.status_code == 200, "Response status code is not 200 OK."
    assert isinstance(response.json(), (list, dict)), "Response body is neither an array nor an object."
    for device in response.json():
        for key in expected_keys:
            assert key in device, f"Key '{key}' is missing in device."

        sub_key = device.get(sub_key_name)
        assert sub_key is not None, f"Key '{sub_key_name}' is missing in device."
        assert isinstance(sub_key, dict), f"Key '{sub_key_name}' is not an object in device."
        for expected_sub_key in expected_sub_keys:
            assert expected_sub_key in sub_key, f"Sub-key '{expected_sub_key}' is missing in '{sub_key_name}'."


def send_and_assert_get_request_after_put_request(put_response, endpoints_dev, ca_bundle):
    data = put_response.json()
    get_response = requests.get(endpoints_dev["inventory_devices"], verify=ca_bundle)
    get_data = get_response.json()
    assert get_data == data["new_body"], "Body of GET request was not changed."
    try:
        new_status_code = int(data["new_status_code"])
        assert get_response.status_code == new_status_code, "Status code of GET request was not changed."
    except (ValueError, TypeError):
        # If the status_code is not valid, the server sets default status code ot GET request
        assert get_response.status_code == put_response.status_code, \
            "Status code should remain the same when 'new_status_code' is invalid."


def assert_successful_put_request(body, response):
    data = response.json()
    expected_keys = ["new_body", "new_status_code"]
    assert response.status_code == 200, "Response status code is not 200 OK."
    assert isinstance(data, dict), "Response is not a JSON object."
    for key in expected_keys:
        assert key in data, f"Key '{key}' is missing in response."
    assert data["new_body"] == body["body"], "'body' keys don't match."
    assert data["new_status_code"] == body["status_code"], "'status_code' keys don't match."


def test_retrieving_currently_saved_devices(base_url, endpoints_dev, ca_bundle):
    """TC_INV_01"""
    # arrange
    expected_keys = ["build", "deviceAddresses", "id", "ipAddress", "model", "serialNum", "version"]
    sub_key = "deviceAddresses"
    expected_device_addresses_keys = ["fqdn", "ipv4Address", "ipv6Address"]

    # act
    response = requests.get(endpoints_dev["inventory_devices"], verify=ca_bundle)

    # assert
    assert_successful_get_request(response, expected_keys, sub_key, expected_device_addresses_keys)


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_02"))
def test_changing_response_of_get_req(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_02"""
    # arrange
    body = {
          "body": test_data["body"],
          "status_code": test_data["status_code"]
        }

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    send_and_assert_get_request_after_put_request(response, endpoints_dev, ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_03"))
def test_behavior_when_key_is_missing(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_03"""
    # arrange
    body = test_data

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)

    # assert
    assert response.status_code == 500, "Response status code is not 500 Internal Server Error."
    assert "Internal Server Error" in response.text, "Response does not contain 'Internal Server Error'."
    assert response.headers.get("Content-Type", "").startswith("text/html"), "Response is not HTML."


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_04"))
def test_behavior_when_status_code_is_sent_as_an_array_or_float(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_04"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)
    response_get = requests.get(endpoints_dev["inventory_devices"], verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    assert response_get.status_code == 500, "Status code of GET is not 500 Internal Server Error."
    assert "Internal Server Error" in response_get.text, \
        "Response of GET request does not contain 'Internal Server Error'."
    assert response_get.headers.get("Content-Type", "").startswith("text/html"), "Response of GET request is not HTML."


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_05"))
def test_behavior_when_status_code_is_sent_as_an_object(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_05"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    send_and_assert_get_request_after_put_request(response, endpoints_dev, ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_06"))
def test_behavior_when_status_code_is_sent_as_an_invalid_string(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_06"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(endpoints_dev["inventory_devices"], verify=ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_07"))
def test_behavior_when_status_code_is_an_integer_with_invalid_code(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_07"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(endpoints_dev["inventory_devices"], verify=ca_bundle)


@pytest.mark.parametrize("test_data", load_test_data("test_data_inv.json", "TC_INV_08"))
def test_behavior_when_status_code_is_an_integer_with_valid_code(base_url, endpoints_dev, ca_bundle, test_data):
    """TC_INV_08"""
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }

    # act
    response = requests.put(endpoints_dev["inventory_devices"], json=body, verify=ca_bundle)

    # assert
    assert_successful_put_request(body, response)
    send_and_assert_get_request_after_put_request(response, endpoints_dev, ca_bundle)
