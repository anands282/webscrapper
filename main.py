from shop import Shop
from shop_data import ShopData
import argparse
from playwright.sync_api import sync_playwright


def main():

    command_line_args = argparse.ArgumentParser()
    command_line_args.add_argument("--category", type=str)
    command_line_args.add_argument("--location", type=str)
    command_line_args.add_argument("--number", type=int)
    search_parameters = command_line_args.parse_args()
    category = search_parameters.category
    location = search_parameters.location
    number_of_items = search_parameters.number

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com/maps", timeout=10000)
        page.wait_for_timeout(1000)

        page.locator('//input[@id="searchboxinput"]').fill(category + " " +location)
        page.wait_for_timeout(1000)

        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)

        page.hover('//a[contains(@href, "https://www.google.com/maps/place")]')

        previously_counted = 0
        while True:
            page.mouse.wheel(0, 10000)
            page.wait_for_timeout(3000)

            if (
                    page.locator(
                        '//a[contains(@href, "https://www.google.com/maps/place")]'
                    ).count()
                    >= number_of_items
            ):
                listings = page.locator(
                    '//a[contains(@href, "https://www.google.com/maps/place")]'
                ).all()[:number_of_items]

                print(f"Total Scraped: {len(listings)}")
                break
            else:
                # logic to break from loop to not run infinitely
                # in case arrived at all available listings
                if (
                        page.locator(
                            '//a[contains(@href, "https://www.google.com/maps/place")]'
                        ).count()
                        == previously_counted
                ):
                    listings = page.locator(
                        '//a[contains(@href, "https://www.google.com/maps/place")]'
                    ).all()
                    print(f"Arrived at all available\nTotal Scraped: {len(listings)}")
                    break
                else:
                    previously_counted = page.locator(
                        '//a[contains(@href, "https://www.google.com/maps/place")]'
                    ).count()
                    print(
                        f"Currently Scraped: ",
                        page.locator(
                            '//a[contains(@href, "https://www.google.com/maps/place")]'
                        ).count(),
                    )

        shop_data_obj = ShopData()

        for listing in listings:
            listing.click()
            page.wait_for_timeout(5000)

            name_attribute = 'aria-label'
            location_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
            website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
            contact_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
            average_review_count_xpath = '//div[@jsaction="pane.reviewChart.moreReviews"]//span'
            average_review_points_xpath = '//div[@jsaction="pane.reviewChart.moreReviews"]//div[@role="img"]'

            shop_obj = Shop()

            if len(listing.get_attribute(name_attribute)) >= 1:

                shop_obj.shop_name = listing.get_attribute(name_attribute)
            else:
                shop_obj.shop_name = ""
            if page.locator(location_xpath).count() > 0:
                shop_obj.shop_location = page.locator(location_xpath).all()[0].inner_text()
            else:
                shop_obj.shop_location = ""
            if page.locator(website_xpath).count() > 0:
                shop_obj.website = page.locator(website_xpath).all()[0].inner_text()
            else:
                shop_obj.website = ""
            if page.locator(contact_number_xpath).count() > 0:
                shop_obj.contact_number = page.locator(contact_number_xpath).all()[0].inner_text()
            else:
                shop_obj.contact_number = ""
            if page.locator(average_review_count_xpath).count() > 0:
                shop_obj.average_review_count = int(
                    page.locator(average_review_count_xpath).inner_text()
                    .split()[0]
                    .replace(',', '')
                    .strip()
                )
            else:
                shop_obj.average_review_count = ""

            if page.locator(average_review_points_xpath).count() > 0:
                shop_obj.average_review_points = float(
                    page.locator(average_review_points_xpath).get_attribute(name_attribute)
                    .split()[0]
                    .replace(',', '.')
                    .strip())
            else:
                shop_obj.average_review_points = ""

            shop_data_obj.business_list.append(shop_obj)

        shop_data_obj.create_csv(f"{category}_in_{location}_google_maps")
        browser.close()


if __name__ == "__main__":
    main()
