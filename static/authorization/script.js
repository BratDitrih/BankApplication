document.addEventListener('DOMContentLoaded', function() {
    
    loginForm.addEventListener('submit', function(event) {
      event.preventDefault();
  
      var loginForm = document.getElementById('loginForm');

      var usernameInput = loginForm.querySelector('#username')
      var passwordInput = loginForm.querySelector('#password')
      
      var formData = {
        username: usernameInput.value,
        password: passwordInput.value
      };
      
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/login');
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onload = function() {
          if (xhr.status === 200) {
              var userId = JSON.parse(xhr.responseText).user_id;
              window.location.href = '/user/' + userId;
          } else {
              alert("Неправильный логин или пароль");
          }
      };
      xhr.send(JSON.stringify(formData));
  
      usernameInput.value = '';
      passwordInput.value = '';
    });

    registerForm.addEventListener('submit', function(event) {
      event.preventDefault();

      var registerForm = document.getElementById('registerForm');

      var usernameInput = registerForm.querySelector('#username')
      var passwordInput = registerForm.querySelector('#password')
      var emailInput = registerForm.querySelector('#email')
      var phoneInput = registerForm.querySelector('#phone')

      var formData = {
        username: usernameInput.value,
        password: passwordInput.value,
        email: emailInput.value,
        phone: phoneInput.value
      };
      
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/register');
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onload = function() {
        if (xhr.status === 200) {
          var userId = JSON.parse(xhr.responseText).user_id;
          window.location.href = '/user/' + userId;
        }
        else {
          alert("Неправильный логин или пароль");
        }
      };
      xhr.send(JSON.stringify(formData));

      usernameInput.value = '';
      passwordInput.value = '';
      emailInput.value = '';
      phoneInput.value = '';
    });
    
    var loginButton = document.getElementById('loginButton');
    var loginContainer = document.getElementById('loginContainer');
    
    var registerButton = document.getElementById('registerButton');
    var registerContainer = document.getElementById('registerContainer');

    loginButton.addEventListener('click', function() {
      loginContainer.style.display = 'block';
      registerContainer.style.display = 'none';
      registerButton.style.display = 'block';
      loginButton.style.display = 'none';
    });
    
    registerButton.addEventListener('click', function() {
      loginContainer.style.display = 'none';
      registerContainer.style.display = 'block';
      registerButton.style.display = 'none';
      loginButton.style.display = 'block';
    });
});
  