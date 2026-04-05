import os
from mergea5toa4 import merge_fixed_rotation
from mergea5toa4 import merge_two_pages

def prepare_papers(number_of_pages):
    pages = number_of_pages
    number_of_papers = int(pages / 4)
    if pages % 4 != 0:
        number_of_papers += 1
    papers = []
    empty_pages = (number_of_papers * 4) - pages
    b = 1
    e = pages + empty_pages
    for page in range(number_of_papers):
        current_paper = {"BL": b, "L": b + 1 , "R": e -1, "BR": e}
        papers.append(current_paper)
        b += 2
        e -= 2
    if empty_pages == 1:
        papers[0]["BR"] = None
    elif empty_pages == 2:
        papers[0]["BR"] = None
        papers[0]["R"] = None
    elif empty_pages == 3:
        papers[0]["BR"] = None
        papers[0]["R"] = None
        if pages == 1:
            papers[0]["L"] = None
        else:
            papers[1]["BR"] = None
    return papers

number_of_pages = 1
while True:
    if not os.path.exists("{}.html".format(number_of_pages)):
        number_of_pages -= 1
        break
    number_of_pages += 1
print(prepare_papers(number_of_pages))
merged = 1
for paper in prepare_papers(number_of_pages):
    merge_fixed_rotation(f"{paper["BR"]}.pdf", f"{paper["BL"]}.pdf", f"{paper["BR"]}{paper["BL"]}.pdf")
    merge_fixed_rotation(f"{paper["L"]}.pdf", f"{paper["R"]}.pdf", f"{paper["L"]}{paper["R"]}.pdf")
    merge_two_pages(f"{paper["BR"]}{paper["BL"]}.pdf",
                    f"{paper["L"]}{paper["R"]}.pdf",
                    f"{paper["BR"]}{paper["BL"]}{paper["L"]}{paper["R"]}.pdf")
    merged += 2
