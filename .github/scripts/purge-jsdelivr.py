from json import load
from os.path import isfile
from requests import Session
from time import sleep

GH_REPO = "PRO-2684/pURLfy-rules"
x = Session()


def _purge(file):
    url = f"https://purge.jsdelivr.net/gh/{GH_REPO}@core-0.3.x/{file}"
    print(f'Purging "{url}"...')
    r = x.get(url)
    if r.status_code != 200:
        print(
            f"Unexpected status code: {r.status_code}, response: {r.text}"
        )
    elif r.json()["status"] != "finished":
        print(f"Failed to purge! Response: {r.text}")
    else:
        print("✅ Purged!")


def purge(name):
    json_path = f"{name}.json"
    min_path = f"{name}.min.json"
    if isfile(json_path):
        _purge(json_path)
    if isfile(min_path):
        _purge(min_path)


if __name__ == "__main__":
    with open("./list.json", "r") as f:
        names = load(f)
    for name in names:
        purge(name)
        sleep(1)
    purge("list")
    print("🎉 Done!")
