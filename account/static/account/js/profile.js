document.addEventListener("DOMContentLoaded", () => {
    $("select").selectpicker();

    document.querySelectorAll(".dropdown-toggle").forEach((element) => {
        element.classList.add("increase-height");
        element.classList.add("border");
    });
});