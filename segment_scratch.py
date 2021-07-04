import json
import requests
from xml.etree import ElementTree as ET
import pandas as pd


def fetch_grobid_structure(pdf_file: str, grobid_host: str = "http://localhost:8072", 
fetch_headers_only=False):
    files = {
        "input": (pdf_file, open(pdf_file, "rb"), "application/pdf", {"Expires": "0"})
    }
    if fetch_headers_only:
        url = "{}/api/processHeaderDocument".format(grobid_host)
    else:
        # url = "{}/api/processPdfStructure".format(grobid_host)
        url = "{}/api/processFulltextDocument".format(grobid_host)

    resp = requests.post(url, files=files)

    if resp.status_code == 200:
        return resp.text
    else:
        print(resp.reason)
        raise Exception("Grobid returned status code {}".format(resp.status_code))

# Get Grobid processed file
path = r'C:\Users\henzh\Downloads\CUAD_v1\CUAD_v1\full_contract_pdf\Part_I\Joint Venture\\'
filename = r'VALENCETECHNOLOGYINC_02_14_2003-EX-10-JOINT VENTURE CONTRACT.pdf'

text = fetch_grobid_structure(path+filename)
text = text.encode()
with open("test.xml", "wb") as f:
    f.write(text)

# Read from XML
tree = ET.parse('test.xml')

elemList = []

for elem in tree.iter():
    elemList.append(elem.tag)

# now I remove duplicities - by convertion to set and back to list
elemList = list(set(elemList))

# Just printing out the result
print(elemList)
iterate = tree.iter()
segment_df = pd.DataFrame(columns=['Header', 'Para'])

for item in iterate:
    # tag=''
    # Find headers, then find paragraph
    if item.tag == '{http://www.tei-c.org/ns/1.0}head':
        header = item.text
        para = None

        next_item = next(iterate)
        if next_item.tag == '{http://www.tei-c.org/ns/1.0}p':
            para = next_item.text

        segment_df.loc[len(segment_df)] = [header, para]

    else:
        pass
    

print(segment_df)


# {'input': ('C:\\Users\\henzh\\Downloads\\CUAD_v1\\CUAD_v1\\full_contract_pdf\\Part_I\\Joint Venture\\\\VALENCETECHNOLOGYINC_02_14_2003-EX-10-JOINT VENTURE CONTRACT.pdf', <_io.BufferedReader name='C:\\Users\\henzh\\Downloads\\CUAD_v1\\CUAD_v1\\full_contract_pdf\\Part_I\\Joint Venture\\\\VALENCETECHNOLOGYINC_02_14_2003-EX-10-JOINT VENTURE CONTRACT.pdf'>, 'application/pdf', {...})}