## CRUD для Yatube

Яндекс Практикум. Спринт 8. Итоговый проект. CRUD для Yatube.

## Описание

CRUD для проекта социальной сети Yatube.

Технологии:
- Python
- Django
- Pytest
- Postman

## Функционал

- Реализован REST API для сервиса публикации постов, Yatube;
- Аутентификация по JWT-токену;
- Работает со всеми модулями Yatube: постами, комментариями, группами и подписчиками.
- Поддерживает методы GET, POST, PUT, PATCH, DELETE;
- Предоставляет данные в формате JSON.

## Установка

1. Клонировать репозиторий:

   ```
   git clone https://github.com/xxyvxx/api_yatube.git
   ```

2. Перейти в папку с проектом:

   ```
   cd api_yatube/
   ```

3. Установить виртуальное окружение для проекта:

   ```
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```
   cd yatube
   python manage.py makemigrations
   python manage.py migrate
   ```


