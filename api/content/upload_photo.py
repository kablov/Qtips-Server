import cloudinary.uploader


def upload_photo(photo, phone):
    path = "profile/" + str(phone)
    cloudinary_photo = cloudinary.uploader.upload_resource(photo, public_id=path)
    url = cloudinary_photo.url
    secure_url = str(url).replace("http", "https")
    return secure_url
