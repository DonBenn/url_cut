## Проект укорачивания ссылок

### Описание 
Данный проект помогает генерировать или создать вашу собственную короткую ссылку любого URL-адреса.
После создания, короткая ссылка перенаправляет на начальную длинную ссылку

### Используемые технологии:

* Flask, Jinja2, SQL-Alchemy, Flask-WTF, Python

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:DonBenn/url_cut.git
```

```
cd url_cut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте файл .evn:
```
touch .evn
```

В файле `.evn` Создайте переменные указанные в файле `env.example`


**Команды для создания и инициализации бд:**

* Создание базы данных
```
flask db init
```

* Создание миграций
```
 flask db migrate -m "add models"
```

* Применение миграций
```
flask db upgrade 
```

* Команда для запуска:

```
flask run
```


### Автор

Bessonov Denis (https://github.com/DonBenn)
