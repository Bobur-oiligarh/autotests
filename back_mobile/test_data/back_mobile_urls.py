back_mobile_urls = {
    "environment": {
        "all": "https://test-mobilebank.hamkorbank.uz/"
    },
    "registration": {
        "start_reg": {
            "path": "api/v1/mobile/start-registration",
            "method": "post"
        },
        "finish_reg": {
            "path": "api/v1/mobile/finish-registration",
            "method": "post"
        },
        "get_offer": {
            "path": "",
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
        "change_language": {
            "path": "api/v1/mobile/settings/language",
            "method": "put"
        }
    },
    "payment": {
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
    },
    "references": {
        "bankomates": {
            "path": "api/v1/mobile/dict/bankomates",
            "method": "get"
        },
        "branches": {
            "path": "api/v1/mobile/dict/branches",
            "method": "get"
        },
        "languages": {
            "path": "api/v1/mobile/dict/languages",
            "method": "get"
        },
        "operators": {
            "path": "api/v1/mobile/dict/operators",
            "method": "get"
        },
        "exchange-rates": {
            "path": "api/v1/mobile/exchange-rates",
            "method": "get"
        }
    },
    "product": {
        "loans": {
            "path": "api/v1/mobile/product/loans",
            "method": "get"
        },
        "accounts": {
            "path": "api/v1/mobile/product/accounts",
            "method": "get"
        },
        "deposits": {
            "path": "api/v1/mobile/product/deposits",
            "method": "get"
        },
        "store_link": {
            "path": "api/v1/mobile/product/store/1",
            "method": "get"
        }
    }
}
