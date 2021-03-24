link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
language_locator = "[selected='selected']"

exp_btn_text_dict = {
    "ru": "Добавить в корзину",
    "en-GB": "Add to basket",
    "es": "Añadir al carrito",
    "fr": "Ajouter au panier"
}


def test_add_to_basket_btn(browser):
    expected_lang_code = browser.user_language
    exp_btn_text = exp_btn_text_dict[expected_lang_code]

    browser.get(link)
    button_add = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    successful_button_text = button_add.text
    assert exp_btn_text in successful_button_text, "Invalid button text"
