from pathlib import Path
import pytest
import json
import os
import requests


@pytest.fixture(scope="session")
def config():
    """Load the configuration from config.json."""
    current_dir = Path(__file__).resolve().parent
    config_path = current_dir / "config.json"
    with open(config_path) as file:
        data = json.load(file)
    return data


@pytest.fixture(scope="session")
def base_url(config):
    """Set base URL and port based on the protocol specified in the config.
    If HTTPS is selected, ensure certificates are downloaded and set up."""
    if config["protocol"] == "http" or config["protocol"] == "https":
        protocol = config["protocol"]
    else:
        raise ValueError("Invalid protocol.")

    if config["host"] == "localhost" or config["host"] == "api-mock":
        host = config["host"]
    else:
        raise ValueError("Invalid host.")

    if protocol == "http" and host == "localhost":
        port = 8080
    elif protocol == "https" and host == "localhost":
        port = 8443
    elif protocol == "http" and host == "api-mock":
        port = 80
    elif protocol == "https" and host == "api-mock":
        port = 443

    return f"{protocol}://{host}:{port}"


def fetch_and_save_certificates(host):
    """Download root and intermediate CA certificates from the server and save them locally.
    Combine them into a single CA bundle for HTTPS requests."""
    certs_dir = Path("certs")
    certs_dir.mkdir(exist_ok=True)
    ca_bundle_path = certs_dir / "ca_bundle.pem"

    # Fetch certificates
    if host == "localhost":
        port = 8080
    else:
        port = 80
    root_ca_response = requests.get(f"http://{host}:{port}/mock_certs/root_ca")
    intermediate_ca_response = requests.get(f"http://{host}:{port}/mock_certs/intermediate_ca")

    # Save certificates
    with open(ca_bundle_path, "wb") as file:
        file.write(root_ca_response.content)
        file.write(intermediate_ca_response.content)

    print(f"Certificates saved successfully at {ca_bundle_path}")
    return ca_bundle_path


@pytest.fixture(scope="session")
def ca_bundle(config):
    """Provide the CA bundle path if HTTPS is enabled. Return None if using HTTP."""
    if config["protocol"].lower() == "https":
        if config["certs"] == "download":
            return fetch_and_save_certificates(config["host"])
        elif config["certs"] == "mounted":
            return None  # requests lib by default uses REQUESTS_CA_BUNDLE set in compose.yaml
    return None


@pytest.fixture(scope="session")
def endpoints_dev(base_url):
    """Fixture to provide API endpoints for inventory devices"""
    return {
        "inventory_devices": f"{base_url}/inventory/devices",
        "guids": f"{base_url}/guids",
    }


@pytest.fixture(scope="session")
def add_guid(base_url, request):
    guid_value = request.param
    return f"{base_url}/{guid_value}/add"


@pytest.fixture(scope="session")
def endpoints_files(base_url):
    """Fixture to provide API endpoints for handling files"""
    return {
        "root_certs": f"{base_url}/mock_certs/root_ca",
        "intermediate_certs": f"{base_url}/mock_certs/intermediate_ca",
        "upload": f"{base_url}/file/add"
    }


@pytest.fixture(scope="function", autouse=True)
def reset_server_state(base_url, endpoints_dev, ca_bundle):
    """Reset the server state to its initial conditions after all tests"""
    yield

    body_inv = {
      "body": [
        {
          "id": "TEST1",
          "ipAddress": "10.0.49.140",
          "deviceAddresses": {
            "fqdn": "test.com",
            "ipv4Address": "10.0.49.140",
            "ipv6Address": "null"
          },
          "model": "TEST_DEVICE",
          "serialNum": "TEST1-1fecaf6a-0619-41b1-86d8-acf36064f9ec",
          "version": "2.3.12",
          "build": "20240410.1854-8f4e21frg65t"
        },
        {
          "id": "TEST2",
          "ipAddress": "10.0.49.141",
          "deviceAddresses": {
            "fqdn": "test.com",
            "ipv4Address": "10.0.49.141",
            "ipv6Address": "2de4:712b:d13d:d51e:0d5f:3530:1d51:1493"
          },
          "model": "TEST_DEVICE",
          "serialNum": "TEST2-1ghfaf6a-0723-52e1-86d8-acf42055f9eg",
          "version": "3.0.0",
          "build": "20240410.1854-8f4e21y111ef-snapshot"
        }
      ],
      "status_code": 200
    }

    body_guids = {
      "body": {
        "guids": []
      },
      "status_code": 200
    }

    # act
    requests.put(endpoints_dev["inventory_devices"], json=body_inv, verify=ca_bundle)
    requests.put(endpoints_dev["guids"], json=body_guids, verify=ca_bundle)
