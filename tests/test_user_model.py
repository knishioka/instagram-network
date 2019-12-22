from instagram_network.models import UserModel


def test_answer():
    assert UserModel.collection == 'users'
