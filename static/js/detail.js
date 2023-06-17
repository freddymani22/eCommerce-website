let addToCart = document.querySelector('.atc');
const quantity = document.querySelector('#quantity');
const cartInnerValue = document.querySelector('#cart');

async function updateCartPopover() {
    try {
        const response = await axios.get('http://localhost:8000/api/');
        const data = response.data;
        let cartString = "";
        let cartIndex = 1;
        for (let cartItem of data) {
            console.log(cartItem["title"])
            cartString += cartIndex + ') '
            cartString += cartItem["title"] + '-' + cartItem["quantity"]
            cartString += '<br>'
            cartIndex += 1;
        }
        cartString += '<a href="/checkout/" class="text-center btn btn-outline-danger p-1 mt-1" id="checkout">Checkout</a>';

        document.querySelector('#cart').setAttribute('data-bs-content', cartString);
        const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
        console.log(popoverTriggerList);
        const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
        cartInnerValue.textContent= `Cart(${data.length})`

    } catch (error) {
        console.log(error);
    }
}



addToCart.addEventListener('click', async (e) => {
    e.preventDefault()
    const itemId = addToCart.id
    const quantityNum = quantity.value
    const data = { product: itemId, quantity: quantityNum }
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const headers = {
        headers: {
            'X-CSRFToken': csrfToken
        }
    }
    try {
        await axios.post('http://localhost:8000/api/', data, headers)
    }
    catch (error) {
        console.log(error)
    }
    updateCartPopover()
});
updateCartPopover()