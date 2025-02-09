// function toggleQuantityPopup(event) {
//     event.preventDefault();
//     let popup = event.target.nextElementSibling;
//     popup.style.display = popup.style.display === "block" ? "none" : "block";
// }

// function confirmQuantity(productName) {
//     let quantityInput = event.target.previousElementSibling;
//     let quantity = quantityInput.value;
//     alert(`Добавлено в заказ: ${productName} - ${quantity} шт.`);
//     event.target.parentElement.style.display = "none";
// }


function toggleQuantityPopup(productId) {
    // Показываем или скрываем попап
    let popup = document.getElementById("quantity-popup-" + productId);
    popup.style.display = popup.style.display === "block" ? "none" : "block";
}


function confirmQuantity(productName) {
    let quantityInput = event.target.previousElementSibling;
    let quantity = quantityInput.value;

    // Создаем скрытую форму для отправки данных
    let form = document.createElement('form');
    form.method = 'POST';
    form.action = "{% url 'main:add_to_order' %}";  // URL для добавления в заказ
    form.style.display = 'none';
    
    let productIdField = document.createElement('input');
    productIdField.type = 'hidden';
    productIdField.name = 'product_id';
    productIdField.value = productName;

    let quantityField = document.createElement('input');
    quantityField.type = 'hidden';
    quantityField.name = 'quantity';
    quantityField.value = quantity;

    form.appendChild(productIdField);
    form.appendChild(quantityField);
    document.body.appendChild(form);
    form.submit();

    alert(`Добавлено в заказ: ${productName} - ${quantity} шт.`);
    event.target.parentElement.style.display = "none";
}
