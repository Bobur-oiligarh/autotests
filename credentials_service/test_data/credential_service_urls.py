cred_service = {
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
        }
    }
}
