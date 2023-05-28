function showPopup(accountNumber) {
  var popupContainer = document.getElementById('popupContainer');
  var accountNumberLabel = document.getElementById('accountNumberLabel');
    
  accountNumberLabel.textContent = 'Номер счета: ' + accountNumber;
  popupContainer.style.display = 'block';
  var topUpForm = document.getElementById('topUpForm');
  topUpForm.dataset.account_number = accountNumber;
}

function showSection(sectionId) {
  var sections = document.getElementsByClassName('section');
  for (var i = 0; i < sections.length; i++) {
    sections[i].style.display = 'none';
  }

  var selectedSection = document.getElementById(sectionId);
  if (selectedSection) {
    selectedSection.style.display = 'block';
  }
}

function exit() {
  window.location.href = '/';
}

document.addEventListener('DOMContentLoaded', function() {
    showSection("accounts");
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

    var transferForm = document.getElementById('transferForm');
    transferForm.addEventListener('submit', function(event) {
      event.preventDefault()

      var fromAccountSelect = document.getElementById('fromAccount');
      var toAccountInput = document.getElementById('toAccount');
      var amountInput = document.getElementById('transferAamount');

      var formData = {
        fromAccountNumber: fromAccountSelect.value,
        toAccountNumber: toAccountInput.value,
        amount: amountInput.value
      }

      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/account/transfer');
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onload = function() {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText).status;
          switch (response) {
            case 'Перевод выполнен успешно':
              alert('Перевод выполнен успешно');
              window.location.reload();
              break;
            case 'Недостаточно средств':
              alert('На счету недостаточно средств');
              break;
            case 'Счет для перевода не найден':
              alert('Счет для перевода не найден');  
              break;
            default:
              break;
          }
        }
        else {
          alert(xhr.responseText);
        }
      };
      xhr.send(JSON.stringify(formData));
    });
});
  