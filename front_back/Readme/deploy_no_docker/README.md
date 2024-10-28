### Install Docker on ubuntu

git clone https://github.com/antuanuran/htsoft.git

Короткий способ:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
systemctl start docker
curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker version
docker-compose --version
```

```bash
sudo apt update
sudo apt install python3-venv python3-pip 
```

```bash
docker pull antuanuran/telegram
docker pull antuanuran/onvif
docker pull antuanuran/metadata  
```

1. Переходим в Backend (/srv/deploy_front_backend/backend_deploy/admin_frontend)

2. install dependencies:
```bash
pip install -r requirements.txt
```

3. run:
```bash
python3 manage.py runserver 0.0.0.0:8000
```

***************************
## Deploy - Bacend + Frontend

1. Создаем Удаленный Сервер на рег.ру
2. Клонируем наш Деплой Проект в /srv/  -> https://github.com/antuanuran/htsoft.git
3. Устанавливаем туда Докер, venv и pip (`sudo apt install python3-venv python3-pip`)
4. Устанавливаем nginx (`apt install nginx`) , затем вводим в строке браузера ip – там должна быть приветственная страница
5. Затем заходим в `/etc/nginx/sites-avalible` и видим там default - конфигурацию
6. Копируем этот файл: `cp  default  htsoft.conf`
7. Заходим в него и меняем. Сам файл находится по пути: `/backend_deploy/admin_frontend/nginx.sites_eneble`
8. Затем заходим в `/etc/nginx/sites-enabled` и удаляем default
9. Теперь перезагружаем nginx: `nginx –s reload`

#### На этом Фронт запущен, переходим к Бэкенду

10. Вначале делаем настройку nginx (по аналогии с предыдущим), делаем те же действия, теперь у нас в sites-eneble 2 действующих конфигурационных файла
11. Теперь создаем Демона-Гуникорна. Переходим в путь: `/etc/systemd/system/` и создаем unit-файл. Файл лежит по адресу: `/backend_deploy/admin_frontend/backend_htsoft.service`
12. В этом файле мы прописали путь до загрузочного файла - run.sh. Он уже лежит, надо ему создать права доступа на исполнение: `chmod +x run.sh`
13. Включаем Демона: `systemctl enable backend_htsoft.service`
14. Стартуем: `systemctl start backend_htsoft.service`
15. И проверяем статус: `systemctl status backend_htsoft.service`



# run FAKE-RTSP

```bash
cvlc -I dummy --loop /srv/htsoft/front_back/rtsp_relay/video/gun.mp4 \
:sout=#gather:rtp{sdp=rtsp://:8557/stream} \
:network-caching=500 \
:sout-all \
:sout-keep
```


























