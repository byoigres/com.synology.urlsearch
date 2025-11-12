import urllib.request
import json
import sys


def fetch_from_url(url):
    """
    Make a GET request to the provided URL and parse the response as JSON.
    
    Args:
        url (str): The URL to fetch data from
        
    Returns:
        dict or list: The parsed JSON response, or None if an error occurs
    """
    timeouts = 30
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1; de-de) AppleWebKit/527+ (KHTML, like Gecko) Version/3.1.1 Safari/525.20',
    }
    
    try:
        request = urllib.request.Request(url=url, headers=header, method='GET')
        response = urllib.request.urlopen(request, timeout=timeouts)
        result = response.read().decode('utf-8')
        
        # Parse the response as JSON
        json_data = json.loads(result)
        return json_data
        
    except urllib.error.HTTPError as http_e:
        # Handle HTTP errors
        sys.exit()
        
    except urllib.error.URLError as url_e:
        # Handle URL errors (network issues, etc.)
        sys.exit()
        
    except json.JSONDecodeError as json_e:
        # Handle JSON parsing errors
        sys.exit()
        
    except Exception as e:
        # Handle unexpected errors
        sys.exit()
    
    return None