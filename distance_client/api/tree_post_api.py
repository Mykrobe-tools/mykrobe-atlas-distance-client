# coding: utf-8

"""
    Distance API

    <p>An API for CRUD of two types of distances <li> between a sample and its closest samples <li> between a sample and its closest phylogenetic tree node <p>This API is intended to satisfy the following user stories <li> as a user, I want to add my new sample and its close neighbours so that I can retrieve them later <li> as a user, I want to query a sample for its close neighbours and its nearest node in a phylogenetic tree <li> as a user, I want to query a sample for its close neighbours so that I can do my analysis <li> as a user, I want to query a sample for its nearest node in a phylogenetic tree so that I can do my analysis <li> as a user, I want to update a sample with new list of close neighbours so that they are correct <li> as a user, I want to update a sample with new nearest leaf node in a phylogenetic tree so that it is correct <li> as a user, I want to remove the nearest leaf node in a phylogenetic tree from a sample so that it is correct <li> as a user, I want to remove a sample so that it is no longer available to any users <li> as a user, I want to add a new leaf node to the phylogenetic tree <li> as a user, I want to remove a leaf node from the phylogenetic tree <li> as a user, I want to query a tree node for a list of samples which have this as nearest tree node  # noqa: E501

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


class TreePostApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tree_post(self, leaf, **kwargs):  # noqa: E501
        """tree_post  # noqa: E501

        Create a leaf node for the phylogenetic tree.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tree_post(leaf, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Leaf leaf: Leaf node to be added (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Leaf
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.tree_post_with_http_info(leaf, **kwargs)  # noqa: E501

    def tree_post_with_http_info(self, leaf, **kwargs):  # noqa: E501
        """tree_post  # noqa: E501

        Create a leaf node for the phylogenetic tree.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tree_post_with_http_info(leaf, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Leaf leaf: Leaf node to be added (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Leaf, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['leaf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tree_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'leaf' is set
        if self.api_client.client_side_validation and ('leaf' not in local_var_params or  # noqa: E501
                                                        local_var_params['leaf'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `leaf` when calling `tree_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'leaf' in local_var_params:
            body_params = local_var_params['leaf']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tree', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Leaf',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
