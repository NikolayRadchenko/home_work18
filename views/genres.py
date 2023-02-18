from flask import request
from flask_restx import Resource, Namespace

from implemented import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    # def post(self):
    #     req_json = request.json
    #     genre_service.create(req_json)
    #     return "", 201


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid: int):
        try:
            one_genre = genre_service.get_one(gid)
            return genre_schema.dump(one_genre), 200
        except Exception as e:
            return e, 404

    # def put(self, gid: int):
    #     req_json = request.json
    #     req_json["id"] = gid
    #
    #     genre_service.update(req_json)
    #
    #     return "", 204
    #
    # def patch(self, gid: int):
    #     req_json = request.json
    #     req_json["id"] = gid
    #
    #     genre_service.update_partial(req_json)
    #
    #     return "", 204
    #
    # def delete(self, gid: int):
    #     genre_service.delete(gid)
    #
    #     return "", 204
