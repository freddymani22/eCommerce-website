  let cart;
    if (localStorage.getItem('cart') == null) {
        cart = {};
    } else {
        cart = JSON.parse(localStorage.getItem('cart'));
    }

    $(document).on('click', '.atc', function () {
        const item_id = this.id.toString();

    if (cart[item_id] != undefined) {
        quantity = cart[item_id][0] + 1;
    cart[item_id][0] = quantity;
    cart[item_id][2] = cart[item_id][2] + parseFloat(document.querySelector("#price"+item_id).innerText);

        } else {
        quantity = 1;
    name1 = document.querySelector(`#nm${item_id}`).innerText;
    price = parseFloat(document.querySelector("#price"+item_id).innerText);
    cart[item_id] = [quantity, name1, price];
        }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.querySelector('#cart').innerText = `Cart(${Object.keys(cart).length})`;

    });
    window.addEventListener('load', function () {
        localStorage.getItem('cart');
    document.querySelector('#cart').innerText = `Cart(${Object.keys(cart).length})`;
    });


    function displayCart(cart) {
        let cartString = "";
    let cartIndex = 1;
    for (let item in cart) {

        cartString += cartIndex + ') '
            cartString += cart[item][1] + '-' + cart[item][0]
    cartString += '<br>'
        cartIndex += 1;
        }

        cartString += '<a href="/checkout/" class="text-center btn btn-outline-danger p-1 mt-1" id="checkout">Checkout</a>';

        document.querySelector('#cart').setAttribute('data-bs-content', cartString);
        const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
        const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
    }

        displayCart(cart);


