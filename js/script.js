document.querySelectorAll(".offer-btn").forEach(function (button) {
    button.addEventListener("click", function () {
        var isOpen = document.getElementById(button.dataset.target).classList.toggle("open");
        button.textContent = isOpen ? "Skrýt nabídku" : "Zobrazit nabídku";
        button.setAttribute("aria-expanded", isOpen);
    });
});

var form = document.getElementById("contact-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    document.getElementById("form-message").textContent =
        "Děkujeme, " + form.elements.namedItem("name").value + "! Ozveme se vám do 24 hodin.";
    form.reset();
});
