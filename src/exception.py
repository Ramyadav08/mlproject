import sys 

def error_details_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = str(error)
    error_details = f"Error occurred in script: {file_name} at line number: {line_number} with error message: {error_message}"
    return error_details

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_details_message(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
    

