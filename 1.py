import requests
import pandas as pd
import pathlib
import os
filename="D:/ean/nsc_result_request/BM_All_Forthcoming.csv"
# source_url = "https://www1.nseindia.com/corporates/datafiles/BM_All_Forthcoming.csv"
source_url = "https://api.bseindia.com/BseIndiaAPI/api/DownloadCSV1/w?scripcode=&fromdate=&todate="
resp = requests.get(source_url)
file=pathlib.Path(filename)
