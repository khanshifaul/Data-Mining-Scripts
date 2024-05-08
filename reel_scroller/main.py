import time

from selenium.webdriver.common.by import By

from browser import driver

url = "https://www.facebook.com/"
driver.get(url)
posts = []


def scroll_smoothly(timeout=120):
    end_time = time.time() + timeout
    last_height = driver.execute_script("return document.body.scrollHeight")

    while time.time() < end_time:
        # Scroll by a smaller amount for smoother effect
        driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        time.sleep(2)  # Adjust sleep time as needed

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def capture_screenshots():
    new_posts = driver.find_elements(
        By.CSS_SELECTOR,
        "div.x1lliihq:nth-of-type(n+2) .x9f619 > div > div.x1jx94hy > div > div > div:nth-of-type(1) > div",
    )
    captured_count = len(posts)  # Track captured posts

    for i in range(captured_count, len(new_posts) + captured_count):
        new_posts[i - captured_count].screenshot(f"post_{i + 1}.png")
        print(f"Screenshot saved as 'post_{i + 1}.png'")
    posts.extend(new_posts)  # Add all new posts


# Assuming 'driver' is already initialized with your browser configuration

posts = []  # List to store captured posts

# Initial scroll and capture
scroll_smoothly()
capture_screenshots()

no_new_posts_count = 0  # Track consecutive loops without new posts

while True:
    # Scroll a bit and wait for new content
    driver.find_elements(
        By.CSS_SELECTOR,
        "div.x1lliihq:nth-of-type(n+2) .x9f619 > div > div.x1jx94hy > div > div > div:nth-of-type(1) > div",
    )
    time.sleep(5)  # Adjust sleep time as needed

    # Capture screenshots of newly loaded posts
    capture_screenshots()

    # Check if no new posts found for a certain number of loops
    if len(posts) == len(set(posts)):
        no_new_posts_count += 1
        if no_new_posts_count >= 2:  # Adjust threshold for waiting
            print("No new posts found for a while. Re-scrolling...")
            no_new_posts_count = 0
            scroll_smoothly()
            capture_screenshots()
    else:
        no_new_posts_count = 0  # Reset counter if new posts found

print("All posts processed.")
