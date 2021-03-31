class Metadata:
    METADATA_YAML = 'managed-object-index.yaml'


class BaconIpsumMeta:
    API_URL = 'https://baconipsum.com/api/'
    TYPE = "type"
    SENTENSES = "sentences"
    TYPE_VALUES = {"all-meat": None, "meat-and-filler": None}


class Messages:
    WRONG_PARAMETER_MSG = "Invalid type value. Choose between <all-meat> and <meat-and-filler>"
    KEY_ERROR_MESSAGE = "is not a valid query parameter value"
