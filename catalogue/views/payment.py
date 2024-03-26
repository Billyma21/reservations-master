#<!-- Bilal ma - Views paiement -->

from django.shortcuts import render, redirect, get_object_or_404
from catalogue.models import Cart, Order
from catalogue.forms import PaymentForm
from django.contrib.auth.decorators import login_required

@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            cart_items = request.session.get('cart', {})
            total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
            
            # Avec les articles commandés
            order_items = [{'title': item['title'], 'quantity': item['quantity'], 'price': item['price'], 'total_price': item['quantity'] * item['price']} for item in cart_items.values()]
            
            order = Order.objects.create(
                user=request.user,
                total_amount=total_price,
                payment_method=payment_method,
                payment_confirmed=False,
                items=order_items
            )
            order.save()
            request.session['cart'] = {}
            return redirect('payment_success')
    else:
        form = PaymentForm()

    cart_items = request.session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render(request, 'cart/payment_information.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})
# Hostirque de commande & détaille de celle ci
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/order_detail.html', {'order': order})


@login_required
def order_history(request):
    # Récupérer l'historique des commandes de l'utilisateur connecté
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'cart/order_history.html', {'orders': orders})


@login_required
def payment_success(request):
    last_order = Order.objects.last()
    return render(request, 'cart/payment_success.html', {'order': last_order})

def checkout_summary(request):
    cart = Cart(request)
    cart_items = request.session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render(request, 'cart/checkout_summary.html', {'cart_items': cart_items, 'total_price': total_price})