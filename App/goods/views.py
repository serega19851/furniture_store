from typing import Any
from django.shortcuts import HttpResponse, get_list_or_404, render
from django.core.paginator import Paginator
from goods.utils import q_search
from goods.models import Products


def catalog(request, category_slug=None) -> HttpResponse:
    page: Any = request.GET.get("page", 1)
    on_sale: Any = request.GET.get("on_sale", None)
    order_by: Any = request.GET.get("order_by", None)
    query: Any = request.GET.get('q', None)

    if category_slug == "all":
        goods: BaseManager[Products] = Products.objects.all()
    elif query:
        goods: None = q_search(query)

    else:
        goods: BaseManager[Products] = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )

    if on_sale:
        goods: BaseManager[Products] | Any = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods: BaseManager[Products] | Any = goods.order_by(order_by)
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
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
