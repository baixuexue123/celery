import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from celery import Celery


app = Celery('myapp')

app.config_from_object('celeryconfig')


@app.task(name='add')
def add(x, y):
    return x + y


if __name__ == '__main__':
    app.start()


# $ celery -A myapp worker -l info
# $ celery -A myapp worker --loglevel=info

# $ ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
# $ celery -A dts beat -l info
