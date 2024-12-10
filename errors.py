class AppException(Exception):
    def __init__(self, app_code: int, err_text: str):
        self.app_code = app_code
        self.err_text = err_text


errorEmailNotValidate = AppException(app_code=400, err_text="почта не прошла валидацию")
errorPhonelNotValidate = AppException(app_code=400, err_text="номер телефона не прошел валидацию")
errorDateNotValidate = AppException(app_code=400, err_text="дата не прошла валидацию")
errorEmptyValue = AppException(app_code=400, err_text="Пустое значение")