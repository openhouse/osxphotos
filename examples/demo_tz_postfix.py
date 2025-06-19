import osxphotos
from osxphotos.phototemplate import RenderOptions

PHOTOS_DB = "./tests/Test-16.0.0-beta.photoslibrary/database/photos.db"
UUID = "6F570409-7B94-4D89-AFC6-D04BF11E5EA8"


def main():
    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photo = photosdb.photos(uuid=[UUID])[0]
    template = osxphotos.PhotoTemplate(photo)
    options = RenderOptions()
    fields = [
        "{created}",
        "{created.utc}",
        "{created.local}",
        "{photo.date_added}",
        "{photo.date_added.utc}",
        "{photo.date_modified}",
        "{photo.date_modified.utc}",
    ]
    for f in fields:
        rendered, _ = template.render(f, options)
        print(f"{f} => {rendered[0]}")


if __name__ == "__main__":
    main()
