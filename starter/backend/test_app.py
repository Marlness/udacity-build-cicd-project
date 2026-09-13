from . import app


def test_root_endpoint_returns_200():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.is_json


def test_movies_endpoint_returns_200():
    with app.test_client() as client:
        response = client.get("/movies")
        assert response.status_code == 200
        assert response.is_json


def test_movies_endpoint_returns_json():
    with app.test_client() as client:
        response = client.get("/movies")
        assert response.content_type == "application/json"


def test_movies_endpoint_returns_valid_data():
    with app.test_client() as client:
        response = client.get("/movies")
        data = response.get_json()
        assert isinstance(data, dict)
        assert "movies" in data
        assert isinstance(data.get("movies"), list)
        assert len(data["movies"]) > 0
        assert "title" in data["movies"][0]


def test_movie_detail_endpoint_returns_200():
    with app.test_client() as client:
        response = client.get("/movies/123")
        assert response.status_code == 200
        data = response.get_json()
        assert "movie" in data
        assert data["movie"]["title"] == "Top Gun: Maverick"


def test_movie_create_update_and_delete_flow():
    with app.test_client() as client:
        create_response = client.post(
            "/movies",
            json={"title": "Interstellar", "description": "Space travel"},
        )
        assert create_response.status_code == 201
        created_movie = create_response.get_json()["movie"]
        created_id = str(created_movie["id"])

        update_response = client.put(
            f"/movies/{created_id}",
            json={"title": "Interstellar Updated", "description": "Deep space"},
        )
        assert update_response.status_code == 200
        assert update_response.get_json()["movie"]["title"] == "Interstellar Updated"

        delete_response = client.delete(f"/movies/{created_id}")
        assert delete_response.status_code == 200
