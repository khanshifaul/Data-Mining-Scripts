import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def comment_image(image_url):
  """Comments an image on a Facebook post.

  Args:
    post_id: The ID of the Facebook post.
    image_url: The URL of the image to comment.
  """

  browser = webdriver.Chrome()
  browser.get("https://www.facebook.com/")

  # Login to Facebook.
  browser.find_element(By.ID,"email").send_keys('felix33247@gmail.com')
  browser.find_element(By.ID,"pass").send_keys('Md$@kib760')
  browser.find_element(By.NAME,'login').click()

  # Go to the post page.
  post_url = "https://www.facebook.com/"
  browser.get(post_url)

  # Find the comment box.
  comment_box = browser.find_element(By.ID, "composerInput")

  # Upload the image.
  image_file = requests.get(image_url)
  comment_box.send_keys(image_file.content)

  # Click the "Post" button.
  browser.find_element(By.ID,"composerButton").click()

if __name__ == "__main__":
#   post_id = input("Enter the ID of the Facebook post: ")
#   image_url = input("Enter the URL of the image to comment: ")
  image_url = "https://scontent.fdac140-1.fna.fbcdn.net/v/t39.30808-6/366702511_2290872477780795_7538467565719403853_n.jpg?stp=dst-jpg_p75x225&_nc_cat=108&ccb=1-7&_nc_sid=755d08&_nc_ohc=N-dmJKW2D-sAX8Bw_mx&_nc_ht=scontent.fdac140-1.fna&oh=00_AfD_RtlwqfiXhJtvgLFPzI8UOuj79FJw6cA8Q1zBYquQPA&oe=64DF863E"
  comment_image(image_url)
