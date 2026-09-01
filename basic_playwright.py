import os
import pytest
from playwright.sync_api import Page, expect

def test_select_spiderman(page: Page):
    # 1. Resolve the absolute path to your file
    file_path = os.path.abspath("webpage.html")
    
    # 2. Open the local file
    page.goto(f"file://{file_path}")

    # 3. Select 'Spiderman' from the dropdown
    hero_dropdown = page.get_by_test_id("select-hero")
    hero_dropdown.select_option("Spiderman")

    # 4. Verify that the display text shows Spiderman
    hero_display = page.get_by_test_id("text-selected-hero")
    expect(hero_display).to_have_text("Selected: Spiderman")

    # 5. Ensure the 'output' directory exists
    output_dir = os.path.abspath("output")
    os.makedirs(output_dir, exist_ok=True)

    # 6. Capture and save the screenshot
    screenshot_path = os.path.join(output_dir, "spiderman_selected.png")
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"\nScreenshot saved to: {screenshot_path}")