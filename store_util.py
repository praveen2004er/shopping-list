from web_util import get_json_response
from web_util import dict_to_query_params
from util import project_dict

def get_store_positions_for_query(config, query):
    store_positions = {}
    url_prefix = 'https://redsky.target.com/redsky_aggregations/v1/web/product_fulfillment_v1'
    query_params_needed = ['key','is_bot','required_store_id','has_required_store_id','user_agent','visitor_id']
    query_params_dict = project_dict(config, query_params_needed)
    product_ids = get_product_ids_for_query(config, query)

    for product_id in product_ids:
        query_params_dict['tcin'] = str(product_id)
        query_params_string = dict_to_query_params(query_params_dict)
        url_to_fetch = url_prefix + '?' + query_params_string
        json_response = get_json_response(url_to_fetch)
        if json_response:
            for pos in json_response['data']['product']['store_positions']:
                aisle_key = pos['block'] + str(pos['aisle']) 
                store_positions[aisle_key] = pos
    return store_positions

def get_product_ids_for_query(config, query):
  url_prefix = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2'
  query_params_needed = ['key','channel','count','new_search','platform','pricing_store_id','store_ids','user_agent','visitor_id']
  query_params_dict = project_dict(config, query_params_needed)
  query_params_dict['keyword'] = query
  query_params_dict['page'] = '%2Fs%2F'+query
  query_params_string = dict_to_query_params(query_params_dict)
  url_to_fetch = url_prefix + '?' + query_params_string
  return get_product_ids(url_to_fetch)


def get_product_ids(url_to_fetch):
  json_response = get_json_response(url_to_fetch)
  if json_response:
    ids = [product['tcin'] for product in json_response['data']['search']['products']]
    return ids
  return []
