const paymentId = document.querySelector('#payment-id').textContent
const paymentAmt = document.querySelector('#payment-amount').textContent

let options = {
    "key": "rzp_test_4w0xGiYcUxsMvR", // Enter the Key ID generated from the Dashboard
    "amount": paymentAmt, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    "currency": "INR",
    "name": "Music Store",
    "description": "Test Transaction",
    "image": "https://example.com/your_logo",
    "order_id": paymentId, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
    "handler": function (response){
console.log('success')


      
    },

    "theme": {
        "color": "#3399cc"
    }
};
var rzp1 = new Razorpay(options);
rzp1.on('payment.failed', function (response){
        alert(response.error.code);
        alert(response.error.description);
        alert(response.error.source);
        alert(response.error.step);
        alert(response.error.reason);
        alert(response.error.metadata.order_id);
        alert(response.error.metadata.payment_id);
});
document.getElementById('rzp-button1').onclick =  async function(e){
    rzp1.open();
    e.preventDefault();
  

}


