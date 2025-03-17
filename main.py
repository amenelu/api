from flask import Flask
from flask_restful import Api, Resource

app=Flask(__name__)
api=Api(app)

if__name__=="__main__": # type: ignore
app.run(debug=True)
