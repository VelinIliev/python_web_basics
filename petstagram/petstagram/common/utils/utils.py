from petstagram.common.models import Like


def get_user_liked_photo(photo_id):
    photo_likes = Like.objects.filter(to_photo_id=photo_id)
    return photo_likes


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def apply_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo
