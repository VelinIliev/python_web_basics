from gamesplay_app.auth_app.models import Profile


def get_user():
    user = Profile.objects.count()
    if user == 0:
        return False
    else:
        return True
