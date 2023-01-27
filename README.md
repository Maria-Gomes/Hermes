# Hermes
Provides company phone numbers and manages plans for different users. To run the project first use

```pip install -r requirements.txt```

to install the necessary packages from the ```requirements.txt``` file.

Use the following commands to run the server:

1. ```python manage.py makemigrations```
2. ```python manage.py migrate```
3. ```python manage.py runserver```

In a separate terminal run the following command

```python manage.py qcluster```

to create a cluster and schedule the task queue.

