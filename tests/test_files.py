import requests


def assert_get_request(response):
    assert response.status_code == 200, "Response status code is not 200 OK."
    assert "-----BEGIN CERTIFICATE-----" in response.text, "Response does not contain start of certificates."
    assert "-----END CERTIFICATE-----" in response.text, "Response does not contain end of certificates."
    assert response.headers.get("Content-Disposition", "").startswith("attachment"), \
        "Response does not have an attachment."
    assert response.headers.get("Content-Type", "").startswith("application/pem-certificate-chain"), \
        "Response is not sending certificates."


def test_retrieving_root_certificates(base_url, endpoints_files, ca_bundle):
    """TC_INV_FILES_01"""
    # act
    response = requests.get(endpoints_files["root_certs"], verify=ca_bundle)

    # assert
    assert_get_request(response)


def test_retrieving_intermediate_certificates(base_url, endpoints_files, ca_bundle):
    """TC_INV_FILES_02"""
    # act
    response = requests.get(endpoints_files["intermediate_certs"], verify=ca_bundle)

    # assert
    assert_get_request(response)


def test_uploading_file_successfully(base_url, endpoints_files, ca_bundle):
    """TC_INV_FILES_03"""
    # arrange
    file_name = "upload_this.txt"  # expected to exist in the same directory as the test
    file_path = f"test_data/{file_name}"  # used to open the file for reading

    # act
    # In order to send a file, it needs to be read and converted into a format that can be included in the request
    with open(file_path, "rb") as file:
        # files dictionary is a standard way of packaging files in requests
        files = {'file': (file_name, file, 'application/octet-stream')}

        # send the POST request with the file
        response = requests.post(endpoints_files["upload"], files=files, verify=ca_bundle)

    # assert
    assert response.status_code == 200, "Response status code is not 200 OK."
    assert f"File uploaded successfully to /opt/project/upload/{file_name}" in response.text, "File was not uploaded."


def test_sending_request_without_attached_file(base_url, endpoints_files, ca_bundle):
    """TC_INV_FILES_04"""
    # act
    response = requests.post(endpoints_files["upload"], verify=ca_bundle)

    # assert
    assert response.status_code == 400, "Response status code is not 400 Bad Request."
    assert f"No file part in the request" in response.text, "Incorrect error message."


def test_sending_request_without_selected_file(base_url, endpoints_files, ca_bundle):
    """TC_INV_FILES_03"""
    # act
    response = requests.post(endpoints_files["upload"], files={"file": ("", b"")}, verify=ca_bundle)

    # assert
    assert response.status_code == 400, "Response status code is not 400 Bad Request."
    assert f"No selected file" in response.text, "Incorrect error message."
