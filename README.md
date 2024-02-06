<a href="https://wakatime.com/badge/user/018c3f04-b140-41f9-a489-5b0143d153f5/project/018d7949-eafa-4bae-a8f7-2bc61e39e0fc"><img src="https://wakatime.com/badge/user/018c3f04-b140-41f9-a489-5b0143d153f5/project/018d7949-eafa-4bae-a8f7-2bc61e39e0fc.svg" alt="wakatime"></a>

# Система авторизации и регистрации

<ul>
<li><strong>Django 5</strong></li>
<li><strong>Postgres</strong></li>
<li><strong>Sqlite 3</strong></li>
</ul>

## 1. Файлы переменного окружения

### 1) sqlite.env

```Shell
DEBUG=1 # Включить или выключить режим отладки

SECRET_KEY='test' # Токен для шифрования паролей 

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] # Доступные хосты

EMAIL_HOST_USER = "test@yandex.ru" # Почта с которой будут приходить письма о сбросе пароля

EMAIL_HOST_PASSWORD = "test" # Токен от этой почты
```   

### 2) postgres.env

```Shell
DEBUG=1 # Включить или выключить режим отладки

SECRET_KEY='test' # Токен для шифрования паролей 

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] # Доступные хосты

EMAIL_HOST_USER = "test@yandex.ru" # Почта с которой будут приходить письма о сбросе пароля

EMAIL_HOST_PASSWORD = "test" # Токен от этой почты

SQL_ENGINE=django.db.backends.postgresql # Бэкенд postgres

SQL_DATABASE=test # Имя таблицы

SQL_USER=test # Логин от postgres

SQL_PASSWORD=test # Пароль от postgres

SQL_HOST=db # Хост от postgres

SQL_PORT=5432 # Порт от postgres

DATABASE=postgres
```   

## 2. Консольные команды

### 1) Запуск контейнера

```Shell
sudo docker-compose up -d --build # --force-recreate 
```

### 2) Остановка контейнера

```Shell
sudo docker-compose down -v
```

### 3) Посмотреть логи

```Shell
sudo docker-compose logs -f
```

### 4) Создать миграции

```Shell
docker-compose exec web python manage.py makemigrations --noinput
```

### 5) Удалить все образы, сети, волюмы

```Shell
docker rm $(docker stop $(docker ps -aq)) 
docker system prune --volumes --all 
```

### 6) Загрузить файл с переменными окружения

```Shell
env $(cat ../sqlite3.env | xargs) python3 manage.py createsuperuser
source ../sqlite3.env && python3 manage.py createsuperuser
```