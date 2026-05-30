# 🤖 Automation Python

Учебный проект по автоматизации на Python. Пять модулей: API, БД, тесты, окружение, CI/CD.

## 📁 Структура

- `JsonPlaceholder_Api/` — тесты REST API
- `Working_With_Pytest/` — автотесты с pytest
- `SQL_with_Python/` — работа с БД (требуется локальный `.env`)
- `Dotenv/` — пример использования переменных окружения
- `.github/workflows/` — GitHub Actions

## 🚀 Запуск

```bash
git clone https://github.com/Waspish/automation-python.git
cd automation-python
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Примеры команд

| Модуль              | Команда                                             |
|---------------------|-----------------------------------------------------|
| JsonPlaceholder_Api | `python test_api.py`                                |
| Working_With_Pytest | `pytest -v`                                         |
| SQL_with_Python     | `python sql_examples.py` (требует настройки `.env`) |

## ⚠️ Важно для SQL модуля

Пароль к базе данных хранится в `.env` файле, который **не включён в репозиторий**.  
Чтобы запустить `SQL_with_Python`, создайте файл `.env` в корне проекта со следующим содержимым:

```
DB_PASSWD="AVNS_tegPDkI5BlB2lW5eASC"
```

## 🛠 Технологии

Python, pytest, requests, SQLite/PostgreSQL, GitHub Actions, python-dotenv