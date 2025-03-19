document.addEventListener("DOMContentLoaded", function() {
    const sanya = document.getElementById("sanya");
    if (sanya.textContent.trim() !== "") {
        setTimeout(() => {
            sanya.textContent = "";
        }, 1000);
    }
});