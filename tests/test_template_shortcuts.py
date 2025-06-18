import datetime
import osxphotos
from osxphotos.phototemplate import RenderOptions

PHOTOS_DB = "./tests/Test-16.0.0-beta.photoslibrary/database/photos.db"
UUID = "6F570409-7B94-4D89-AFC6-D04BF11E5EA8"


def test_nested_date_shortcuts():
    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photo = photosdb.photos(uuid=[UUID])[0]
    template = osxphotos.PhotoTemplate(photo)
    options = RenderOptions()
    rendered, _ = template.render("{photo.date_added.year}", options)
    assert rendered[0] == "2025"
    rendered, _ = template.render("{photo.date_added.yy}", options)
    assert rendered[0] == "25"
    rendered, _ = template.render("{photo.date_added.strftime,%Y-%m-%d}", options)
    assert rendered[0] == "2025-06-11"
