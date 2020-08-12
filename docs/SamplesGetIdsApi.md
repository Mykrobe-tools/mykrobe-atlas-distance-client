# distance_client.SamplesGetIdsApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_get**](SamplesGetIdsApi.md#samples_get) | **GET** /samples | 


# **samples_get**
> list[Sample] samples_get(ids=ids)



Return one or more samples based on IDs

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.SamplesGetIdsApi()
ids = ['ids_example'] # list[str] | A comma-separated list of sample IDs (optional)

try:
    api_response = api_instance.samples_get(ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesGetIdsApi->samples_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of sample IDs | [optional] 

### Return type

[**list[Sample]**](Sample.md)

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

