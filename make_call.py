import requests

def make_postcall(api_gateway : str,body : dict) -> dict:
    """This function make an post api call and returns the body information

    Args:
        api_gateway (str): api gateway to which the post call need to be performed.
        body (dict): json payload input for the api gateway

    Returns:
        dict: returns the json output
    """    
    try:
        post_response = requests.post(api_gateway, body)
        with open('post_response.json', 'wb') as fd:
            for chunk in post_response.iter_content(chunk_size=128):
                fd.write(chunk)
        return post_response.status_code
    except Exception as exc:
        print(exc)
        return None

def make_fetchcall(api_gateway : str, query_params : dict) -> dict:
    """This function make an Get api call and returns the body information

    Args:
        api_gateway (str): api gateway to which the post call need to be performed.
        query_params (dict): json payload input for the api gateway

    Returns:
        dict: returns the json output
    """    
    try:
        get_response = requests.get(api_gateway, query_params)
        with open('get_response.json', 'wb') as fd:
            for chunk in get_response.iter_content(chunk_size=128):
                fd.write(chunk)
        return get_response.status_code
    except Exception as exc:
        print(exc)
        return None

post_status = make_postcall('https://httpbin.org/post', {'key': 'value'})
print(f"post status code: {post_status}")
get_status = make_fetchcall('https://httpbin.org/get', {'key1': 'value1', 'key2': 'value2'})
print(f"get status code: {get_status}")