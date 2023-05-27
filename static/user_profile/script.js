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
              location.reload();
          } else {
              alert(xhr.responseText);
          }
      };
      xhr.send(JSON.stringify(formData));
    });
});
  