import sys
import traceback
sys.path.append(r"C:\document_portal")
from logger.custom_logger import CustomLogger
logger = CustomLogger().get_logger("exception_experiment")

class DocumentPortalException(Exception):
    """Custom exception class for the Document Portal application."""
    def __init__(self, error_message, error_details:sys):
        _,_,exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno
        self.error_message = str(error_message)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))

    def __str__(self):
        return f"""
        Error in [{self.file_name}] at line [{self.lineno}]
        Message: {self.error_message}
        Traceback: {self.traceback_str}
        """
if __name__ == "__main__":
    logger = CustomLogger().get_logger("exception_experiment")
    try:
        # Simulate an error for demonstration purposes
        1 / 0
    except Exception as e:
        app_exc=DocumentPortalException(e, sys)
        logger.error(app_exc)
        raise app_exc
        