# Monosplit

Trying to implement a scenario of splitting a huge "core" into smaller microservices,
that have their own API, data storage, etc.

## Development

Nginx configuration used:
```
server {
    listen 80;
    server_name core.localhost;
    location / {
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   Host      $http_host;
        proxy_pass         http://127.0.0.1:8000;
    }
}

server {
    listen 80;
    server_name microservice.localhost;
    location / {
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   Host      $http_host;
        proxy_pass         http://127.0.0.1:7000;
    }
}
```

Remember to update `/etc/hosts` with relevant lines:
```
127.0.0.1    core.localhost
127.0.0.1    microservice.localhost
```

Launching both services:
```
pip install -r requirements
cd core
./manage.py runserver

# other terminal
cd microservice
./manage.py runserver 0.0.0.0:7000
```

TODO: Dockerize