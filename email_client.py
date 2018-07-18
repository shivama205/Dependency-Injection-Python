import imaplib
class EmailClient(object):
    def __init__(self, config):
        self._config = config
        self.connect(self._config)
    def connect(self, config):
        try:
            self._client = imaplib.IMAP4_SSL(config.get('domain_name'))
            self._client.login(config.get('email_address'), config.get('password'))
            self.mailbox(config.get('mailbox'))
        except Exception as e:
            raise e
    def mailbox(self, mailbox_name):
        try:
            rv, data = self._client.select(mailbox_name)
            if rv != 'OK':
                raise Exception("Invalid mailbox: ", mailbox_name)
        except Exception as e:
            raise e
    
    def search(self, search_str):
        try:
            rv, data = self._client.search(None, search_str)
            if rv != 'OK':
                raise Exception("No email with given search criteria ", search_str)
            return data[0].split()
        except Exception as e:
            raise e
    def get_email(self, email_id):
        try:
            rv, data = self._client.fetch(email_id, '(RFC822)')
            if rv != 'OK':
                raise Exception("No email found for email id ", email_id)
            return data[0][1]
        except Exception as e:
            raise e
def search(self, search_str):
        try:
            print search_str
            rv, data = self._client.search(None, search_str)
            if rv != 'OK':
                raise Exception("No email with given search criteria ", search_str)
            return data[0].split()
        except Exception as e:
            raise e
def get_email(self, email_id):
        try:
            rv, data = self._client.fetch(email_id, '(RFC822)')
            if rv != 'OK':
                raise Exception("No email found for email id ", email_id)
            return data[0][1]
        except Exception as e:
            raise e
