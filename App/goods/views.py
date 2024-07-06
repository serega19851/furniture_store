from django.shortcuts import get_list_or_404, render
from goods.models import Products


def catalog(request, category_slug):
    if category_slug== 'all':
        goods: BaseManager[Products] = Products.objects.all()
    else:   
        goods: BaseManager[Products] = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    context: dict[str, Any] = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product: Products = Products.objects.get(slug=product_slug)
    context: dict[str, Products] = {"product": product}
    return render(request, "goods/product.html", context=context)
