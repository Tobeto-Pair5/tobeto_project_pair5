LOGIN_URL= "https://tobeto.com/giris"



login_button_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"

navbar_button_css = ".btn.d-xxl-none.navbar-burger.p-0 > svg"

profile_page_xpath = "/html//div[@id='offcanvasExample']/div[@class='offcanvas-body']//button[@type='button']"

profile_info_page_xpath = "/html//div[@id='offcanvasExample']/div[@class='offcanvas-body']//div[@class='btn-group header-avatar w-100']/ul/li[1]/a[@href='#']"

foreign_language_xpath = "//div[@id='__next']/div[@class='back-white']/main/section/div[@class='container']//div[@class='col-12 col-lg-3 mb-8 mb-lg-0']/div/a[7]/span[@class='sidebar-text']"

select_language_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//select[@name='languageName']"

language_save_button_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//form[@action='#']/button[.='Kaydet']"

error_empty_language = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/p" 
errorEmptyLanguageText = "Doldurulması zorunlu alan*"

select_language_level_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//select[@name='proficiency']"

alert_xpath = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
addLanguageMessageText = "• Yabancı dil bilgisi eklendi."

delete_box_xpath = "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/div/div/div[1]"

delete_language_button_xpath = "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/div/div/div[1]/span[@class='delete-lang']"

errorAddLanguageMessageText = "• Bu dil zaten mevcut."

reject_delete_button_xpath = "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[.='Hayır']"

confirm_delete_button_xpath = "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']"

language_remove_successful = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"

LanguageRemoveSuccessfulText = "• Yabancı dil kaldırıldı."

