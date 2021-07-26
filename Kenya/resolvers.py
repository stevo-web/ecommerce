from ariadne import QueryType
from Kenya.counties import counties, get_county

query = QueryType()


@query.field('allCounties')
def resolver_all_counties(obj, info):
    return counties


@query.field('county')
def resolve_county(obj, info, code):
    if code > 47 or code <= 0:
        return None
    else:
        return get_county(code)

resolvers = [query]