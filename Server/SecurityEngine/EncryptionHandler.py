import bcrypt
from Utils.Logger import LoggingSingleton

logger = LoggingSingleton.get_logger()

class PasswordManager:
    @staticmethod
    def hash_password(password: str) -> bytes:
        try:
            logger.debug("Starting password hashing process.")
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            logger.debug("Password hashing completed successfully.")
            return hashed_password
        except Exception as e:
            logger.error(f"Error hashing password: {e}")
            raise

    @staticmethod
    def verify_password(password: str, hashed_password: bytes) -> bool:
        try:
            logger.debug("Starting password verification process.")
            verification_result = bcrypt.checkpw(password.encode(), hashed_password)
            if verification_result:
                logger.info("Password verification succeeded.")
            else:
                logger.warning("Password verification failed.")
            return verification_result
        except Exception as e:
            logger.error(f"Error verifying password: {e}")
            raise
