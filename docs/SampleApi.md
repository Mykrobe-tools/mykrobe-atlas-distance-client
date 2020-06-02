# distance_client.SampleApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_post**](SampleApi.md#samples_post) | **POST** /samples | 


# **samples_post**
> Sample samples_post(sample)



Add a new sample. Duplicates are not allowed

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.SampleApi()
sample = distance_client.Sample() # Sample | Sample to be added

try:
    api_response = api_instance.samples_post(sample)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->samples_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample** | [**Sample**](Sample.md)| Sample to be added | 

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
**201** | Created. Maybe partially satisfied, the response body contains the created resource. |  -  |
**409** | Already existed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

