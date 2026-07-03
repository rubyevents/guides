function initToc() {
  const headings = [
    ...document.querySelectorAll(
      ".guide-content h2[id], .interview-anchor[id]",
    ),
  ];
  const links = [...document.querySelectorAll(".toc__link")];

  if (!headings.length || !links.length) {
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

  // Active = the last heading whose top has scrolled above the activation line
  // (20% down the viewport). Computed from live positions so it stays correct
  // in both directions and regardless of how far apart the headings sit.
  const updateActive = () => {
    const line = window.innerHeight * 0.2;
    let currentId = headings[0].id;

    for (const heading of headings) {
      if (heading.getBoundingClientRect().top <= line) {
        currentId = heading.id;
      } else {
        break;
      }
    }

    setActiveLink(currentId);
  };

  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      updateActive();
      ticking = false;
    });
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  updateActive();
}

initToc();
