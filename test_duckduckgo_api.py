import requests
import pytest

presidents = ["Lincoln", "Johnson", "Trump", "Jefferson", "Washington", "Arthur", "Roosevelt", "Bush", "Clinton",
              "Jackson", "Kennedy", "Reagan", "Obama", "Monroe", "Tyler", "Buchanan", "Garfield",
              "Harding", "Ford", "Taft", "Hoover", "Nixon", "Cleveland", "Wilson", "Eisenhower",
              "Pierce", "Johnson", "Roosevelt", "Coolidge", "Carter", "Fillmore", "Truman", "Hayes", "Harrison",
              "Polk", "Taylor", "Grant", "Adams", "McKinley", "Buren", "Harrison", "Madison"]
url_ddg = "https://api.duckduckgo.com"


def test_ddg_presidents():
    resp = requests.get(url_ddg + "/?q=Presidents%20of%20the%20United%20States&format=json")
    rsp_data = resp.json()
    body_content = ""
    for item in rsp_data["RelatedTopics"]:
        body_content += item["Result"]
    all_presidents_present = True
    for president in presidents:
        if president not in body_content:
            all_presidents_present = False
    assert all_presidents_present

