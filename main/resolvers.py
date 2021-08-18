from ariadne import QueryType, MutationType, convert_kwargs_to_snake_case, snake_case_fallback_resolvers
from django.conf import settings
from cart.cart import Cart
from .models import Product, SubCategory, Category

query = QueryType()
mutation = MutationType()


@query.field('allCategories')
def resolve_all_categories(obj, info):
    categories = Category.objects.all()

    return [
        {
            "id": cat.id,
            "name": cat.name,
            "sub_category": [
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
                        } for prod in Product.objects.filter(category_id=sub.id)
                    ]
                }for sub in SubCategory.objects.filter(category_id=cat.id)
            ]
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


def get_prod(id):
    prod = Product.objects.get(pk=id)
    return {
        "id": prod.id,
        "name": prod.name,
        "description": prod.description,
        "image": f'{settings.SITE_DOMAIN}{prod.image.url}',
        "discount": prod.discount,
        "price": prod.price,
    }


@query.field('cart')
def resolve_cart(_, info):
    request = info.context["request"]
    cart = Cart(request)

    return {
        "count": cart.count(),
        "summary": cart.summary(),
        "items": [
            {
                "id": item.id,
                "quantity": item.quantity,
                "unit": item.unit_price,
                "total": item.total_price,
                "product": get_prod(item.product.id)
            } for item in cart
        ]
    }


@mutation.field('addToCart')
@convert_kwargs_to_snake_case
def resolve_add_to_cart(_, info, prod_id, quantity):
    request = info.context['request']
    cart = Cart(request)
    prod = Product.objects.get(pk=prod_id)
    cart.add(product=prod, unit_price=prod.price, quantity=quantity)
    return {
        "success": True
    }


@mutation.field('removeItem')
@convert_kwargs_to_snake_case
def resolve_remove_item(_, info, prod_id):
    request = info.context["request"]
    cart = Cart(request)
    prod = Product.objects.get(pk=prod_id)
    cart.remove(prod)
    return {
        "success": True
    }


@mutation.field('update')
@convert_kwargs_to_snake_case
def resolve_update(_, info, prod_id, quantity):
    request = info.context["request"]
    cart = Cart(request)
    prod = Product.objects.get(pk=prod_id)
    cart.update(prod, quantity, prod.price)
    return {
        "success": True
    }


resolvers = [query, mutation, snake_case_fallback_resolvers]
