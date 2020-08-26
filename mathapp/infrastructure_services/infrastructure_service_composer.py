from mathapp.infrastructure_services.encryption_service import EncryptionService


class InfrastructureServiceComposer:
    
    def compose_encryption_service(self):
        return EncryptionService()