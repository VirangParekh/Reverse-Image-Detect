# To Set Up this project locally:

- In the desired folder, git bash the following:
  > > `git clone https://github.com/VirangParekh/Reverse-Image-Detect.git`
- Set up a python virtual environment using the following commands:

```
$ pip install virtualenv
$ python -m venv env
```

- Activate and deactivate using:

```
$ .\env\Scripts\activate
$ deactivate
```

- In the env, install all the requirements using:
  > > `$ pip install -r requirements.txt`

# To run the project

> - Run the migrations if you haven't already using:

> > `$ python manage.py makemigations`
> > OR
> > `$ python manage.py makemigrations AppName`
> > and
> > `$ python manage.py migrate`

> - Run the server using:
>   > `$ python manage.py runserver`
