# from flaskblog import app
from cloudblog import app


if __name__ == '__main__':
    app.run(debug=False,port=4000)
