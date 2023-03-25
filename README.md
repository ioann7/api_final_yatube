### Описание
#### REST API для социальной сети блогеров.
#### Автор
Ioann Chimrov 47 cohort yandex practicum

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов
#### Получение публикаций
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.<br>
```GET /api/v1/posts/```<br>
```Response 200```<br>
```content type: application/json```<br>
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

#### Создание публикации
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.<br>
```POST /api/v1/posts/```<br>
```Payload:```<br>
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
```Response 200```<br>
```content type: application/json```<br>
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

```Response 400```<br>
```content type: application/json```<br>
```json
{
  "text": [
    "Обязательное поле."
  ]
}
```

```Response 401```<br>
```content type: application/json```<br>
```json
{
  "detail": "Учетные данные не были предоставлены."
}
```

#### Более подробную документацию можно получить по адресу `http://localhost/redoc.yaml`, предварительно развернув проект у себя локально.
