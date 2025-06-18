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
