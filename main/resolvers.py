from ariadne import QueryType

query = QueryType()


@query.field('hello')
def resolve_hello(obj, info, name):
    return f'hello {name}'


resolvers = [query]
