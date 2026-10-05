from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("======================================")
print("       INTERACTIVE WEB SCRAPER")
print("======================================")

# Talentely LMS website
url = "https://lms.talentely.com/"

print("\nOpening website...")
print(url)

try:
    # Open Chrome browser
    driver = webdriver.Chrome()

    # Open Talentely LMS
    driver.get(url)

    # Wait for JavaScript to load
    time.sleep(5)

    # --------------------------------
    # 1. WEBSITE TITLE
    # --------------------------------
    print("\n========== WEBSITE TITLE ==========")

    print(driver.title)

    # --------------------------------
    # 2. HEADINGS
    # --------------------------------
    print("\n========== HEADINGS ==========")

    headings = driver.find_elements(
        By.XPATH,
        "//h1 | //h2 | //h3"
    )

    if headings:
        for i, heading in enumerate(headings, 1):
            text = heading.text.strip()

            if text:
                print(i, ".", text)
    else:
        print("No headings found.")

    # --------------------------------
    # 3. LINKS
    # --------------------------------
    print("\n========== LINKS ==========")

    links = driver.find_elements(By.TAG_NAME, "a")

    count = 0

    for link in links:

        text = link.text.strip()
        href = link.get_attribute("href")

        if text and href:
            count += 1
            print(count, ".", text, "->", href)

        if count == 10:
            break

    if count == 0:
        print("No links found.")

    # --------------------------------
    # 4. CONTACT / SUPPORT LINKS
    # --------------------------------
    print("\n========== CONTACT / SUPPORT ==========")

    contact_found = False

    for link in links:

        text = link.text.strip().lower()
        href = link.get_attribute("href")

        if (
            "contact" in text
            or "support" in text
            or "contact" in str(href).lower()
            or "support" in str(href).lower()
        ):
            print(text, "->", href)
            contact_found = True

    if not contact_found:
        print("No Contact or Support link found.")

    # --------------------------------
    # 5. PAGE TEXT
    # --------------------------------
    print("\n========== PAGE TEXT ==========")

    body_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text

    print(body_text[:2000])

    # --------------------------------
    # FINISHED
    # --------------------------------

    print("\n======================================")
    print("          SCRAPING COMPLETED")
    print("======================================")

    # Close browser
    driver.quit()

except Exception as e:

    print("\nError occurred:")
    print(e)