from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.item import Item
from typing import Dict
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    item_id: int,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/items/{item_id}".format(item_id=item_id,),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, Item]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Item.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[HTTPValidationError, Item]]:
    """ Get By Id

    Args:
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Item]]
     """


    kwargs = _get_kwargs(
        item_id=item_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[HTTPValidationError, Item]]:
    """ Get By Id

    Args:
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Item]
     """


    return sync_detailed(
        item_id=item_id,
client=client,

    ).parsed

async def asyncio_detailed(
    item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[HTTPValidationError, Item]]:
    """ Get By Id

    Args:
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Item]]
     """


    kwargs = _get_kwargs(
        item_id=item_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[HTTPValidationError, Item]]:
    """ Get By Id

    Args:
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Item]
     """


    return (await asyncio_detailed(
        item_id=item_id,
client=client,

    )).parsed
