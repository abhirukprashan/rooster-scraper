import csv
from playwright.sync_api import sync_playwright
import sys




def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url_arg = sys.argv[1]

        site_rl = "https://rooster.jobs"
        url = f"https://rooster.jobs/?query={url_arg}&limit=10000&page=1"
        page.goto(url)
        
        products = page.locator(".job-item")
        count = products.count()
        print(count)
        with open('jobs.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['title','link'])
            writer.writeheader()

 
        for i in range(count):
            try: 
                product = products.nth(i)
                title_locator = product.locator(".job-title-h5")
                
                link_locator = product.locator(".job-title")
                href = link_locator.get_attribute("href")
                full_url = site_rl + href
                tile_name = title_locator.text_content()

                with open('jobs.csv', 'a', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['title','link'])
                    
                    writer.writerow({"title":tile_name,"link":full_url})
                print(title_locator.text_content())
                print(full_url)


            except:
                print("Error")
if __name__ == "__main__":
    main()
