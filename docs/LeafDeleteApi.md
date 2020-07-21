# distance_client.LeafDeleteApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_nearest_leaf_node_delete**](LeafDeleteApi.md#samples_id_nearest_leaf_node_delete) | **DELETE** /samples/{id}/nearest-leaf-node | 


# **samples_id_nearest_leaf_node_delete**
> samples_id_nearest_leaf_node_delete(id)



Delete the nearest leaf node associated with a sample based on a sample ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.LeafDeleteApi()
id = 'id_example' # str | 

try:
    api_instance.samples_id_nearest_leaf_node_delete(id)
except ApiException as e:
    print("Exception when calling LeafDeleteApi->samples_id_nearest_leaf_node_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

