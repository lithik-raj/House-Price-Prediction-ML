// ===============================
// HOUSE PRICE PREDICTION UI
// ===============================

// Smooth page load animation

window.addEventListener("load", () => {
  document.body.style.opacity = "1";
});

// ===============================
// FORM SUBMIT LOADING EFFECT
// ===============================

const form = document.querySelector("form");

if (form) {
  form.addEventListener("submit", () => {
    const button = document.querySelector(".predict-btn");

    button.innerHTML = "Predicting...";

    button.disabled = true;
  });
}

// ===============================
// INPUT ANIMATION
// ===============================

const inputs = document.querySelectorAll("input, select");

inputs.forEach((input) => {
  input.addEventListener("focus", () => {
    input.style.transform = "scale(1.03)";
  });

  input.addEventListener("blur", () => {
    input.style.transform = "scale(1)";
  });
});

// ===============================
// SCROLL REVEAL ANIMATION
// ===============================

const revealElements = document.querySelectorAll(
  ".glass-card, .feature-card, .about",
);

window.addEventListener("scroll", () => {
  revealElements.forEach((element) => {
    const windowHeight = window.innerHeight;

    const revealTop = element.getBoundingClientRect().top;

    if (revealTop < windowHeight - 100) {
      element.style.opacity = "1";

      element.style.transform = "translateY(0px)";
    }
  });
});

// ===============================
// HERO BUTTON EFFECT
// ===============================

const heroButton = document.querySelector(".hero-btn");

if (heroButton) {
  heroButton.addEventListener("mouseover", () => {
    heroButton.style.boxShadow = "0px 0px 20px rgba(255,255,255,0.7)";
  });

  heroButton.addEventListener("mouseout", () => {
    heroButton.style.boxShadow = "none";
  });
}
