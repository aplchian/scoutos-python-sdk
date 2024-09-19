# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .req_body_inputs_value import ReqBodyInputsValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ReqBody(UniversalBaseModel):
    inputs: typing.Dict[str, ReqBodyInputsValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
