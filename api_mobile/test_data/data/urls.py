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
        "client_bio_reg": {
            "method": "post",
            "path": "api/v1/mobile/client-bio-registration"
        },
        "client_sms_reg": {
            "method": "post",
            "path": "api/v1/mobile/client-registration"
        },
        "bio_identification": {
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
        },
        "cards_balances": {
            "path": "api/v2/mobile/cards-balances",
            "method": "post"
        },
        "client_name": {
            "path": "api/v1/mobile/client-name",
            "method": "get"
        },
        "cards_operations": {
            "path": "api/v2/mobile/cards-operations",
            "method": "post"
        }
    },
    "auth": {
        "environment": {
            "all": "https://test-mobilebank.hamkorbank.uz/"
        },
        "refreshtoken": {
            "path": "api/v1/mobile/refresh",
            "method": "post"
        },
        "login": {
            "path": "api/v1/mobile/login",
            "method": "post"
        }
    },
    "settings": {
        "environment": {
            "all": "https://test-mobilebank.hamkorbank.uz/"
        },
        "change_language": {
            "path": "api/v1/mobile/settings/language",
            "method": "put"
        }
    },
    "payment": {
        "environment": {
            "all": "https://test-mobilebank.hamkorbank.uz/"
        },
        "p2p_templates": {
            "path": "api/v1/mobile/payment/p2p-templates",
            "method": "get"
        },
        "p2p_info": {
            "path": "api/v1/mobile/payment/p2p-info/",
            "method": "get"
        },
        "p2p_validate": {
            "path": "api/v1/mobile/payment/p2p-validate",
            "method": "post"
        },
        "p2p_init": {
            "path": "api/v1/mobile/payment/p2p-init",
            "method": "post"
        },
        "p2p_confirm": {
            "path": "api/v1/mobile/payment/p2p-confirm",
            "method": "post"
        }
    }
}
