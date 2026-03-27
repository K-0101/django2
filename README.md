# Django Blog

Простой блог на Django с возможностью добавления статей через админку.

## Возможности
- добавление статей
- загрузка изображений
- автор поста
- дата публикации
- категории для статей
- вывод статей на главной странице

## Технологии
- Python
- Django
- SQLite
- HTML
- CSS

## Установка
```bash
git clone <repo_url>
cd django2
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver