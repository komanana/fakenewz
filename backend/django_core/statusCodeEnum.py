"""

"""

from enum import Enum


class StatusCodeEnum(Enum):
    """statu code enum"""

    OK = (0, 'Success')
    ERROR = (-1, 'Error')
    SERVER_ERR = (500, 'Server Exception')

    IMAGE_CODE_ERR = (4001, 'Error in Image Code')
    THROTTLING_ERR = (4002, 'Too Frequent Visits')
    NECESSARY_PARAM_ERR = (4003, 'Missing Required Parameters')
    USER_ERR = (4004, 'Invalid Username')
    PWD_ERR = (4005, 'Invalid Password')
    CPWD_ERR = (4006, 'Password Inconsistency')
    MOBILE_ERR = (4007, 'Invalid Mobile Number')
    SMS_CODE_ERR = (4008, 'Error in SMS Verification Code')
    ALLOW_ERR = (4009, 'Unaccepted Protocol')
    SESSION_ERR = (4010, 'User Not Logged In')
    REGISTER_FAILED_ERR = (4011, 'Registration Failed')

    DB_ERR = (5000, 'Database Error')
    EMAIL_ERR = (5001, 'Invalid Email')
    TEL_ERR = (5002, 'Invalid Telephone Number')
    NODATA_ERR = (5003, 'No Data')
    NEW_PWD_ERR = (5004, 'Invalid New Password')
    OPENID_ERR = (5005, 'Invalid OpenID')
    PARAM_ERR = (5006, 'Invalid Parameter')
    STOCK_ERR = (5007, 'Insufficient Stock')

    @property
    def code(self):
        """get the error code"""
        return self.value[0]

    @property
    def errmsg(self):
        """to get the error msg"""
        return self.value[1]