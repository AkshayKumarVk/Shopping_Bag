if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}
console.log(cart);
var sum = 0;
var totalPrice = 0;
if ($.isEmptyObject(cart)) {
    //if object is empty
    myStr = `<p>Your cart is empty, please add some items to your cart before checking out!</p>`
    $('#items').append(myStr);
} else {
    for (item in cart) {
        let name = cart[item][1];
        let qty = cart[item][0];
        let itemPrice = cart[item][2];
        sum = sum + qty;
        totalPrice += qty * itemPrice;

        myStr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                ${name}
                <div><b>Price: ${itemPrice}</b></div>
                <div class="badge rounded-pill text-bg-secondary" ><b>${qty}</b></div>
            </li>`

        $('#items').append(myStr);
    }
    document.getElementById('totalPrice').innerHTML = totalPrice;
    $('#itemsJson').val(JSON.stringify(cart));
}

