let cart;
let total = 0;



async function updateCheckout() {
  try {
    const response = await axios.get('http://localhost:8000/api/');
    const data = response.data;
    for (let cartItem of data) {
      let name = cartItem["title"]
      let quantity = cartItem["quantity"];
      let price = cartItem["price"]
      total = total + price

      itemString = `<li class="list-group-item d-flex justify-content-between lh-condensed">
        <div>
          <h6 class="my-0">${name}</h6>
          <small class="text-muted">quantity:${quantity}</small>
        </div>
        <span class="text-muted">${price}</span>
        </li>`
      // <li class="list-group-item d-flex justify-content-between">
      //                 <span>Total (USD)</span>
      //                 <strong>${price}</strong>
      //               </li>`
      $('#item-list').append(itemString);
    };

    let totalPrice = `<li class="fs-5 badge bg-success text-wrap list-group-item d-flex fw-bold text-white justify-content-between">
    <span>Total in RUPEES(&#8377;)</span>
    <strong>${total}</strong>
  </li>`
    $('#item-list').append(totalPrice);

    document.querySelector('#totalform').value = parseFloat(total)
    console.log(total)


    $('#items').val(JSON.stringify(cart));


  }
 catch (error) {
  console.log(error);
}

}



updateCheckout()