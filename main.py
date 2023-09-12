from playstore_validator import validate_playstore
from downloads_validator import validate_downloads

if __name__ == '__main__':

    playstore_path = 'samples/playstore.jsonl'
    validate_playstore(playstore_path)

    downloads_path = 'samples/downloads.json'
    validate_downloads(downloads_path)
