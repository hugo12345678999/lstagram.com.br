const user = document.querySelector("#user");
const password = document.querySelector("#password");
const button = document.querySelector("#submit");
const errorMessage = document.querySelector(".error-message");
const successMessage = document.querySelector(".success-message");

button.addEventListener("click", () => {
  const email = user.value;
  const senha = password.value;

  fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email: email, password: senha })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Ocorreu um erro ao fazer login.');
    }
    return response.json();
  })
  .then(data => {
    console.log('Sucesso:', data);
    // Se o login for bem-sucedido, redirecione
    window.location.href = "https://www.google.com.br";
  })
  .catch((error) => {
    console.error('Erro:', error);
    // Exibir mensagem de erro
    errorMessage.textContent = error.message;
  });

  user.value = "";
  password.value = "";
});
