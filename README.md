# Проект приложение QRKot
### Описание
Приложение для Благотворительного фонда поддержки котиков. Реализовано на базе фреймворка FastAPI.
### Как запустить
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AlexanderKuryatnikov/cat_charity_fund.git
cd cat_charity_fund
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
3. Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Создать файл .env и ввести переменные окружения:
  - APP_TITLE=Ваше название
  - APP_DESCRIPTION=Ваше Описание
  - DB_URL=sqlite+aiosqlite:///./fastapi.db
  - SECRET=Ваше секретное слово
5. Запустить проект:
```
uvicorn app.main:app --reload
```
### Автор
Александр Курятников
