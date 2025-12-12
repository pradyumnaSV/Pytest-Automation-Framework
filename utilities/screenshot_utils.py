import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# If you need to include the time module in the utility for delays, you can add it here.
# import time 

def headless_capture_full_page_screenshot(driver: WebDriver, file_name: str):
    """
    Captures a full-page screenshot by resizing the browser window to fit the
    entire page content, then saves the screenshot to the project's 'screenshots' folder.

    Args:
        driver (WebDriver): The active Selenium WebDriver instance.
        file_name (str): The name for the screenshot file (e.g., 'registration_success.png').
    """
    try:
        # --- 1. Get the total height and width of the page using JavaScript ---
        # Get dimensions from the scrollable area of the HTML document
        total_width = driver.execute_script("return document.body.parentNode.scrollWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

        # --- 2. Set the window size to match the total page size ---
        driver.set_window_size(total_width, total_height)
        
        # Optional: Add a brief pause if the resizing causes rendering issues
        # time.sleep(0.5) 

        # --- 3. Locate the 'body' tag (the container for the whole page) ---
        body_element = driver.find_element(By.TAG_NAME, "body")

        # --- 4. Define the save path ---
        # It's best practice to join the file name to the project root path
        # Assuming the 'screenshots' folder is at the project root
        
        # This creates the path: [Project Root]/screenshots/[file_name]
        save_path = os.path.abspath(os.path.join(os.curdir, "screenshots", file_name))
        
        # Ensure the 'screenshots' directory exists
        screenshot_dir = os.path.dirname(save_path)
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # --- 5. Save the screenshot ---
        body_element.screenshot(save_path)
        
        print(f"\n✅ Full page screenshot saved successfully at: {save_path}")

    except Exception as e:
        print(f"\n❌ ERROR capturing full page screenshot: {e}")
        # Optionally, take a regular viewport screenshot on failure
        driver.save_screenshot(os.path.abspath(os.path.join(os.curdir, "screenshots", f"FAILED_{file_name}")))



import base64

def head_capture_full_page_screenshot(driver: WebDriver, file_name: str):
    """
    Captures a full-page screenshot using Chrome DevTools Protocol (CDP).
    This method uses the 'clip' parameter to avoid zooming issues, ensuring a 1:1 scale capture.
    """
    print(f"\nAttempting CDP full-page screenshot for: {file_name}")
    try:
        # 1. Get the total width and height of the page using JavaScript.
        #    Using Math.max covers different ways browsers calculate page dimensions.
        width = driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
        height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

        # Add a small buffer and ensure they are integers
        width = int(width) + 10
        height = int(height) + 10

        print(f"Page dimensions determined as: {width}x{height}")

        # 2. Define the clipping region for the screenshot.
        #    This tells CDP exactly what area to capture and at what scale.
        clip = {
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "scale": 1  # Important: Keep scale at 1 to prevent zooming
        }

        # 3. Take the screenshot via CDP using the defined 'clip'.
        #    'captureBeyondViewport': True is required to capture outside the visible area.
        screenshot_data = driver.execute_cdp_cmd('Page.captureScreenshot', {
            'format': 'png',
            'fromSurface': True,
            'captureBeyondViewport': True,
            'clip': clip
        })

        # 4. Define path and ensure the directory exists.
        save_path = os.path.abspath(os.path.join(os.curdir, "screenshots", file_name))
        screenshot_dir = os.path.dirname(save_path)
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # 5. Decode the Base64 data and save the file.
        with open(save_path, "wb") as f:
            f.write(base64.b64decode(screenshot_data['data']))

        print(f"✅ Full page screenshot saved successfully: {save_path}")

    except Exception as e:
        print(f"\n❌ CDP Full Page Screenshot failed: {e}")
        # Fallback to standard viewport screenshot if CDP fails
        fallback_path = os.path.abspath(os.path.join(os.curdir, "screenshots", "fallback_" + file_name))
        driver.save_screenshot(fallback_path)
        print(f"Saved fallback viewport screenshot to: {fallback_path}")
    finally:
        # Good practice to clear any potential emulation overrides
        try:
            driver.execute_cdp_cmd('Emulation.clearDeviceMetricsOverride', {})
        except:
            pass