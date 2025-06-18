import datetime
import osxphotos
from osxphotos.phototemplate import RenderOptions

PHOTOS_DB = "./tests/Test-16.0.0-beta.photoslibrary/database/photos.db"
UUID = "6F570409-7B94-4D89-AFC6-D04BF11E5EA8"


def test_utc_local_postfix():
    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photo = photosdb.photos(uuid=[UUID])[0]
    template = osxphotos.PhotoTemplate(photo)
    options = RenderOptions()
    dt_utc = photo.date.astimezone(datetime.timezone.utc)
    rendered, _ = template.render("{created.utc.strftime,%Y-%m-%dT%H:%M:%S%z}", options)
    assert rendered[0] == dt_utc.strftime("%Y-%m-%dT%H:%M:%S%z")
    dt_local = photo.date.astimezone()
    rendered, _ = template.render("{created.local.strftime,%Y-%m-%dT%H:%M:%S%z}", options)
    assert rendered[0] == dt_local.strftime("%Y-%m-%dT%H:%M:%S%z")


def test_nested_date_tz_postfix():
    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photo = photosdb.photos(uuid=[UUID])[0]
    template = osxphotos.PhotoTemplate(photo)
    options = RenderOptions()
    dt_utc = photo.date_added.astimezone(datetime.timezone.utc)
    rendered, _ = template.render("{photo.date_added.utc.strftime,%Y-%m-%dT%H:%M:%S%z}", options)
    assert rendered[0] == dt_utc.strftime("%Y-%m-%dT%H:%M:%S%z")
    rendered, _ = template.render("{photo.date_added.utc.year}", options)
    assert rendered[0] == dt_utc.strftime("%Y")
    dt_local = photo.date_added.astimezone()
    rendered, _ = template.render("{photo.date_added.local.strftime,%Y-%m-%dT%H:%M:%S%z}", options)
    assert rendered[0] == dt_local.strftime("%Y-%m-%dT%H:%M:%S%z")
    rendered, _ = template.render("{photo.date_added.local.year}", options)
    assert rendered[0] == dt_local.strftime("%Y")


def test_utc_no_subfield_same_as_default():
    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photo = photosdb.photos(uuid=[UUID])[0]
    template = osxphotos.PhotoTemplate(photo)
    options = RenderOptions()
    rendered_default, _ = template.render("{created}", options)
    rendered_utc, _ = template.render("{created.utc}", options)
    assert rendered_default[0] == rendered_utc[0]
