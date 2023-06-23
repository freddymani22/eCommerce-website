let cart;
let total = 0;



async function updateCheckout() {
  try {
    const response = await axios.get('http://localhost:8000/api/');
    const data = response.data;

    $('#item-list').empty();
    const table = $('<table>').addClass('table-responsive');
    const tbody = $('<tbody>');
    total = 0;
    for (let cartItem of data) {
      let name = cartItem["title"]
      let quantity = cartItem["quantity"];
      let price = cartItem["price"]
      let id = cartItem["id"]
      total = total + price

      const row = $('<tr>');
      const nameCell = $('<td>').html(`<h6>${name}</h6><small class="text-muted">quantity:${quantity}
      </small>`);
      const priceCell = $('<td>').html(`<span class="text-muted">Rs.${price}</span>`);
      const deleteCell = $('<td>').html(`<i type="submit" id="${id}" class="delete-item fa fa-trash-o ms-2" style="font-size:33px;color:red"></i>`);

      row.append(nameCell, priceCell, deleteCell);
      tbody.append(row);
    }

    table.append(tbody);


    $('#item-list').append(table);
    if(total>0){
    let totalPrice = `<li class="fs-4 font-monospace p-3 badge bg-success text-wrap list-group-item d-flex fw-bold text-white justify-content-center">
    <span>Total in RUPEES</span>
    <strong class='ms-2'>Rs. ${total}</strong>
  </li>`
    $('#item-list').append(totalPrice);
    }
    document.querySelector('#totalform').value = parseFloat(total)


    $('#items').val(JSON.stringify(cart));
    if(total===0){
      const checkout = document.querySelector('.all-items');
      checkout.innerHTML = '';
      const noItemNotice = document.createElement('h3');
      noItemNotice.classList.add('text-center', 'mt-3')
      noItemNotice.textContent = 'Add Items to the cart to checkout';
      checkout.appendChild(noItemNotice);

    }

  }
  catch (error) {
    console.log(error);
  }

}

async function deleteCartItem(itemId, headers) {
  try {
    await axios.delete(`http://localhost:8000/api/${itemId}`, headers);
    // Call updateCheckout after successful deletion
    updateCheckout();
  } catch (error) {
    console.log(error);
  }
}

$(document).on('click', '.delete-item', async function (e) {
  e.preventDefault();
  console.log('clicked');
  const itemId = $(this).attr('id');
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const headers = {
            headers: {
                'X-CSRFToken': csrfToken
            }
        }
  await deleteCartItem(itemId, headers);
});



updateCheckout()



