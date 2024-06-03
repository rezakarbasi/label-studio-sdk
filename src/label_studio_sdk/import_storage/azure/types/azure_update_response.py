# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class AzureUpdateResponse(pydantic_v1.BaseModel):
    project: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Project ID
    """

    container: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Azure blob container
    """

    prefix: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Azure blob prefix name
    """

    regex_filter: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Cloud storage regex for filtering objects
    """

    use_blob_urls: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Interpret objects as BLOBs and generate URLs
    """

    account_name: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Azure Blob account name
    """

    account_key: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Azure Blob account key
    """

    presign: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Presign URLs for direct download
    """

    presign_ttl: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Presign TTL in minutes
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
