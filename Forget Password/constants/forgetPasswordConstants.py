PASSWORD_FORGET_URL = "https://tobeto.com/sifremi-unuttum"

#Case 1: Şifre sıfırlama e-postası gönderme.
email_for_reset_password_path = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//input"
send_button_email_for_reset_password_path = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//button[.='Gönder']"

password_reset_link_message_path = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']//div[@role='alert']/div[@class='toast-body']"
passwordResetLinkMessageText = "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."

#Case 2: Girilen e-postanın geçersiz olma durumu
invalid_email_input_css = "#__next > div > main > section > div > div > div > input"
invalid_email_button_xpath = "//*[@id='__next']/div/main/section/div/div/div/button"

invalid_email_xpath = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']//div[@role='alert']/div[@class='toast-body']"
invalidEmailText = "• Girdiğiniz e-posta geçersizdir."