# distance_client.LeafPutApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_nearest_leaf_node_put**](LeafPutApi.md#samples_id_nearest_leaf_node_put) | **PUT** /samples/{id}/nearest-leaf-node | 


# **samples_id_nearest_leaf_node_put**
> NearestLeaf samples_id_nearest_leaf_node_put(id, nearest_leaf)



Replace the nearest leaf node of a sample based on a sample ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.LeafPutApi()
id = 'id_example' # str | 
nearest_leaf = distance_client.NearestLeaf() # NearestLeaf | New nearest leaf node to replace old one.

try:
    api_response = api_instance.samples_id_nearest_leaf_node_put(id, nearest_leaf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeafPutApi->samples_id_nearest_leaf_node_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nearest_leaf** | [**NearestLeaf**](NearestLeaf.md)| New nearest leaf node to replace old one. | 

### Return type

[**NearestLeaf**](NearestLeaf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Maybe partially satisfied, the response body contains the updated resource. |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

