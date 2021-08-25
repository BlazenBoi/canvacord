import aiohttp
import requests
import asyncio
import json
try:
    from packaging.version import parse
except ImportError:
    print("\n Started Installing required Canvacord Package")
    from pip._vendor.packaging.version import parse
    print("\n Finished Installing required Canvacord Package")

thisversion = "0.2.74"

async def checkversion():
        url_pattern = 'https://pypi.python.org/pypi/canvacord/json'
        req = requests.get(url_pattern)
        version = parse('0')
        try:
            if version != None:
                j = json.loads(req.text.encode("utf-8"))
                releases = j.get('releases', [])
                for release in releases:
                    ver = parse(release)
                    if not ver.is_prerelease:
                        version = max(version, ver)
                if str(version) == (thisversion):
                    pass
                else:
                    if parse(str(thisversion)) < parse(str(version)):
                        print(f"Canvacord is on Version {version} but you are only on Version {thisversion} Please Update for all the newest bug fixes and features!")
                    else:
                        pass
        except Exception as e:
            print(e)
            pass