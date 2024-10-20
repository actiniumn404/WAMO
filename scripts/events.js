document.querySelectorAll(".document .name").forEach(e => e.onclick = (ev) => {
    let element = ev.currentTarget;
    element.parentElement.classList.toggle("open")
    element.querySelector("i").classList.toggle("fa-angle-right");
    element.querySelector("i").classList.toggle("fa-angle-down");
})