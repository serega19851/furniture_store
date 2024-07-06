from django.shortcuts import render
from goods.models import Products


def catalog(request):
    goods: BaseManager[Products] = Products.objects.all()
    context: dict[str, Any] = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product: Products = Products.objects.get(slug=product_slug)
    context: dict[str, Products] = {"product": product}
    return render(request, "goods/product.html", context=context)
