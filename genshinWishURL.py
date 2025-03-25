import re
import subprocess

file_path = "/datadisk/Games/Genshin Impact game/GenshinImpact_Data/webCaches/2.34.0.0/Cache/Cache_Data/data_2"
pattern = r"https://gs\.hoyoverse\.com/genshin/event/e20190909gacha-v3/.*?&game_biz=hk4e_global"

def getLastMatchURL(file_path, pattern):
    last_match = None
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            matches = re.findall(pattern, line)
            if matches:
                last_match = matches[-1]
    return last_match

last_url = getLastMatchURL(file_path, pattern)

if last_url:
    subprocess.run(["xclip", "-selection", "clipboard"], input=last_url.encode(), check=True)
    print("Copied to clipboard:", last_url)
else:
    print("No matching URL found.")
