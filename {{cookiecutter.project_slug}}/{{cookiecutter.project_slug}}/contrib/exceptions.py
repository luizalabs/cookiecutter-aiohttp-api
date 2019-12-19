class APIException(Exception):
    status_code = 500
    error_code = 'server_error'
    error_message = 'Internal server error.'
    error_details = None

    def __init__(
        self,
        error_code=None,
        error_message=None,
        error_details=None,
    ):
        if error_code:
            self.error_code = error_code

        if error_message:
            self.error_message = error_message

        if error_details:
            self.error_details = error_details

    def as_dict(self):
        data = {
            'error_code': self.error_code,
            'error_message': self.error_message,
        }
        if self.error_details:
            data['error_details'] = self.error_details

        return data


class BadRequest(APIException):
    status_code = 400
    error_code = 'bad_request'
    error_message = 'Bad Request'
