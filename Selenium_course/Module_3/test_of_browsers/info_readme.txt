Тест можно запускать как и командой "pytest --language=es test_items.py" (по дефолту тест будет открыт
в браузере Google Chrome, так и командой "pytest --browser_name=firefox --language=es test_items.py" (здесь браузер
на выбор: Google Chrome или Mozilla Firefox).
Для полнового вывода можно выполнить команду с ключами: "pytest -s -v --browser_name=chrome --language=es test_items.py"