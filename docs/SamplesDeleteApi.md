# distance_client.SamplesDeleteApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_delete**](SamplesDeleteApi.md#samples_id_delete) | **DELETE** /samples/{id} | 


# **samples_id_delete**
> samples_id_delete(id)



Delete a sample based on a sample ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.SamplesDeleteApi()
id = 'id_example' # str | 

try:
    api_instance.samples_id_delete(id)
except ApiException as e:
    print("Exception when calling SamplesDeleteApi->samples_id_delete: %s\n" % e)
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

