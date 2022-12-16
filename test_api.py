import pytest as pytest

from app import app


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def post_keys():
    return {"poster_name", "poster_avatar", "pic",
            "content", "views_count", "likes_count",
            "pk"}

def test_api_posts(client, post_keys):
    resp = client.get('api/posts/')
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for i in resp.json():
        assert isinstance(i.json, dict)
        assert set(i.keys()) == post_keys

def test_api_post(client, post_keys):
    resp = client.get('api/post/1/')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert set(resp.json.keys()) == post_keys