import re
import subprocess

filePath = "Genshin Impact game/GenshinImpact_Data/webCaches/2.36.0.0/Cache/Cache_Data/data_2"
pattern = r"https://gs\.hoyoverse\.com/genshin/event/e20190909gacha-v3/.*?&game_biz=hk4e_global"

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
