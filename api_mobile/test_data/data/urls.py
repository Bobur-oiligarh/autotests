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
        },
        "client-bio-reg": {
            "method": "post",
            "path": "api/v1/mobile/client-bio-registration"
        },
        "client-sms-reg": {
            "method": "post",
            "path": "api/v1/mobile/client-registration"
        },
        "bio-identification": {
            "method": "post",
            "path": "api/v1/mobile/bio-identification"
        }
    },
    "main_page": {
        "environment": {
            "all": "https://test-mobilebank.hamkorbank.uz/"
        },
        "client_cards": {
            "path": "api/v1/mobile/client-cards",
            "method": "get"
        }
    }
}
