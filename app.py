import requests
from dotenv import load_dotenv
import os
import openpyxl 
import datetime


load_dotenv()


def get_smm_panel_data():
    url = os.getenv("SMMPanel_URL")
    key = os.getenv("SMMPanel_KEY")
    data = {"key" :key, "action": "services"}

    response = requests.post(url, data=data)
    return response.json()
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
worksheet.write_row(0, 0, ["Service","Category","Type","Rate","Name","Min","Max","Cancel","Refill","DripFeed"])

dataServices = get_smm_panel_data()
for index, service in enumerate(dataServices, start=1):
    worksheet.write_row(index, 0, [service["service"], service["category"], service["type"], service["rate"], service["name"], service["min"], service["max"], service["cancel"], service["refill"], service["dripfeed"]])
workbook.close()