# distance_client.SamplesPatchApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_patch**](SamplesPatchApi.md#samples_id_patch) | **PATCH** /samples/{id} | 


# **samples_id_patch**
> Sample samples_id_patch(id, sample)



Update a sample based on its ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.SamplesPatchApi()
id = 'id_example' # str | 
sample = distance_client.Sample() # Sample | New sample data

try:
    api_response = api_instance.samples_id_patch(id, sample)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesPatchApi->samples_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sample** | [**Sample**](Sample.md)| New sample data | 

### Return type

[**Sample**](Sample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Location - uri for the new sample <br>  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

