# Test cases for the Inventory of Devices API

| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_01 |Verify retrieving currently saved devices| GET | /inventory/devices|

**Pre-conditions:**
 - The API server is running.
 -  All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.
 - No prior PUT requests should have been made to the `/inventory/devices` endpoint during the session.

**Test Steps:**
1. Send a GET request to  `/inventory/devices`.

**Expected Results:**
1. Response status code should be `200 OK`. 
2. Response body should be an array of devices predefined in the `inventory_devices.json` file. 
3. For each device in the array еnsure the presence of the following keys:
	 -  `build`
	 -  `deviceAddresses` (with sub-keys: `fqdn`, `ipv4Address`, `ipv6Address`)
	 -  `id`
	 -  `ipAddress`
	 -  `model`
	 -  `serialNum`
	 -  `version`
4. Validate that the values of these keys match the expected format and structure.
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_02 |Verify changing the response body and status code of GET request| PUT| /inventory/devices|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a **PUT** request to `/inventory/devices` with the following request body and modifications:
- Test Case 1: Complete data.
```json
{
	"body": [
		{
			"build": "20240410.1854-8f4e21frg65t",
			"deviceAddresses": {
			"fqdn": "test.com",
			"ipv4Address": "10.0.49.140",
			"ipv6Address": null
			},
			"id": "UPDATED_1",
			"ipAddress": "10.0.49.140",
			"model": "TEST_DEVICE",
			"serialNum": "TEST1-1fecaf6a-0619-41b1-86d8-acf36064f9ec",
			"version": "2.3.12"
		}
	],
	"status_code": 201
}
```

- Test Case 2: Remove a key in the device object from the request body (remove `build` key).
 - Test Case 3: Change the value for a key to a different type (change `id` from string to integer).
 - Test Case 4: Send an empty list in the body (`[]`).
 - Test Case 5: Send an object (rather than a list) in the body (`{}`).
 - Test Case 6: Change the status code to a string (`"201"` instead of `201`, parse it to integer in automation).

**Expected Results:**
 1. Response status code of the **PUT** request should be `200 OK`.
 2. Response body should be an object containing the following keys:
	-  `new_body`
	-  `new_status_code`
3. The value of `new_body` in the response should match the `body` sent in the **PUT** request.
4. The value of `new_status_code` in the response should match the `status_code` sent in the **PUT** request.
5. Send a **GET** request to `/inventory/devices` and verify that:
6. The response body equals the `new_body` sent in the **PUT** request.
7. The response status code equals `new_status_code` sent in the **PUT** request.
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_03 |Verify behavior when *body* or *status_code* key is missing in request body| PUT| /inventory/devices|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a **PUT** request to `/inventory/devices` with the following modifications in the body:
- Test Case 1: missing `body` key in the body.
- Test Case 2: missing `status_code` key in the body.

**Expected Results:**

1. Response status code of the **PUT** request should be `500 Internal Server Error`.
2. Response body should be the following HTML:
```html
<html>
	<head>
		<title>Internal Server Error</title>
	</head>
	<body>
		<h1>
			<p>Internal Server Error</p>
		</h1>
	</body>
</html>
```
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_04 |Verify behavior when *status_code* is sent as an array or float| PUT| /inventory/devices|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a **PUT** request to `/inventory/devices` with the following modifications in the body:
- Test Case 1: `"status_code": [200]`
- Test Case 2: `"status_code": 200.00`

**Expected Results:**
1. Response status code of the **PUT** request should be `200 OK`.
2. Response body should be an object containing the following keys:
	-  `new_body`
	-  `new_status_code`
3. The value of `new_body` in the response should match the `body` sent in the **PUT** request.
4. The value of `new_status_code` in the response should match the `status_code` sent in the **PUT** request.
5. Send a **GET** request to `/inventory/devices` and verify that:
	- Response status code should be `500 Internal Server Error`.
	- Response body should be the following HTML:
