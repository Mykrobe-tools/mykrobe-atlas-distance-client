# distance_client.NeighboursPutApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_nearest_neighbours_put**](NeighboursPutApi.md#samples_id_nearest_neighbours_put) | **PUT** /samples/{id}/nearest-neighbours | 


# **samples_id_nearest_neighbours_put**
> list[Neighbour] samples_id_nearest_neighbours_put(id, neighbour)



Replace the list of nearest neighbours of a sample based on a sample ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.NeighboursPutApi()
id = 'id_example' # str | 
neighbour = [distance_client.Neighbour()] # list[Neighbour] | New list of nearest neighbours to replace old one.

try:
    api_response = api_instance.samples_id_nearest_neighbours_put(id, neighbour)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NeighboursPutApi->samples_id_nearest_neighbours_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **neighbour** | [**list[Neighbour]**](Neighbour.md)| New list of nearest neighbours to replace old one. | 

### Return type

[**list[Neighbour]**](Neighbour.md)

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

