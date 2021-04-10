let question = document.querySelector("#text_field")
question.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("Vous avez bien appuyé sur envoyer");
})
