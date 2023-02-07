# abocados 🥑

## 💻 Run with docker-compose

1 - Clone the project on your computer:

```sh
git clone https://github.com/susmaycan/abocados-docker.git
```

2 - Build the project:

```sh
make build
```

**Note: You need docker, docker-compose to be installed**

3 - Run the project:

```sh
make run
```

4 - Migrate Django database and load data

```sh
make setup_database
```

5 - Open in the browser:

Front-end: [http://localhost](http://localhost)

Back-end: [http://localhost:3003/](http://localhost:3003/)

Django admin: [http://localhost:3003/admin](http://localhost:3003/admin)

## 👤 User credentials

```sh
email: phoebe_buffay@friends.com
password: ab0cad0s
```

## 🧪 Tests

To run the API tests:

```sh
make test
```
