from flask import Flask
from flask_restful import Api, Resource, reqparse,abort

app = Flask(__name__)
api = Api(app)

Video_put_args = reqparse.RequestParser()
Video_put_args.add_argument("name", type=str, help="name of video"),required=True
Video_put_args.add_argument("views", type=int, help="view of video",required=True)
Video_put_args.add_argument("likes", type=int, help="likes of video",required=True)

videos = {}

def if_id_not_found(video_id):
    if video_id not in videos:
        abort(404,message='id not found')


class Video(Resource):
    def get(self, video_id):
        if_id_not_found(video_id)
        return videos[video_id]

    def put(self, video_id):
        args=Video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
