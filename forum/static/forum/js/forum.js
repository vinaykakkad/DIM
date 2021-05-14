document.addEventListener("DOMContentLoaded", () => {
    $("select").selectpicker();

    document.querySelectorAll(".dropdown-toggle").forEach((element) => {
        element.classList.add("fields");
        element.classList.add("border");
    });
});