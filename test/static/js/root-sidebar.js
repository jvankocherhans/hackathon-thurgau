const sidebarToggle = document.getElementById("root-sidebar-toggle");
const sidebar = document.getElementById("root-sidebar");

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("open");
});
