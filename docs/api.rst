API
=========

Endpoints
---------
 * "silo": "https://tables.hikayadata.io/api/silo/",
 * "public_tables": "https://tables.hikayadata.io/api/public_tables/",
 * "users": "https://tables.hikayadata.io/api/users/",
 * "read": "https://tables.hikayadata.io/api/read/",
 * "readtype": "https://tables.hikayadata.io/api/readtype/",
 * "tag": "https://tables.hikayadata.io/api/tag/"
 * "owners": "https://tables.hikayadata.io/api/owners"
 * "boards": "https://tables.hikayadata.io/api/boards"
 * "graphs": "https://tables.hikayadata.io/api/graphs"
 * "graphmodels": "https://tables.hikayadata.io/api/graphmodels"
 * "items": "https://tables.hikayadata.io/api/items"
 * "graphinputs": "https://tables.hikayadata.io/api/graphinputs"
 * "boardsilos": "https://tables.hikayadata.io/api/boardsilos"

 

Silo (Represents a Table)

Example
-------
::
    curl -H "Authorization: Token adkai39a9sdfj239m0afi2" https://tables.hikayadata.io/api/silo/{{siloid}}/`

GET /api/silo/

HTTP 200 OK
Allow: GET, POST, OPTIONS
Content-Type: application/json
Vary: Accept

::
    {
        "owner": {
            "url": "http://tables.hikayadata.io/api/users/2/",
            "password": "!kBeo6116YCeMonUVGpB2Q9ONRh387XLtPNy0u6CJ",
            "last_login": "2017-01-13T17:00:53Z",
            "is_superuser": false,
            "username": "glindf9003af87068415a",
            "first_name": "Greg",
            "last_name": "Lind",
            "email": "peter@hikaya.io",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2015-10-08T00:50:29Z",
            "groups": [],
            "user_permissions": []
        },
        "name": "NS Security Incident",
        "reads": [
            {
                "url": "http://tables.hikayadata.io/api/read/10/",
                "read_name": "NS Security Incident",
                "description": "",
                "read_url": "https://api.ona.io/api/v1/data/132211",
                "resource_id": null,
                "gsheet_id": null,
                "username": null,
                "password": null,
                "token": null,
                "file_data": null,
                "autopull_frequency": "daily",
                "autopush_frequency": null,
                "create_date": "2016-07-02T19:48:49Z",
                "edit_date": "2016-08-24T17:54:52Z",
                "owner": "http://tables.hikayadata.io/api/users/2/",
                "type": "http://tables.hikayadata.io/api/readtype/1/"
            },
            {
                "url": "http://tables.hikayadata.io/api/read/79/",
                "read_name": "NS Security Incident",
                "description": "Google Spreadsheet Export",
                "read_url": "https://docs.google.com/a/hikaya.io/spreadsheets/d/1x7n0JViOqQB90W-G38QR5D2lHfJQWyZpkOUZfypWY0Y/",
                "resource_id": "1x7n0JViOqQB90W-G38QR5D2lHfJQWyZpkOUZfypWY0Y",
                "gsheet_id": null,
                "username": null,
                "password": null,
                "token": null,
                "file_data": null,
                "autopull_frequency": null,
                "autopush_frequency": null,
                "create_date": "2016-10-10T08:12:26Z",
                "edit_date": "2016-10-10T08:12:26Z",
                "owner": "http://tables.hikayadata.io/api/users/2/",
                "type": "http://tables.hikayadata.io/api/readtype/3/"
            }
        ],
        "description": null,
        "create_date": null,
        "id": 12,
        "data": "http://tables.hikayadata.io/api/silo/12/data/",
        "shared": [],
        "tags": [],
        "public": false
    },
