from pydantic import BaseModel, AnyUrl, EmailStr
from typing import List
from phonenumbers import parse, NumberParseException, is_valid_number
from app.models.rwmodel import RWModel
from app.models.dbModel import DBModelMixin

class PhoneNumber(str):
    @staticmethod
    def validate(v):
        """
        Validate the phone number.

        Args:
            v (str): Phone number to validate.

        Returns:
            str: Validated phone number.

        Raises:
            ValueError: If the phone number is invalid.
        """
        try:
            parsed_number = parse(v, "NG")  # Assuming "NG" stands for Nigeria
            if not is_valid_number(parsed_number):
                raise ValueError("Invalid phone number")
        except NumberParseException:
            raise ValueError("Invalid phone number")

        return v

    @classmethod
    def __get_validators__(cls):
        """
        Get validators for the PhoneNumber class.

        Yields:
            callable: Validators for the PhoneNumber class.
        """
        yield cls.validate


class Profile(BaseModel):
    network: str = ""
    username: str = ""
    url: AnyUrl = None

class BasicInfoBase(RWModel):
    first_name: str
    middle_name: str = ""
    last_name: str
    email: EmailStr


class BasicInfo(DBModelMixin, BasicInfoBase):
    label: str = ""
    image: AnyUrl = None
    picture: AnyUrl = None
    phone: List[PhoneNumber]
    website: AnyUrl = None
    summary: str = ""
    location: str = ""
    profiles: List[Profile] = []
    headline: str = ""
    blog: AnyUrl = None
    years_of_experience: int = 0
    username: str = ""
    location_string: str = ""
    region: str = ""
    country: str = ""
    country_code: str = ""


class BasicInfoCreate(BasicInfoBase):
    pass