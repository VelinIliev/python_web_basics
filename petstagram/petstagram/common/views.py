import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.models import Like
from petstagram.photos.models import Photo
from petstagram.common.utils.utils import get_user_liked_photo, get_photo_url, apply_likes_count, apply_user_liked_photo


def index(request):
    photos = Photo.objects.all()
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photo(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        Like.objects.create(to_photo_id=photo_id)

    redirect_path = get_photo_url(request, photo_id)
    return redirect(redirect_path)
    # или
    # photo_like = Like(photo_id)
    # photo_like.save()


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={'pk': photo_id})
    pyperclip.copy(f'http://127.0.0.1:8000{photo_details_url}')
    return redirect(get_photo_url(request, photo_id))
