
This prisma python project is loosly based on documentation and

# Prisma FastApi

[![CI](https://github.com/prisma-korea/prisma-fastapi/actions/workflows/main.yml/badge.svg)](https://github.com/prisma-korea/prisma-fastapi/actions/workflows/main.yml)


## Install requirement

```pip```

```python3```

```docker-compose```

```docker```

```pip install prisma```

```pip install fastapi```

```pip install uvicorn```

## Generate Prisma Client

```sh
prisma generate
```

## Start postgres as docker

```sh
uvicorn main:app --reload
```

## Start postgres

```sh
docker-compose up -d
```

## Push updates in schema to postgres db

```sh
prisma db push
```

## Try the api commands at local

```sh
localhost:3000/docs
```


## Close down postgres to avoid port bind

```sh
docker-compose dowm
```