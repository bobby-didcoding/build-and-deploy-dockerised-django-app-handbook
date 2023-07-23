# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Product


@login_required
def manage_cart(request, product_id, action):
    """
    Function used to handle the adding and removing of items to cart.
    This is also where we handle stock.
    """
    data = {
        "result": "Error",
        "message": "Something went wrong, please try again",
        "redirect": False,
    }

    if (
        request.method == "POST"
        and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    ):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            data["message"] = "Product does not exist"
            return JsonResponse(data)

        cart = request.user.customer_user.cart_customer

        match action:
            case "remove":
                cart.products.remove(product)
            case "add":
                cart.products.add(product)
        cart.save()

        data.update(
            {
                "result": "Success",
                "message": "Cart has been updated",
                "redirect": "/cart/",
            }
        )

        return JsonResponse(data)
    return JsonResponse(data)
