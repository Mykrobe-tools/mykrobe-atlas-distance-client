# distance_client.TreePostApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tree_post**](TreePostApi.md#tree_post) | **POST** /tree | 


# **tree_post**
> Leaf tree_post(leaf)



Create a leaf node for the phylogenetic tree.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.TreePostApi()
leaf = distance_client.Leaf() # Leaf | Leaf node to be added

try:
    api_response = api_instance.tree_post(leaf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreePostApi->tree_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaf** | [**Leaf**](Leaf.md)| Leaf node to be added | 

### Return type

[**Leaf**](Leaf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The response body contains the created resource. |  -  |
**409** | Already existed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

