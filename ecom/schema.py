from ariadne import make_executable_schema, QueryType, load_schema_from_path

from main.resolvers import resolvers as main_resolvers
from Kenya.resolvers import resolvers as counties_resolvers
from users.resolvers import resolvers as user_resolvers

type_def = load_schema_from_path('schema/schema.graphql')
query = QueryType()

resolvers = [query]
resolvers += main_resolvers
resolvers += counties_resolvers
resolvers += user_resolvers

schema = make_executable_schema(type_def, resolvers)
