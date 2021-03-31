from functools import lru_cache
import yaml
from app.main.utils.config import *


@lru_cache(maxsize=16)
def load_metadata():
    with open(Metadata.METADATA_YAML, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return file
