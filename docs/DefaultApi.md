# distance_client.DefaultApi

All URIs are relative to *http://distance-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_delete**](DefaultApi.md#samples_id_delete) | **DELETE** /samples/{id} | 
[**samples_id_get**](DefaultApi.md#samples_id_get) | **GET** /samples/{id} | 
[**samples_id_nearest_leaf_node_put**](DefaultApi.md#samples_id_nearest_leaf_node_put) | **PUT** /samples/{id}/nearest-leaf-node | 
[**samples_id_nearest_neighbours_put**](DefaultApi.md#samples_id_nearest_neighbours_put) | **PUT** /samples/{id}/nearest-neighbours | 
[**tree_id_delete**](DefaultApi.md#tree_id_delete) | **DELETE** /tree/{id} | 
[**tree_id_get**](DefaultApi.md#tree_id_get) | **GET** /tree/{id} | 
[**tree_post**](DefaultApi.md#tree_post) | **POST** /tree | 


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
api_instance = distance_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_instance.samples_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->samples_id_delete: %s\n" % e)
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

# **samples_id_get**
> Sample samples_id_get(id)



Return a sample based on a sample ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.samples_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->samples_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Sample**](Sample.md)

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
api_instance = distance_client.DefaultApi()
id = 'id_example' # str | 
nearest_leaf = distance_client.NearestLeaf() # NearestLeaf | New nearest leaf node to replace old one.

try:
    api_response = api_instance.samples_id_nearest_leaf_node_put(id, nearest_leaf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->samples_id_nearest_leaf_node_put: %s\n" % e)
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
api_instance = distance_client.DefaultApi()
id = 'id_example' # str | 
neighbour = [distance_client.Neighbour()] # list[Neighbour] | New list of nearest neighbours to replace old one.

try:
    api_response = api_instance.samples_id_nearest_neighbours_put(id, neighbour)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->samples_id_nearest_neighbours_put: %s\n" % e)
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

# **tree_id_delete**
> tree_id_delete(id)



Delete a leaf node based on an ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_instance.tree_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->tree_id_delete: %s\n" % e)
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

# **tree_id_get**
> list[Neighbour] tree_id_get(id)



Return the list of nearest samples of a tree node based on an ID.

### Example

```python
from __future__ import print_function
import time
import distance_client
from distance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = distance_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.tree_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tree_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Neighbour]**](Neighbour.md)

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
api_instance = distance_client.DefaultApi()
leaf = distance_client.Leaf() # Leaf | Leaf node to be added

try:
    api_response = api_instance.tree_post(leaf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tree_post: %s\n" % e)
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

