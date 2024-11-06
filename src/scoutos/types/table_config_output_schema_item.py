# This file was auto-generated by Fern from our API Definition.

import typing
from .check_box_column import CheckBoxColumn
from .json_column import JsonColumn
from .markdown_column import MarkdownColumn
from .number_column import NumberColumn
from .select_column import SelectColumn
from .text_long_column import TextLongColumn
from .text_short_column import TextShortColumn
from .url_column import UrlColumn

TableConfigOutputSchemaItem = typing.Union[
    CheckBoxColumn, JsonColumn, MarkdownColumn, NumberColumn, SelectColumn, TextLongColumn, TextShortColumn, UrlColumn
]
