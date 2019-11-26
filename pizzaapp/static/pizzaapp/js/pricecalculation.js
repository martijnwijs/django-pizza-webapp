//var orderform = document.forms["orderform"];
alert('yo');
// enter all the menu items in a javascript list
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input').onclick= getPrice;
}
var items =[
    {% for item in Items %}
    {
        type: item.type,
        size: item.size,
        price: item.price,
    }
    {% endfor %}
];


// returns the price of the current product
function getPrice()
{
    alert('yo');
    // get form data
    var orderform = document.forms["orderform"];
    var selectedsize = orderform.elements["size"];
    var selectedtype = orderform.elements["type"];

    // loop over items to find base price
    for (item in items){
        if (item.type == selectedtype && item.size == selectedsize){
            var baseprice = item.price;
        }
    }
    
    // add the toppingprice and extra options
    // add the quantity
    // insert result into form
    document.querySelector('#totalPrice').innerHTML = "Total Price $" + baseprice;
}
