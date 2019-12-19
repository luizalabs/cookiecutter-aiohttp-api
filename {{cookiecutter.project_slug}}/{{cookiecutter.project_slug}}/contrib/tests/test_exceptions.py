from {{cookiecutter.project_slug}}.contrib.exceptions import APIException


class TestAPIException:

    def test_as_dict_returns_all_fields(self):
        error_code = 'testing_error_code'
        error_message = 'oh my god!'
        error_details = {'some extra info': 'goes here'}

        exception = APIException(
            error_code=error_code,
            error_message=error_message,
            error_details=error_details
        )

        data = exception.as_dict()

        assert data['error_code'] == error_code
        assert data['error_message'] == error_message
        assert data['error_details'] == error_details

    def test_as_dict_removes_empty_error_details(self):
        exception = APIException()

        data = exception.as_dict()
        assert 'error_details' not in data
