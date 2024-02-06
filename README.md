<a href="https://wakatime.com/badge/user/018c3f04-b140-41f9-a489-5b0143d153f5/project/018d7949-eafa-4bae-a8f7-2bc61e39e0fc"><img src="https://wakatime.com/badge/user/018c3f04-b140-41f9-a489-5b0143d153f5/project/018d7949-eafa-4bae-a8f7-2bc61e39e0fc.svg" alt="wakatime"></a>
# Система авторизации и регистрации
## 1. Консольные команды

#### 1) Запуск контейнера

```Shell
sudo docker-compose up -d --build # --force-recreate 
```

#### 2) Остановка контейнера

```Shell
sudo docker-compose down -v
```

#### 3) Посмотреть логи

```Shell
sudo docker-compose logs -f
```

#### 4) Создать миграции

```Shell
docker-compose exec web python manage.py makemigrations --noinput
```

#### 5) Удалить все образы, сети, волюмы

```Shell
docker rm $(docker stop $(docker ps -aq)) 
docker system prune --volumes --all 
```
#### 5) Загрузить файл с переменными окружения
```Shell
env $(cat ../sqlite3.env | xargs) python3 manage.py createsuperuser
source ../sqlite3.env && python3 manage.py createsuperuser
```