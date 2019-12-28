import internetarchive as ia
from time import sleep
from uuid import uuid1
import os.path

# # Check if s3 is overloaded
# session = get_session(config_file=config_file)
# session.s3_is_overloaded()


class InternetArchive:
    DETAILS_URL = 'https://archive.org/details/{identifier}'
    DOWNLOAD_URL = 'https://archive.org/download/{identifier}/{filename}'

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.config_name = 'ia-config.ini'
        self.config_path = os.path.dirname(os.path.realpath(__file__))
        self.config_file = os.path.join(self.config_path, self.config_name)
        self.config_exist = os.path.exists(self.config_file)
        self.session = ia.get_session(config_file=self.config_file)
        self.access_key = self.session.config.get('s3', {}).get('access')
        self.secret_key = self.session.config.get('s3', {}).get('secret')
        self.is_authorized = self._is_user_auth()


    def _update_session(self):
        self.session = ia.get_session(config_file=self.config_file)
        self.access_key = self.session.config.get('s3', {}).get('access')
        self.secret_key = self.session.config.get('s3', {}).get('secret')

    def _is_user_auth(self):
        authenticated = False
        retries = 3
        while True:
            retries-=1
            try:
                auth = ia.get_user_info(access_key=self.access_key, secret_key=self.secret_key)
                if auth.get('authorized') == True:
                    authenticated = True
                    break
            except ia.exceptions.AuthenticationError as e1:
                print('get_user_info() Auth from config file Failed\n', e1)
                sleep(1)
                try:
                    ia.configure(self.username, self.password, config_file=self.config_file)
                    self._update_session()
                except Exception as e2:
                    print('ia.configure() Auth from Username|Password Failed\n', e1)
                    sleep(1)
                    print(e2)
                continue
            except Exception as e:
                authenticated = False
                continue
            finally:
                if retries == 0:
                    break
        return authenticated

    def upload(self, file, newname=None, title=None):
        if not self.is_authorized:
            return dict(download=None,details=None,status='not authenticated')
        unique_id = str(uuid1())[:8]
        filename = os.path.basename(file)
        name, ext = os.path.splitext(filename)
        newname = filename if newname is None else os.path.splitext(newname)[0]+ext
        retries = 3
        while retries > 0:
            try:
                ia.upload(unique_id, files = {
                                        newname: file
                                    },
                                    metadata = {
                                        'title': title,
                                        'mediatype': 'movies'
                                    })
                status = 'success'
            except FileNotFoundError:
                status = 'file not found'
            except Exception as e:
                status = str(e)
                retries-=1
                continue
            finally:
                if retries == 0:
                    break
            break

        return dict(download = self.DOWNLOAD_URL.format(identifier=unique_id, filename=newname) if status == 'success' else None,
                    details = self.DETAILS_URL.format(identifier=unique_id) if status == 'success' else None,
                    status = status)



if __name__ == '__main__':

    # Create internetarchive authenticated instance
    iarchive = InternetArchive('nforeleasenfo@gmail.com', 'make7arag')


    # Upload file to internetarchive
    """
    upload(self, file, newname=None, title=None)

        file: Path to the file to upload.

        newname: Name of the file on internetarchive.
            If nothing is set, original filename will be used

        title: Title of the internetarchive upload. If
            no title is set, the identifier will be used.

    """
    upload = iarchive.upload('Trimmed.mp4')


    # Output upload status
    if upload['download']:
        print(upload['status'], upload['download'])
    else:
        print(upload['status'])
