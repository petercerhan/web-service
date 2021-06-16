from mathapp.infrastructure_services.encryption_service import EncryptionService
from mathapp.infrastructure_services.token_service import TokenService
from mathapp.infrastructure_services.date_service import DateService
from mathapp.infrastructure_services.file_service import FileService

from flask import current_app

class InfrastructureServiceComposer:

    def __init__(self, file_uploads_path):
        self._file_uploads_path = file_uploads_path
    
    def compose_encryption_service(self):
        csrf_hash_key = current_app.config['CSRF_HASH_KEY']
        return EncryptionService(csrf_hash_key=csrf_hash_key)

    def compose_token_service(self):
        web_signing_key = current_app.config['AUTH_SECRET_KEY']
        api_signing_key = current_app.config['API_AUTH_SECRET_KEY']
        return TokenService(web_signing_key=web_signing_key, api_signing_key=api_signing_key)

    def compose_date_service(self):
        return DateService()

    def compose_file_service(self):
        return FileService(file_uploads_path=self._file_uploads_path)