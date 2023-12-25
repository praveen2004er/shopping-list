from web_util import get_json_response

def get_product_ids(url_to_fetch):
  json_response = get_json_response(url_to_fetch)
  if json_response:
    ids = [product['tcin'] for product in json_response['data']['search']['products']]
    return ids
  return []

def get_store_positions(url_to_fetch):
  store_positions = []
  json_response = get_json_response(url_to_fetch)
  if json_response:
    store_positions = json_response['data']['product']['store_positions']
    return store_positions
  return store_positions
