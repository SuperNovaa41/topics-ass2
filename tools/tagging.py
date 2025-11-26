from urllib.request import urlopen
from pathlib import Path


def get_date() -> str:
    res = urlopen("http://just-the-time.appspot.com/")

    result = res.read().strip()
    result_str = result.decode("utf-8").split(" ")[0]

    return result_str


def increment_ver(inc: str) -> str:
    if not Path("current_version").exists():
        with open("current_version", "w") as file:
            file.write("0.0.0")

    with open("current_version", "r") as file:
        v = file.read()

    vers = v.split(".")

    print(vers)

    if inc == "major":
        vers[0] = str(int(vers[0]) + 1)
    elif inc == "minor":
        vers[1] = str(int(vers[1]) + 1)
    else:
        vers[2] = str(int(vers[2]) + 1)
    print(vers)

    v_str = f"{vers[0]}.{vers[1]}.{vers[2]}"
    with open("current_version", "w") as file:
        file.write(v_str)
    print(v_str)

    return v_str


class tagger:
    def __init__(self):
        pass

    def tag(self, title: str, inc: str) -> str:
        title = title.replace("{{version}}", increment_ver(inc))
        title = title.replace("{{date}}", get_date())

        return title
