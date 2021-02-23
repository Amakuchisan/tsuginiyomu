import requests
from urllib.robotparser import RobotFileParser as OriginalRobotFileParser

class RobotFileParser(OriginalRobotFileParser):
    def read(self):
        f = requests.get(self.url, verify=False)
        if f.status_code >= 400 and f.status_code < 500:
            self.allow_all = True
        raw = f.content
        self.parse(raw.decode("utf-8").splitlines())
