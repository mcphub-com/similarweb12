import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Glavier/api/similarweb12'

mcp = FastMCP('similarweb12')

@mcp.tool()
def autocomplete(query: Annotated[Union[str, None], Field(description='Search query')] = None) -> dict: 
    '''Autocomplete'''
    url = 'https://similarweb12.p.rapidapi.com/v3/autocomplete/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filter_options(type: Annotated[Literal['websites', 'apps', 'browsers', 'search-engines', 'platforms'], Field(description='Default: websites. It must be one of the following: websites apps browsers search-engines platforms Example: websites')]) -> dict:
    '''Filter Options'''
    url = 'https://similarweb12.p.rapidapi.com/v2/filter-options/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def marketshare(type: Annotated[Literal['browsers', 'search-engines', 'platforms'], Field(description='It must be one of the following: browsers search-engines platforms Example: browsers')],
                country: Annotated[Union[str, None], Field(description='You should use the Filter Options endpoint to list the countries that can be selected. Example: united-states')] = None,
                platform: Annotated[Union[str, None], Field(description='You should use the Filter Options endpoint to list the platforms that can be selected. Example: desktop')] = None) -> dict:
    '''Marketshare'''
    url = 'https://similarweb12.p.rapidapi.com/v3/marketshare/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'country': country,
        'platform': platform,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def serpseismometer() -> dict:
    '''SERP Seismometer measures SERP fluctuations for 10K+ domains and keywords that we monitor daily. We track both desktop and mobile SERP volatility over the past 30 and 90 days to allow you full SERP visibility. Check below what’s the risk for a SERP earthquake according to our Seismograph'''
    url = 'https://similarweb12.p.rapidapi.com/v2/serp-seismometer'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def website_analytics_detailed(domain: Annotated[str, Field(description='Website / domain name')]) -> dict:
    '''Website Analytics / Detailed'''
    url = 'https://similarweb12.p.rapidapi.com/v2/website-analytics/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def website_analytics_light_fast(domain: Annotated[str, Field(description='Website / domain name')]) -> dict:
    '''Website Analytics / Light & Fast'''
    url = 'https://similarweb12.p.rapidapi.com/v3/website-analytics/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def website_competitors(domain: Annotated[str, Field(description='Website / domain name')]) -> dict:
    '''Website Competitors'''
    url = 'https://similarweb12.p.rapidapi.com/v2/website-competitors'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_websites(country: Annotated[Union[str, None], Field(description="You should use the Filter Options endpoint (with type=websites) to list the countries that can be selected. Don't send the parameter for Worldwide. Example: united-states")] = None,
                 category: Annotated[Union[str, None], Field(description="You should use the Filter Options endpoint (with type=websites) to list the categories that can be selected. Don't send the parameter for All categories. Example: arts-and-entertainment")] = None,
                 subcategory: Annotated[Union[str, None], Field(description="You should use the Filter Options endpoint (with type=websites) to list the sub-categories that can be selected. Don't send the parameter for All categories. Example: animation-and-comics")] = None) -> dict:
    '''Top Websites'''
    url = 'https://similarweb12.p.rapidapi.com/v3/top-websites/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'category': category,
        'subcategory': subcategory,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_websites_v2(country: Annotated[Union[str, None], Field(description='Country URL code. Example: united-states, albania')] = None,
                    category: Annotated[Union[str, None], Field(description='Category URL code. Example: finance')] = None,
                    subcategory: Annotated[Union[str, None], Field(description='Sub-Category URL code. Example: investing')] = None,
                    trending: Annotated[Union[bool, None], Field(description=' Example: false')] = None) -> dict:
    '''Top Websites / v2'''
    url = 'https://similarweb12.p.rapidapi.com/v2/top-websites'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'category': category,
        'subcategory': subcategory,
        'trending': trending,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_apps(store: Annotated[Literal['apple', 'google'], Field(description='Store parameter. apple: App Store google: Google Play Store Example: apple')],
             country: Annotated[Union[str, None], Field(description="You should use the Filter Options endpoint (with type=apps) to list the countries that can be selected. Don't send the parameter for Worldwide. Example: united-states")] = None,
             category: Annotated[Union[str, None], Field(description="You should use the Filter Options endpoint (with type=apps) to list the categories that can be selected. Don't send the parameter for All categories. Example: games")] = None,
             subcategory: Annotated[Union[str, None], Field(description="You should use the Filter Options endpoint (with type=apps) to list the sub-categories that can be selected. Don't send the parameter for All categories. Example: action")] = None,
             mode: Annotated[Literal['top-free', 'top-paid', 'top-grossing', None], Field(description='Default: top-free Example: top-free')] = None,
             device: Annotated[Literal['iphone', 'ipad', None], Field(description='Currently available for the App Store Example: iphone')] = None,
             date: Annotated[Union[str, None], Field(description='Format: YYYY-MM-DD')] = None) -> dict:
    '''Top Apps'''
    url = 'https://similarweb12.p.rapidapi.com/v3/top-apps/'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'store': store,
        'country': country,
        'category': category,
        'subcategory': subcategory,
        'mode': mode,
        'device': device,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def app_store_app_details(app_id: Annotated[str, Field(description='App Store App ID')]) -> dict:
    '''App Store / App Details'''
    url = 'https://similarweb12.p.rapidapi.com/v2/app-store-app-details'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'app_id': app_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def app_store_top_apps(country: Annotated[Union[str, None], Field(description='Country URL code. Example: united-states, albania')] = None,
                       category: Annotated[Union[str, None], Field(description='Category URL code. Example: business')] = None,
                       mode: Annotated[Literal['top-free', 'top-paid', 'top-grossing', None], Field(description=' Example: top-free')] = None,
                       device: Annotated[Literal['iphone', 'ipad', None], Field(description=' Example: iphone')] = None,
                       trending: Annotated[Union[bool, None], Field(description=' Example: false')] = None) -> dict:
    '''App Store / Top Apps'''
    url = 'https://similarweb12.p.rapidapi.com/v2/app-store-top-apps'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'category': category,
        'mode': mode,
        'device': device,
        'trending': trending,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def play_store_app_details(app_id: Annotated[str, Field(description='Google Play App ID')]) -> dict:
    '''Play Store / App Details'''
    url = 'https://similarweb12.p.rapidapi.com/v2/play-store-app-details'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'app_id': app_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def play_store_top_apps(country: Annotated[Union[str, None], Field(description='Country URL code. Example: united-states, albania')] = None,
                        category: Annotated[Union[str, None], Field(description='Category URL code. Example: business')] = None,
                        mode: Annotated[Literal['top-free', 'top-paid', 'top-grossing', None], Field(description=' Example: top-free')] = None,
                        trending: Annotated[Union[bool, None], Field(description=' Example: false')] = None) -> dict:
    '''Play Store / Top Apps'''
    url = 'https://similarweb12.p.rapidapi.com/v2/play-store-top-apps'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'category': category,
        'mode': mode,
        'trending': trending,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def company_details(company_domain: Annotated[str, Field(description='Website / domain name')]) -> dict:
    '''Company Details'''
    url = 'https://similarweb12.p.rapidapi.com/v2/company-details'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'company_domain': company_domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_platforms(country: Annotated[Union[str, None], Field(description='Country URL code. Example: united-states, albania')] = None) -> dict:
    '''Top Platforms'''
    url = 'https://similarweb12.p.rapidapi.com/v2/top-platforms'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_browsers(country: Annotated[Union[str, None], Field(description='Country URL code. Example: united-states, albania')] = None,
                 platform: Annotated[Literal['all-platforms', 'desktop', 'tablet', 'mobile-phone', None], Field(description='Platform Example: all-platforms')] = None) -> dict:
    '''Top Browsers'''
    url = 'https://similarweb12.p.rapidapi.com/v2/top-browsers'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'platform': platform,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_search_engines(country: Annotated[Union[str, None], Field(description='Country URL code. Example: united-states, albania')] = None,
                       platform: Annotated[Literal['all-platforms', 'desktop', 'tablet', 'mobile-phone', None], Field(description='Platform Example: all-platforms')] = None) -> dict:
    '''Top Search Engines'''
    url = 'https://similarweb12.p.rapidapi.com/v2/top-engines'
    headers = {'x-rapidapi-host': 'similarweb12.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'platform': platform,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
