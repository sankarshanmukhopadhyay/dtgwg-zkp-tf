document.addEventListener("DOMContentLoaded", async function () {
  if (!window.mermaid) return;

  document.querySelectorAll("pre > code.language-mermaid").forEach(function (code) {
    const container = document.createElement("div");
    container.className = "mermaid";
    container.textContent = code.textContent;
    code.parentElement.replaceWith(container);
  });

  window.mermaid.initialize({
    startOnLoad: false,
    securityLevel: "strict",
    theme: "neutral"
  });

  await window.mermaid.run({ querySelector: ".mermaid" });
});
