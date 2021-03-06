import json
import decimal
from decimal import Decimal

# { "nid":0, "time":0, "type": 0, "size":1, "pos":1, "to": -1},
f = open('./org_deemo.json')
chart = json.load(f)
# print(chart)
cchart = {"name": "test", "bpm": 0, "offset": 0, "note": []}
# note_time = []
cchart["bpm"] = int(input("Enter Song BPM:"))
global_offset = 0
# offset = float(input("Enter Global Offset:"))

count = 0
for note in chart["notes"]:
    # print(note["$id"])
    cnote = {"nid": 0, "time": 0, "type": 0, "size": 1, "pos": 1, "to": -1}
    cnote["nid"] = int(note["$id"])
    cnote["type"] = 0
    cnote["pos"] = note["pos"]
    cnote["size"] = round(note["size"], 3)
    cnote["time"] = float(round(Decimal(note["time"]) * Decimal(cchart["bpm"]) / Decimal(240.0), 5)) + global_offset
    cchart["note"].append(cnote)
    # note_time.append(cnote["time"])

for nl in chart["links"]:
    for n in nl["notes"]:
        cchart["note"][int(n["$ref"]) - 1]["type"] = 1

i = 0
print(len(cchart["note"]))
while i < len(cchart["note"]):
    if cchart["note"][i]["pos"] > 2.5:
        del cchart["note"][i]
        i -= 1
    i += 1

i = 1
while i <= len(cchart["note"]):
    cchart["note"][i - 1]["nid"] = i
    cchart["note"][i - 1]["pos"] = round(cchart["note"][i - 1]["pos"] + 2, 4)-(cchart["note"][i - 1]["size"]-1)/2
    i += 1

print(cchart)
print("Success")
with open('./unichart.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(cchart) + '\n')
