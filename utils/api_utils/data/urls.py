urls = {
    "registration": {
        "environment": {
            "all": "https://test-mobilebank.hamkorbank.uz/"
        },
        "start_reg": {
            "path": "api/v1/mobile/start-registration",
            "method": "post"
        },
        "finish_reg": {
            "path": "api/v1/mobile/finish-registration",
            "method": "post"
        },
        "get_offer": {
            "path": "api/v1/mobile/registration-offer",
            "method": "get"
        },
        "agree_offer": {
            "path": "api/v1/mobile/registration-offer",
            "method": "put"
        },
        "check_client_reg": {
            "method": "post",
            "path": "api/v1/mobile/check-client-registration"
        }
    }
}
