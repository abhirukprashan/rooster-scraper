from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        site_rl = "https://rooster.jobs"
        url = "https://rooster.jobs/?query=intern&limit=445&page=1"
        page.goto(url)
        
        products = page.locator(".job-item")
        count = products.count()
        print(count)
        for i in range(count):
            try: 
                product = products.nth(i)
                title_locator = product.locator(".job-title-h5")
                
                link_locator = product.locator(".job-title")
                href = link_locator.get_attribute("href")
                full_url = site_rl + href
                print(title_locator.text_content())
                print(full_url)


            except:
                print("Error")
if __name__ == "__main__":
    main()
