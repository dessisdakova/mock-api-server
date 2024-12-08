# Interact with the Inventory of Files API
There are three available endpoints for inventory files: "**/mock_certs/root_ca**", "**/mock_certs/intermediate_ca**" and "**/file/add**" with the following requests implemented:
### GET /mock_certs/root_ca
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
	- Body: none
	- Response body: 
 		-----BEGIN CERTIFICATE-----
		genarated certificates
		-----END CERTIFICATE-----
	- Response status code: 200 OK
	- Purpose: Downloading certificates
### GET /mock_certs/intermediate_ca
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
	- Body: none
	- Response body: 
 		-----BEGIN CERTIFICATE-----
		genarated certificates
		-----END CERTIFICATE-----
	- Response status code: 200 OK
	- Purpose: Downloading intermediate certificates
### POST /file/add
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
	- Body: use the form-data option.
		- Key: file (type = file)
		- Value: select a file to upload from your local system.
	- Expected responses and status codes:
		- File uploaded successfully to /opt/project/upload/filename, 200 OK
		- No file part in the request, 400 Bad Request
		- No selected file, 400 Bad Request
	- Purpose: Uploading file to container