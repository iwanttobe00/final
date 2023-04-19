# YaMDb API
![Python version](https://img.shields.io/badge/python-3.7-yellow) 
![Django version](https://img.shields.io/badge/django-2.2-orange) 
![workflow status](https://github.com/AleksandrUsolcev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

YaMDb API - демо: [main](http://yamdb-usolcev.ddns.net/api/v1/) | [redoc](http://yamdb-usolcev.ddns.net/redoc/)

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).
Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список
категорий (Category) может быть расширен администратором.

В каждой категории есть произведения: книги, фильмы или музыка. 

Произведению может быть присвоен жанр (Genre) из списка предустановленных (
например, "Сказка", "Рок" или "Артхаус"). Новые жанры может создавать только
администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые
отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (
целое число); из пользовательских оценок формируется усреднённая оценка
произведения — рейтинг (целое число). На одно произведение пользователь может
оставить только один отзыв.

## Технологии

- Python 3.7+
- [django](https://github.com/django/django) 2.2.16
- [django-rest-framework](https://github.com/encode/django-rest-framework)
  3.12.4
- [Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt) 5.2.0

## Запуск проекта

Клонировать репозиторий и перейти в корень проекта

```bash
git clone https://github.com/AleksandrUsolcev/infra_sp2.git
cd infra_sp2
``` 

Создать файл переменного окружения и заполнить по [образцу](/infra/example.env)

```bash
cd infra/
nano .env
``` 

Развернуть docker контейнер

```
docker-compose up -d --build 
``` 

Выполнить миграции, создать суперпользователя, собрать статику

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

Загрузить тестовый [дамп](/infra/fixtures.json) базы данных*

```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

<em>*опционально для выполнения. Помимо тестовых данных, дамп включает в себя уже созданного суперпользователя **admin** с паролем **admin12345**</em>

## Получение персонального токена

Для взаимодействия с API необходимо завести учетную запись пользователя,
или суперпользователя и иметь персональный токен, для чего необходимо
перейти по адресу .../api/v1/auth/signup/ и отправить POST запрос с
именем и адресом электронной почты пользователя

```
{
    "username": "example_name",
    "email": "example_email"
}
``` 

После успешной регистрации на указаный email придет секретный код, который
необходимо скопировать в поле "confirmation_code" по адресу ...
/api/v1/auth/token/ и получить персональный токен

```
{
    "username": "example_name",
    "confirmation_code": "your_code"
}
``` 

Далее передаем полученный токен в headers

```
KEY: Authorization
VALUE: Bearer <ваш токен>
``` 

## Примеры запросов

**Список запросов можно посмотреть перейдя на .../redoc/
развернутого проекта**

## Автор проекта

[Александр Усольцев](https://github.com/AleksandrUsolcev)
