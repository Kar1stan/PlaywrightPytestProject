import allure


def take_screenshot(page, name):
    allure.attach(
        body=page.screenshot(full_page=True),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

