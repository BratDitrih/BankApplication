function showPopup(accountNumber) {
  var popupContainer = document.getElementById('popupContainer');
  var accountNumberLabel = document.getElementById('accountNumberLabel');
    
  accountNumberLabel.textContent = 'Номер счета: ' + accountNumber;
  popupContainer.style.display = 'block';
  var topUpForm = document.getElementById('topUpForm');
  topUpForm.dataset.account_number = accountNumber;
}

document.addEventListener('DOMContentLoaded', function() {
    var openAccountForm = document.getElementById('openAccountForm');
    
    openAccountForm.addEventListener('submit', function(event) {
      event.preventDefault();
  
      var typeInput = openAccountForm.querySelector('#accountType')
      var userId = openAccountForm.dataset.user_id;
      
      var formData = {
        type: typeInput.value,
        userId: userId
      };
      
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/account/open');
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onload = function() {
          if (xhr.status === 200) {
              window.location.reload();
          } else {
              alert(xhr.responseText);
          }
      };
      xhr.send(JSON.stringify(formData));
    });


    var topUpForm = document.getElementById('topUpForm');
    topUpForm.addEventListener('submit', function(event) {
      event.preventDefault();
      
      var accountNumber = topUpForm.dataset.account_number;
      var phoneNumberInput = document.getElementById('phoneNumber');
      var amountInput = document.getElementById('amount');
      
      var formData = {
          accountNumber: accountNumber,
          phoneNumber: phoneNumberInput.value,
          amount: amountInput.value
      };
      
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/account/topup');
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onload = function() {
          if (xhr.status === 200) {
              var popupContainer = document.getElementById('popupContainer');
              popupContainer.style.display = 'none';
              window.location.reload();
          } else {
              alert(xhr.responseText);
          }
      };
      xhr.send(JSON.stringify(formData));
  });
});
  