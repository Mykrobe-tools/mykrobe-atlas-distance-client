# coding: utf-8

"""
    Distance API

    <p>An API for CRUD of two types of distances <li> between a sample and its closest samples <li> between a sample and its closest phylogenetic tree node <p>This API is intended to satisfy the following user stories <li> as a user, I want to add my new sample and its close neighbours so that I can retrieve them later <li> as a user, I want to query a sample for its close neighbours and their nearest nodes in a phylogenetic tree <li> as a user, I want to query a sample for its close neighbours so that I can do my analysis <li> as a user, I want to query a sample for its nearest node in a phylogenetic tree so that I can do my analysis <li> as a user, I want to update a sample with new list of close neighbours so that they are correct <li> as a user, I want to update a sample with new nearest leaf node in a phylogenetic tree so that it is correct <li> as a user, I want to remove the nearest leaf node in a phylogenetic tree from a sample so that it is correct <li> as a user, I want to remove a sample so that it is no longer available to any users <li> as a user, I want to add a new leaf node to the phylogenetic tree <li> as a user, I want to remove a leaf node from the phylogenetic tree <li> as a user, I want to query a tree node for a list of samples which have this as nearest tree node  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from distance_client.api_client import ApiClient
from distance_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class NeighboursGetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def samples_id_nearest_neighbours_get(self, id, **kwargs):  # noqa: E501
        """samples_id_nearest_neighbours_get  # noqa: E501

        Return the list of nearest neighbours of a sample based on a sample ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samples_id_nearest_neighbours_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Neighbour]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.samples_id_nearest_neighbours_get_with_http_info(id, **kwargs)  # noqa: E501

    def samples_id_nearest_neighbours_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """samples_id_nearest_neighbours_get  # noqa: E501

        Return the list of nearest neighbours of a sample based on a sample ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samples_id_nearest_neighbours_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Neighbour], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samples_id_nearest_neighbours_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `samples_id_nearest_neighbours_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/samples/{id}/nearest-neighbours', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Neighbour]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
