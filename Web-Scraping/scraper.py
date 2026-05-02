import requests, csv, time
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"
CAT  = "https://books.toscrape.com/catalogue/"
RATINGS = {"One":1,"Two":2,"Three":3,
             "Four":4,"Five":5}

def scrape_page(url):
    r    = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = []
    for b in soup.select('article.product_pod'):
        r_word = b.select_one('.star-rating')['class'][1]
        rows.append({
          "title"   : b.select_one('h3 a')['title'],
          "price"   : b.select_one('.price_color').text,
          "rating"  : RATINGS.get(r_word,0),
          "available":b.select_one('.availability').text.strip(),
          "url"     : CAT + b.select_one('h3 a')['href']
        })
    nxt = soup.select_one('li.next a')
    return rows, (CAT+nxt['href'] if nxt else None)

url, all_data = BASE, []
while url:
    rows, url = scrape_page(url)
    all_data.extend(rows)
    print(f"  {len(all_data)} books scraped...", end="\r")
    time.sleep(0.3)

# Save to CSV
with open('books.csv', 'w', newline='') as f:
    w = csv.DictWriter(f,
      fieldnames=all_data[0].keys())
    w.writeheader()
    w.writerows(all_data)
print(f"\nSaved {len(all_data)} rows → books.csv")
