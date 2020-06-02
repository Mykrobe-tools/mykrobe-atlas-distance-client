# coding: utf-8

"""
    Distance API

    <p>An API for CRUD of two types of distances <li> between a sample and its closest samples <li> between a sample and its closest phylogenetic tree node <p>This API is intended to satisfy the following user stories <li> as a user, I want to add my new sample and its close neighbours so that I can retrieve them later <li> as a user, I want to query a sample for its close neighbours and its nearest node in a phylogenetic tree <li> as a user, I want to query a sample for its close neighbours so that I can do my analysis <li> as a user, I want to query a sample for its nearest node in a phylogenetic tree so that I can do my analysis <li> as a user, I want to update a sample with new list of close neighbours so that they are correct <li> as a user, I want to update a sample with new nearest leaf node in a phylogenetic tree so that it is correct <li> as a user, I want to remove a sample so that it is no longer available to any users <li> as a user, I want to add a new leaf node to the phylogenetic tree <li> as a user, I want to remove a leaf node from the phylogenetic tree <li> as a user, I want to query a tree node for a list of samples which have this as nearest tree node  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import distance_client
from distance_client.models.error import Error  # noqa: E501
from distance_client.rest import ApiException


class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testError(self):
        """Test Error"""
        # FIXME: construct object with mandatory attributes with example values
        # model = distance_client.models.error.Error()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()