function initMobileStickyHeader() {
  const header = document.querySelector("[data-mobile-sticky-header]");
  const toggle = document.querySelector("[data-mobile-menu-toggle]");
  const menu = document.querySelector("[data-mobile-menu]");

  if (!header || !toggle || !menu) return;

  const closeMenu = () => {
    toggle.setAttribute("aria-expanded", "false");
    menu.hidden = true;
  };

  const openMenu = () => {
    toggle.setAttribute("aria-expanded", "true");
    menu.hidden = false;
  };

  const updateHeaderVisibility = () => {
    const isMobile = window.matchMedia("(max-width: 767px)").matches;
    const hasScrolled = window.scrollY > 160;

    header.toggleAttribute("data-visible", isMobile && hasScrolled);

    if (!isMobile) closeMenu();
  };

  toggle.addEventListener("click", () => {
    const isExpanded = toggle.getAttribute("aria-expanded") === "true";

    if (isExpanded) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  menu.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMenu();
  });

  document.addEventListener("click", (event) => {
    if (header.contains(event.target)) return;
    closeMenu();
  });

  window.addEventListener("scroll", updateHeaderVisibility, { passive: true });
  window.addEventListener("resize", updateHeaderVisibility);
  updateHeaderVisibility();
}

initMobileStickyHeader();
