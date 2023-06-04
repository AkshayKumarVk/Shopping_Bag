// Retrieve cart data from local storage
var cart = JSON.parse(localStorage.getItem('cart'));

// Check if the cart is not empty and has at least one element
if (cart && cart.length > 0) {
    // Access the first element of the cart
    var firstCartItem = cart[0];

    // Get the "cartPill" element by its ID
    var cartPillElement = document.getElementById('cart');

    // Set the value of the "cartPill" element to the first cart item
    cartPillElement.innerHTML = firstCartItem;
}
var sum = 0;
for (var item in cart) {
    sum = sum + cart[item][0]
    document.getElementById('cart').innerHTML = sum;
}