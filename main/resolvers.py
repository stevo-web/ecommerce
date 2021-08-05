from ariadne import QueryType, convert_kwargs_to_snake_case, snake_case_fallback_resolvers
from django.conf import settings
from cart.cart import Cart
from .models import Product, SubCategory, Category

query = QueryType()


@query.field('allCategories')
def resolve_all_categories(obj, info):
    categories = Category.objects.all()

    return [
        {
            "id": cat.id,
            "name": cat.name
        }for cat in categories
    ]


@query.field('allSubCategories')
def resolve_all_sub_categories(obj, info, id):
    subs = SubCategory.objects.filter(category_id=id)
    return [
        {
            "id": sub.id,
            "name": sub.name,
            "products": [
                {
                    "id": prod.id,
                    "name": prod.name,
                    "description": prod.description,
                    "image": f'{settings.SITE_DOMAIN}{prod.image.url}',
                    "discount": prod.discount,
                    "price": prod.price,
                }for prod in Product.objects.filter(category_id=sub.id)
            ]
        }for sub in subs
    ]



@query.field('allProducts')
def resolve_all_products(obj, info):
    products = Product.objects.all()
    return [
        {
            "id": prod.id,
            "name": prod.name,
            "description": prod.description,
            "image": f'{settings.SITE_DOMAIN}{prod.image.url}',
            "discount": prod.discount,
            "price": prod.price,
        }for prod in products
    ]


@query.field("product")
@convert_kwargs_to_snake_case
def resolve_product(obj, info, prod_id):
    prod = Product.objects.get(pk=prod_id)

    return {
        "id": prod.id,
        "name": prod.name,
        "description": prod.description,
        "image": f'{settings.SITE_DOMAIN}{prod.image.url}',
        "discount": prod.discount,
        "price": prod.price,
    }

# cart mutation resolvers


resolvers = [query, snake_case_fallback_resolvers]
