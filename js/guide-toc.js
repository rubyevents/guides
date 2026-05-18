function initGuideToc() {
  const headings = [...document.querySelectorAll(".guide-content h2[id]")];
  const links = [...document.querySelectorAll(".toc__link")];

  if (
    !headings.length ||
    !links.length ||
    !("IntersectionObserver" in window)
  ) {
    return;
  }

  const setActiveLink = (id) => {
    links.forEach((link) => {
      const isActive = link.hash === `#${id}`;
      link.classList.toggle("is-active", isActive);

      if (isActive) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  const visibleHeadings = new Map();
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          visibleHeadings.set(entry.target.id, entry.boundingClientRect.top);
        } else {
          visibleHeadings.delete(entry.target.id);
        }
      });

      const current = [...visibleHeadings.entries()].sort(
        (a, b) => a[1] - b[1],
      )[0];
      if (current) setActiveLink(current[0]);
    },
    { rootMargin: "-20% 0px -65% 0px", threshold: 0 },
  );

  headings.forEach((heading) => observer.observe(heading));
  setActiveLink(headings[0].id);
}

initGuideToc();
