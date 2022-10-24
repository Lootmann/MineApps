// border
const box = document.querySelector(".box");

const borderProperty = {
  isOn: true,
  topLeft: 0,
  topRight: 0,
  bottomLeft: 0,
  bottomRight: 0,

  topLeftRadius: 0,
  topRightRadius: 0,
  bottomLeftRadius: 0,
  bottomRightRadius: 0,
};

function renderBorderBox() {
  const {
    topLeft,
    topRight,
    bottomLeft,
    bottomRight,
    topLeftRadius,
    topRightRadius,
    bottomLeftRadius,
    bottomRightRadius,
  } = borderProperty;

  let radius = "";
  radius += topLeft === 0 ? "0 " : `${topLeft}px `;
  radius += topRight === 0 ? "0 " : `${topRight}px `;
  radius += bottomLeft === 0 ? "0 " : `${bottomLeft}px `;
  radius += bottomRight === 0 ? "0" : `${bottomRight}px`;

  box.style.border = "medium solid black";
  box.style.borderRadius = radius;

  box.style.borderTopLeftRadius = `${topLeftRadius}px 20px`;
  box.style.borderTopRightRadius = `${topRightRadius}px 20px`;
  box.style.borderBottomLeftRadius = `${bottomLeftRadius}px 20px`;
  box.style.borderBottomRightRadius = `${bottomRightRadius}px 20px`;
}

document.getElementById("top-left").addEventListener("input", function () {
  borderProperty.topLeft = Number(this.value);
  renderBorderBox();
});

document.getElementById("top-right").addEventListener("input", function () {
  borderProperty.topRight = Number(this.value);
  renderBorderBox();
});

document.getElementById("bottom-left").addEventListener("input", function () {
  borderProperty.bottomLeft = Number(this.value);
  renderBorderBox();
});

document.getElementById("bottom-right").addEventListener("input", function () {
  borderProperty.bottomRight = Number(this.value);
  renderBorderBox();
});

document
  .getElementById("top-right-radius")
  .addEventListener("input", function () {
    borderProperty.topRightRadius = Number(this.value);
    renderBorderBox();
  });

document
  .getElementById("top-left-radius")
  .addEventListener("input", function () {
    borderProperty.topLeftRadius = Number(this.value);
    renderBorderBox();
  });

document
  .getElementById("bottom-right-radius")
  .addEventListener("input", function () {
    borderProperty.bottomRightRadius = Number(this.value);
    renderBorderBox();
  });

document
  .getElementById("bottom-left-radius")
  .addEventListener("input", function () {
    borderProperty.bottomLeftRadius = Number(this.value);
    renderBorderBox();
  });
