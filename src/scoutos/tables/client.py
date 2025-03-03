# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection_service_handlers_get_tables_response import CollectionServiceHandlersGetTablesResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.table_config_input_schema_item import TableConfigInputSchemaItem
from ..types.collection_service_handlers_create_table_response import CollectionServiceHandlersCreateTableResponse
from ..types.collection_service_handlers_get_table_response import CollectionServiceHandlersGetTableResponse
from .types.table_data_schema_item import TableDataSchemaItem
from ..types.collection_service_handlers_update_table_response import CollectionServiceHandlersUpdateTableResponse
from ..types.collection_service_handlers_delete_table_response import CollectionServiceHandlersDeleteTableResponse
from .types.tables_get_schema_response import TablesGetSchemaResponse
from ..types.collection_service_handlers_table_sync_response import CollectionServiceHandlersTableSyncResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTablesResponse:
        """
        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTablesResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.list(
            collection_id="collection_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetTablesResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetTablesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        collection_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableConfigInputSchemaItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersCreateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableConfigInputSchemaItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersCreateTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.create(
            collection_id="collection_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables",
            method="POST",
            json={
                "table_display_name": table_display_name,
                "table_img_url": table_img_url,
                "table_description": table_description,
                "schema": schema,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersCreateTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersCreateTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.get(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        collection_id: str,
        table_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableDataSchemaItem]] = OMIT,
        index_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersUpdateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableDataSchemaItem]]

        index_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersUpdateTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.update(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}",
            method="PUT",
            json={
                "table_display_name": table_display_name,
                "table_img_url": table_img_url,
                "table_description": table_description,
                "schema": schema,
                "index_id": index_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersUpdateTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersUpdateTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersDeleteTableResponse:
        """
        Delete a table given a collection_id and table_id.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersDeleteTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersDeleteTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_schema(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TablesGetSchemaResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TablesGetSchemaResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_schema(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/schema",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TablesGetSchemaResponse,
                    construct_type(
                        type_=TablesGetSchemaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def sync(
        self,
        collection_id: str,
        table_id: str,
        *,
        request: typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersTableSyncResponse:
        """
        Sync a table with a list of documents.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request : typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersTableSyncResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.sync(
            collection_id="collection_id",
            table_id="table_id",
            request=[{"key": "value"}],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/sync",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersTableSyncResponse,
                    construct_type(
                        type_=CollectionServiceHandlersTableSyncResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTablesResponse:
        """
        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTablesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetTablesResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetTablesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        collection_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableConfigInputSchemaItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersCreateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableConfigInputSchemaItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersCreateTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables",
            method="POST",
            json={
                "table_display_name": table_display_name,
                "table_img_url": table_img_url,
                "table_description": table_description,
                "schema": schema,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersCreateTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersCreateTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        collection_id: str,
        table_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableDataSchemaItem]] = OMIT,
        index_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersUpdateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableDataSchemaItem]]

        index_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersUpdateTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}",
            method="PUT",
            json={
                "table_display_name": table_display_name,
                "table_img_url": table_img_url,
                "table_description": table_description,
                "schema": schema,
                "index_id": index_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersUpdateTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersUpdateTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersDeleteTableResponse:
        """
        Delete a table given a collection_id and table_id.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersDeleteTableResponse,
                    construct_type(
                        type_=CollectionServiceHandlersDeleteTableResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_schema(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TablesGetSchemaResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TablesGetSchemaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_schema(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/schema",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TablesGetSchemaResponse,
                    construct_type(
                        type_=TablesGetSchemaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def sync(
        self,
        collection_id: str,
        table_id: str,
        *,
        request: typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersTableSyncResponse:
        """
        Sync a table with a list of documents.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request : typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersTableSyncResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.sync(
                collection_id="collection_id",
                table_id="table_id",
                request=[{"key": "value"}],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/sync",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersTableSyncResponse,
                    construct_type(
                        type_=CollectionServiceHandlersTableSyncResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
