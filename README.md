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