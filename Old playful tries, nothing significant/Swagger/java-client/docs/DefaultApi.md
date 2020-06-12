# DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**personsGet**](DefaultApi.md#personsGet) | **GET** /persons | 


<a name="personsGet"></a>
# **personsGet**
> List&lt;Person&gt; personsGet(size)



Gets &#x60;Person&#x60; objects. Optional query param of **size** determines size of returned array 

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
Double size = 3.4D; // Double | Size of array
try {
    List<Person> result = apiInstance.personsGet(size);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#personsGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Double**| Size of array |

### Return type

[**List&lt;Person&gt;**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

