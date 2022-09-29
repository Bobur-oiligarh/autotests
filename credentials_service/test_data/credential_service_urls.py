credentials_service = {
    "environment": {
        "all": "http://172.38.107.149:7076/"
    },
    "references": {
        "create_user": {
            "path": "create-user",
            "method": "post"
        },
        "update_user": {
            "path": "update-user",
            "method": "post"
        },
        "get_device_info": {
            "path": "get-device-info",
            "method": "post"
        },
        "device_auth": {
            "path": "device-auth",
            "method": "post"
        }
    }
}
