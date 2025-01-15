# Checkbox
REST API for creating and viewing receipts with user registration and authentication.

## Steps to run app

### Clone repository
```[git clone https://github.com/Aleksandra0001/Checkbox.git](https://github.com/Aleksandra0001/checkbox-test-task.git)```

### Create file .env and fill credentials like in file env.example

### Activate Docker

### Run Docker Compose with Postgres DB
```docker-compose up -d```

### Create virtual enviroment
```python -m venv .venv```

### Activate virtual enviroment
#### for macos/linux
```source .venv/bin/activate```
#### for Windows
```.venv\Scripts\activate```

### Install packages from requirements.txt
```pip install -r requirements.txt```

### Run FastApi App
```python main.py```

### Follow next link
```http://localhost:8000/docs```

### Exit and close app
```docker-compose down```



## Run tests
```pytest -v tests```
