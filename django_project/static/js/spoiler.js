document.querySelectorAll(".spoiler-toggle").forEach(btn => {
    btn.addEventListener("click", () => {
        btn.classList.toggle("active");
        const content = btn.nextElementSibling;
        content.classList.toggle("open");
    });
});