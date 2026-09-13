from flask import jsonify, request
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"id": "123", "title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"id": "456", "title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"id": "789", "title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            return jsonify({"movies": [movie for movie in movies.values()]})

        movie = movies.get(str(movie_id))
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404

        return jsonify({"movie": movie})

    def post(self):
        payload = request.get_json(silent=True) or {}
        title = payload.get("title")
        description = payload.get("description")

        if not title:
            return jsonify({"error": "Movie title is required"}), 400

        next_id = str(len(movies) + 1)
        movie = {"id": next_id, "title": title, "description": description or ""}
        movies[next_id] = movie
        return jsonify({"movie": movie}), 201

    def put(self, movie_id):
        movie = movies.get(str(movie_id))
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404

        payload = request.get_json(silent=True) or {}
        if "title" in payload:
            movie["title"] = payload["title"]
        if "description" in payload:
            movie["description"] = payload["description"]

        return jsonify({"movie": movie})

    def delete(self, movie_id):
        movie = movies.pop(str(movie_id), None)
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404

        return jsonify({"message": "Movie deleted", "movie": movie})
