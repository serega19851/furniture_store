from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator
from goods.models import Products


def catalog(request, category_slug, page=1):
    if category_slug== 'all':
        goods: BaseManager[Products] = Products.objects.all()
    else:   
        goods: BaseManager[Products] = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, Any] = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product: Products = Products.objects.get(slug=product_slug)
    context: dict[str, Products] = {"product": product}
    return render(request, "goods/product.html", context=context)
