# HamkorAutoTests

Для запуска автотестов необходимо:
1) Установить зависимости: pip install -r requirements.txt
2) В терминале ввести команду python -m pytest ./path/to/test/cases.py --alluredir ./path/to/results:
   {"back_mobile": python -m pytest ./back_mobile/tests/test_cases/cases.py --alluredir ./back_mobile/results -v,
    "card_service": python -m pytest ./card_services/tests/test_cases/cases.py --alluredir ./card_service/results -v,
    "iabs_service": python -m pytest ./iabs_client_service/tests/test_cases/search_clients_cases.py --alluredir ./iabs_client_service/results -v,
   }