```html
<html>
	<head>
		<title>Internal Server Error</title>
	</head>
	<body>
		<h1>
			<p>Internal Server Error</p>
		</h1>
	</body>
</html>
```
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_05 |Verify behavior when *status_code* is sent as an object| PUT| /inventory/devices|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**

1. Send a **PUT** request to `/inventory/devices` with the following modification in the body:
	-  `"status_code": {"code": 300}`

**Expected Results:**
1. Response status code of the **PUT** request should be `200 OK`.
2. Response body should be an object containing the following keys:
	-  `new_body`
	-  `new_status_code`
3. The value of `new_body` in the response should match the `body` sent in the **PUT** request.
4. The value of `new_status_code` in the response should match the `status_code` sent in the **PUT** request.
5. Send a **GET** request to `/inventory/devices` and verify that:
	- Response body equals the `new_body` sent in the **PUT** request.
	- Response status code in not changed.
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_06 |Verify behavior when status_code is sent as an invalid string or a negative value| PUT| /inventory/devices|

 **Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**

1. Send a **PUT** request to `/inventory/devices` with the following modifications in the body:
- Test Case 1: `"status_code": "text"` (Invalid string that can't be parsed to an integer).
- Test Case 2: `"status_code": "200.00"` (Status code as a string with a decimal, which should be invalid).

**Expected Results:**
1. Response status code of the **PUT** request should be `200 OK`.
2. Response body should be an object containing the following keys:
	-  `new_body`
	-  `new_status_code`
3. The value of `new_body` in the response should match the `body` sent in the **PUT** request.
4. The value of `new_status_code` in the response should match the `status_code` sent in the **PUT** request.
5. Try to send a **GET** request to `/inventory/devices` and verify "Could not get response" error.
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_07 |Verify behavior when *status_code* is an integer with invalid code| PUT| /inventory/devices|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a **PUT** request to `/inventory/devices` with the following modifications in the body:
- Test Case 1: `"status_code": -201`.
- Test Case 2: `"status_code": 0`.
- Test Case 3: `"status_code": 100` (should be valid for Informational responses).
- Test Case 4: `"status_code": 199` (should be valid for Informational responses).
- Test Case 5: `"status_code": 1000`.

**Expected Results:**
1. Response status code of the **PUT** request should be `200 OK`.
2. Response body should be an object containing the following keys:
	-  `new_body`
	-  `new_status_code`
3. The value of `new_body` in the response should match the `body` sent in the **PUT** request.
4. The value of `new_status_code` in the response should match the `status_code` sent in the **PUT** request.
5. Try to send a **GET** request to `/inventory/devices` and verify "Could not get response" error.
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_08 |Verify behavior when *status_code* is an integer with valid HTTP codes| PUT| /inventory/devices|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a **PUT** request to `/inventory/devices` with the following modifications in the body:
- Test Case 1: `"status_code": 200`.
- Test Case 2: `"status_code": 300`.
- Test Case 3:`"status_code": 500`.
- Test Case 4:`"status_code": 707`.
- Test Case 5:`"status_code": 999`.

**Expected Results:**
1. Response status code of the **PUT** request should be `200 OK`.
2. Response body should be an object containing the following keys:
	-  `new_body`
	-  `new_status_code`
3. The value of `new_body` in the response should match the `body` sent in the **PUT** request.
4. The value of `new_status_code` in the response should match the `status_code` sent in the **PUT** request.
5. Send a **GET** request to `/inventory/devices` and verify that:
	- Response body equals the `new_body` sent in the **PUT** request.
	- Response status code equals `new_status_code` sent in the **PUT** request.

------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_09 |Verify retrieving guids list| GET| /guids|

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.
- No prior POST or PUT requests should have been made to the same endpoint during the session.

**Test Steps:**
1. Send a GET request to `/guids` endpoint.

**Expected Results:**
1. Response status code should be `200 OK`.
2. Response body should be an object with one key - `"guids"`.
3. The value of the `"guids"` key should be an empty array:
```json
{
	"guids": []
}
```
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_10 |Verify adding valid value to guids list| POST| /<path:guid>/add|
  
  **Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.
- No prior POST or PUT requests should have been made to the same endpoint during the session.

**Test Steps:**
1. Send a **POST** request to `/<path:guid>/add` with no body and the following values for `path:guid`:
	- 7777
	- "7777"
	- sometext
	- 123!abc
	- 77.77
	- 77-+*/!^*_+77

**Expected Results:**
1. Response status code should be `200 OK`.
2. Response body should be an object with one key - `"guids"`.
3. The value of the `"guids"` key should be an array containing the GUID value passed in the request URL.
```json
{
	"guids": [
		7777
	]
}
```
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_11 |Verify adding invalid value to guids list| POST| /<path:guid>/add|
  
**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.
- No prior POST or PUT requests should have been made to the same endpoint during the session.

**Test Steps:**
1. Send a **POST** request to `/<path:guid>/add` with no body and the following values for `path:guid`:
	-  \#
	- empty string
	- /
	- ?

**Expected Results:**
1. Response status code should be `404 NOT FOUND`.
2. Response body should be the following HTML:
```html
<!doctype  html>
<html  lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
</html>
```
------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_12 |Verify changing the response body and status code of GET request| PUT| /guids|
  
**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a **PUT** request to `/guids` endpoint. Applicable test cases:
- TC_INV_002
- TC_INV_003
- TC_INV_004
- TC_INV_005
- TC_INV_006
- TC_INV_007
- TC_INV_008

  
# Test cases for the Inventory of Files API

| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_FILES_01 |Verify downloading certificates| GET|  /mock_certs/root_ca |

**Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a GET request to `/mock_certs/root_ca` endpoint.

 **Expected Results:**
1. Response status code should be `200 OK`.
2. Response text should include:
	-  `-----BEGIN CERTIFICATE-----`
	-  `-----END CERTIFICATE-----`
3. Response header `Content-Disposition:` should be `attachment; filename=ca.cert.pem`
4. Response header `Content-Type:` should be `application/pem-certificate-chain`
  ------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_FILES_02 |Verify downloading intermediate certificates| GET |  /mock_certs/intermediate_ca |
  
 **Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a GET request to `/mock_certs/intermediate_ca` endpoint.

 **Expected Results:**
1. Response status code should be `200 OK`.
2. Response text should include:
	-  `-----BEGIN CERTIFICATE-----`
	-  `-----END CERTIFICATE-----`
3. Response header `Content-Disposition:` should be `attachment; filename=intermediate.cert.pem`
4. Response header `Content-Type:` should be `application/pem-certificate-chain`
  ------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_FILES_03 |Verify uploading a file successfully| POST | /file/add |
  
 **Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a POST request to `/file/add` endpoint with attached file in body.

 **Expected Results:**
1. Response status code should be `200 OK`.
2. Response text should be `File uploaded successfully to /opt/project/upload/filename`.
  ------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_FILES_04 |Verify sending request without attached file| POST | /file/add |
  
 **Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a POST request to `/file/add` endpoint without attaching a file to body.

**Expected Results:**
1. Response status code should be `400 Bad Request`.
2. Response text should be `No file part in the request`.
  ------------------------------------------------
| ID | Title | Request | Endpoint |
|:--:|:-----:|:-------:|:--------:|
| TC_INV_FILES_05 |Verify sending request without selected file| POST | /file/add |

 **Pre-conditions:**
- The API server is running.
- All tests should be run only against HTTPS (port `8443`) or HTTP (port `8080`) for each session.

**Test Steps:**
1. Send a POST request to `/file/add` endpoint without selecting a file in body.

 **Expected Results:**
1. Response status code should be `400 Bad Request`.
2. Response text should be `No selected file`.