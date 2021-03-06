import json


def write(s):
    with open('ctody.xml', 'a+', encoding='utf-8') as file:
        file.write(s + '\n')


head = """<?xml version="1.0" encoding="UTF-8" ?>
<CMap xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">"""
ctype = """<m_leftRegion>PAD</m_leftRegion>
<m_rightRegion>PAD</m_rightRegion>
"""
end = """<m_notesLeft>
<m_notes></m_notes>
</m_notesLeft>
<m_notesRight>
<m_notes></m_notes>
</m_notesRight>
</CMap>"""
samenote = """<m_subId>-1</m_subId>
<status>Perfect</status>
</CMapNoteAsset>
"""

with open('ctody.xml', 'w', encoding='utf-8') as f:
    f.write('')

cchart = json.load(open("./unichart.json"))
write(head)
write(f'<m_path>{cchart["name"]}</m_path>')
write(f'<m_barPerMin>{cchart["bpm"] / 4}</m_barPerMin>')
write(f'<m_timeOffset>{cchart["offset"]}</m_timeOffset>')
write(ctype)
write(f'<m_mapID>_map_{cchart["name"]}_M</m_mapID>')

write("<m_notes>")
write("<m_notes>")
schart = ""
for note in cchart["note"]:
    s1 = f'<CMapNoteAsset>\n<m_id>{note["nid"] - 1}</m_id>\n<m_type>{"NORMAL" if note["type"] == 0 else "CHAIN"}</m_type'
    s2 = f'>\n<m_time>{note["time"]}</m_time>\n<m_position>{note["pos"]}</m_position>\n<m_'
    s3 = f'width>{note["size"]}</m_width>\n' + samenote
    schart += s1 + s2 + s3
write(schart)
write("</m_notes>")
write("</m_notes>")
write(end)
