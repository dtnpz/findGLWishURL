import re
import subprocess
from pathlib import Path

webCachesPath = Path(
    "/datadisk/Games/Genshin Impact game/GenshinImpact_Data/webCaches"
)


def getLatestCacheFile(webCachesPath):
    cacheFiles = []
    for cacheFolder in webCachesPath.iterdir():
        if not cacheFolder.is_dir() or not re.fullmatch(
            r"\d+(?:\.\d+)+", cacheFolder.name
        ):
            continue

        cacheFile = cacheFolder / "Cache" / "Cache_Data" / "data_2"
        if cacheFile.is_file():
            version = tuple(int(part) for part in cacheFolder.name.split("."))
            cacheFiles.append((version, cacheFile))

    if not cacheFiles:
        raise FileNotFoundError(
            f"No Genshin web cache data_2 file found in {webCachesPath}"
        )

    return max(cacheFiles, key=lambda item: item[0])[1]


filePath = getLatestCacheFile(webCachesPath)
pattern = r"https://gs\.hoyoverse\.com/genshin/event/e20190909gacha[^/]*/.*?&game_biz=hk4e_global"
def getLastMatchURL(filePath, pattern):
    lastMatch = None
    with open(filePath, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            matches = re.findall(pattern, line)
            if matches:
                lastMatch = matches[-1]
    return lastMatch

lastURL = getLastMatchURL(filePath, pattern)

if lastURL:
    subprocess.run(["xclip", "-selection", "clipboard"], input=lastURL.encode(), check=True)
    print("Copied to clipboard:", lastURL)
else:
    print("No matching URL found.")
