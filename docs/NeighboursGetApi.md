# distance_client.NeighboursGetApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_nearest_neighbours_get**](NeighboursGetApi.md#samples_id_nearest_neighbours_get) | **GET** /samples/{id}/nearest-neighbours | 


# **samples_id_nearest_neighbours_get**
> list[NeighbourRelationship] samples_id_nearest_neighbours_get(id)



Return the list of nearest neighbours of a sample based on a sample ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.NeighboursGetApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.samples_id_nearest_neighbours_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NeighboursGetApi->samples_id_nearest_neighbours_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[NeighbourRelationship]**](NeighbourRelationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

