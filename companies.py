# cd C:\Users\Tengo\Documents
import requests
from bs4 import BeautifulSoup as BS
import math

def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    url = "https://companiesmarketcap.com/"
    response = requests.get(url, headers=headers).text
    soup = BS(response, "lxml")
    
    # elements = soup.find("div", class_="table-container shadow").find("tbody").find_all("td")
    # print(elements)

    item_amount = int(soup.find("div", class_="site-header").find("span", class_="font-weight-bold").text.replace(",", ""))
    pages_count = math.ceil(item_amount / 100)
    urls = []
    elements = []
    for page in range(1, pages_count + 1):
        url = f"https://companiesmarketcap.com/page/{str(page)}"
        response = requests.get(url, headers=headers).text
        soup = BS(response, "lxml")

        el_urls = soup.find("div", class_="table-container shadow").find("table").find("tbody").find_all("td", class_="name-td")
    
        for el in el_urls:
            element_url = el.find("div", class_="name-div").find("a").get("href")
            urls.append(element_url)
        for all_url in urls:
            url = f"https://companiesmarketcap.com{all_url}"
            response = requests.get(url, headers=headers).text
            soup = BS(response, "lxml")

            try:
                name = soup.find("div", class_="table-container").find("div", class_="col-lg-2").find("div", class_="company-name").text.strip()
            except:
                name = "None"
            try:
                rank = soup.find("div", class_="col-lg-6").find("div", class_="row").find("div", class_="info-box").find("div", class_="line1").text.strip()
            except:
                rank = "None"
            try:
                marketcap = soup.find("div", class_="table-container").find_all("div", class_="row")[1].find_all("div", class_="info-box")[1].find("div", class_="line1").text.strip()
            except:
                marketcap = "None"
            try:
                share_price =  soup.find("div", class_="table-container").find_all("div", class_="row")[2].find_all("div", class_="info-box")[0].find("div", class_="line1").text.strip()
            except:
                share_price = "None"
            try:
                change_1d = soup.find("div", class_="table-container").find_all("div", class_="row")[2].find_all("div", class_="info-box")[1].find("div", class_="line1").text.strip()
            except:
                change_1d = "None"
            try:
                change_30d = soup.find("div", class_="table-container").find_all("div", class_="row")[2].find_all("div", class_="info-box")[2].find("div", class_="line1").text.strip()
            except:
                change_30d = "None"
            try:
                description = soup.find("div", class_="table-container").find("div", class_="row").find("div", class_="col-lg-4").text.strip()
            except:
                description = "None"
            element_list = {
                "Name" : name,
                "Rank" : rank,
                "Marketcap" : marketcap,
                "Sare_Price" : share_price,
                "Change_1D" : change_1d,
                "Change_30D" : change_30d,
                "Description" : description
            }
            elements.append(element_list)
            print("in process")

def main():
    get_data()

if __name__ == "__main__":
    main()