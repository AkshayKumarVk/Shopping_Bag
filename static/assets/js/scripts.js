
//getting the localStorage values
if (localStorage.getItem('cart') == null) {
    var cart = {};

}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart);
}

// increment or decrement cart value

$('.divpr').on('click', 'button.cart', function () {
    productId = this.id.toString();
    console.log(productId);


    if (cart[productId] != undefined) {
        quantity = cart[productId] + 1;
    }
    else {
        quantity = 1;
        prodBrand = document.getElementById('brand' + productId).innerHTML;
        prodPrice = document.getElementById('price' + productId).innerHTML;
        cart[productId] = [quantity, prodBrand, prodPrice];
    }
    updateCart(cart);

});





$('#popCart').popover();

function updatePopover(cart) {
    var popStr = "";
    popStr += "<h5> cart for your items in my shopping cart </h5> <div class='mx-2 my-2'>";
    var i = 1;
    var totalPrice = 0
    for (var item in cart) {
        popStr += "<b>" + i + "</b>";
        popStr += document.getElementById('brand' + item).innerHTML + "..." + "<b>" + cart[item][0] + " </b>" + "Qty" + "<br>";
        i++;
    }
    popStr += "</div>";
    popStr += "<a href='/cart'><button class='btn btn-success' id='clearCart'>Checkout</button></a>  <button class='btn btn-dark' onclick='clearCart()' id='clearCart'>ClearCart</button>"; // Wrapping the button inside a div
    document.getElementById("popCart").setAttribute("data-content", popStr);
    $("#popCart").popover("show");
}





function clearCart() {
    cart = JSON.parse(localStorage.getItem('cart'));
    for (var item in cart) {
        document.getElementById('divpr' + item).innerHTML = '<button id="' + item + '" class="btn btn-outline-primary cart">Add to Cart</button>'
    }
    localStorage.clear();
    cart = {};
    updateCart(cart);
}


function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item][0]
        document.getElementById('divpr' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-success minus'>-</button> <span id='val" + item + "'>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-success plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart);
    document.getElementById("popCart").click();
}


$('.divpr').on("click", "button.minus", function () {
    var itemId = this.id.slice(5);  // Extract the item ID from the minus button ID
    if (cart[itemId][0] > 0) {  // Check if the cart value is greater than 0
        cart[itemId][0] -= 1;  // Decrement the cart value
    }
    document.getElementById('val' + itemId).innerHTML = cart[itemId][0];  // Update the value displayed in the 'val' element
    updateCart(cart);
});

$('.divpr').on("click", "button.plus", function () {
    var itemId = this.id.slice(4);  // Extract the item ID from the plus button ID
    cart[itemId][0] += 1;  // Increment the cart value
    document.getElementById('val' + itemId).innerHTML = cart[itemId][0];  // Update the value displayed in the 'val' element
    updateCart(cart);  // Update the cart and perform any necessary actions
});

