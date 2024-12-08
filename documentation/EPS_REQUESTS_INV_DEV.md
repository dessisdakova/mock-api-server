# Interact with the Inventory of Devices API
There are three available endpoints for inventory devices: "**/inventory/devices**", "**/guids**" and "**/path:guid/add**" with the following requests implemented:
### GET /inventory/devices
	- Headers: none explicitly mentioned, so default headers are used
	- Body: none
	- Response body (retrieved from `inventory_devices.json`): 
 		[
		    currently saved devices
		]
	- Response status code: 200 OK (initial, can be changed)
	- Purpose: Retrieving inventory devices
### PUT /inventory/devices
	- Headers: none explicitly mentioned, so default headers are used
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
 	- Purpose: Updating body and status code of GET request /inventory/devices
### POST /path:guid/add
	- Headers: none explicitly mentioned, so default headers are used
 	- Path Parameter: guid - The GUID to be added is passed as part of the URL path. Example: /12345/add
	- Body: none
	- Response status code: 200
	- Response body (retrieved and updated from guid_add.json):
	 	{
		    "guids": [ currently saved guids + guid from request ]
		}
 	- Purpose: Adding guid to guid list
### GET /guids
	- Headers: none explicitly mentioned, so default headers are used
	- Body: none
	- Response status code: 200 OK (initial, can be changed)
	- Response body: 
		{
		    "guids": [
		        currently saved guids
		    ]
		}
	- Purpose: Retrieving all guids
### PUT /guids
	- Headers: none explicitly mentioned, so default headers are used
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
	- Purpose: Updating body and status code of GET request /guids