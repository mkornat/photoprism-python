# Photoprism Python API Client

## Installation

```bash
pip install photoprism
```

## Usage

```python
import asyncio
from pathlib import Path

from photoprism import PhotoprismSession, PhotoprismClient
from photoprism.models.query import Size


async def main():
    session = PhotoprismSession(
        username="username",
        password="password",
        host="localhost",
        protocol="http",
    )
    client = PhotoprismClient(session)
    
    albums = await client.albums.filter(count=3, q="cats")
    for album in albums:
        image_path = await client.albums.download_cover_image(
            album_uid=album.uid,
            size=Size.Tile50,
            file_dir=Path("data/album_covers"),
        )
        print(image_path)

        
if __name__ == '__main__':
    asyncio.run(main())

```
