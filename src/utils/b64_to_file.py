import os
import base64
import uuid


def b64_to_file(b64: str, ext: str, path = 'assets') -> str:
    file_name = '%s.%s' % (str(uuid.uuid4()), ext)
    with open(os.path.join(path, file_name), "wb") as fh:
        fh.write(base64.b64decode(b64))
    return file_name
