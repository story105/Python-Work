def signup_new_user(self, username=None, password=None, email_address=None, confirm_password=None, server='imap.gmail.com', use_defaults=True):
        self.take_screenshot('signup_new_user_pre')

        if use_defaults:
            confirm_password = password

        if username: self.signup_page.username = username
        if password: self.signup_page.password = password
        if confirm_password: self.signup_page.confirm_password = confirm_password
        if email_address: self.signup_page.email = email_address

        shared_variables_mc.username_default = username

        logging.info(f'checking email with email={email_address} password={password}')
        mail = imaplib.IMAP4_SSL(server)
        mail.login(email_address,password)
        mail.select('inbox')
        self._mail = mail
        logging.info('login successful')

        status, email_list_pre = mail.search(None, '(SUBJECT "Welcome to MobiledgeX!")')
        mail_ids_pre = email_list_pre[0].split()
        num_emails_pre = len(mail_ids_pre)
        self._mail_count = num_emails_pre
        logging.info(f'number of emails pre is {num_emails_pre}')

        self._newuser_username = username
        self._newuser_password = password
        self._newuser_email = email_address

        self.signup_page.click_signup_button()

        if self.signup_page.is_alert_box_present():
            if self.signup_page.get_alert_box_text() != 'user created':
                raise Exception('user created alert box not found. got ' + self.signup_page.get_alert_box_text())
