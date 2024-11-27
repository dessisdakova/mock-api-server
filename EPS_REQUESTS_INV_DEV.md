# Interact with the Inventory of Devices API
There are three available endpoints for inventory devices: "**/inventory/devices**", "**/guids**" and "**/path:guid/add**" with the following requests implemented:
### GET /inventory/devices
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST") 
	- Body: none
	- Response body (retrieved from `inventory_devices.json`): 
 		[
		    currently saved devices
		]
	- Response status code: 200 OK (initial, can be changed)
### PUT /inventory/devices
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
	- Body:
		{
		    "body": [
			{
			    device1
			},
			{
			    device2
			}
		    ],
		    "status_code": int
		}
	- Response status code: 200 OK
	- Response body: 
 		{
   		    "new_body": request key "body",
		    "new_status_code": request key "status_code"
		}
 	- Purpose: Updates the default_inventory_devices_response, which the GET request later uses.
### POST /path:guid/add
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
 	- Path Parameter: guid - The GUID to be added is passed as part of the URL path. Example: /12345/add
	- Body: none
	- Response status code: 200
	- Response body (retrieved and updated from guid_add.json):
	 	{
		    "guids": [ currently saved guids + guid from request ]
		}
 	- Purpose: Adds guid to guid list.
### GET /guids
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
	- Body: none
	- Response status code: 200 OK (initial, can be changed)
	- Response body: 
		{
		    "guids": [
		        currently saved guids
		    ]
		}
### PUT /guids
	- Headers: none explicitly mentioned, so default headers are used (for Postman remove "HOST")
 	- Body:
		{
		    "body": {
			"guids": [ values ]
		    },
		    "status_code": int
		}
  	- Response status code: 200 OK
	- Response body:
		{
   		    "new_body": request key "body",
		    "new_status_code": request key "status_code"
		}