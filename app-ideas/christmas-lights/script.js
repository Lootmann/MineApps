const lightOn = document.getElementById("light-on");
const lightOff = document.getElementById("light-off");
const start = document.getElementById("start");

const lights = {
  red: document.querySelector(".darkred"),
  orange: document.querySelector(".darkorange"),
  yellow: document.querySelector(".darkyellow"),
  green: document.querySelector(".darkgreen"),
  skyblue: document.querySelector(".darkskyblue"),
  blue: document.querySelector(".darkblue"),
  purple: document.querySelector(".darkpurple"),
};

function onLight(colorName) {
  lights[colorName].classList.remove(colorName);
  lights[colorName].classList.add(colorName.replace("dark", ""));
  lights[colorName].classList.add("bright");
}

function onLights() {
  for (const colorName in lights) onLight(colorName);
}

function offLight(colorName) {
  lights[colorName].classList.remove(colorName);
  lights[colorName].classList.remove("bright");
  lights[colorName].classList.add("dark" + colorName);
}

function offLights() {
  for (const colorName in lights) offLight(colorName);
}

lightOn.addEventListener("click", onLights);
lightOff.addEventListener("click", offLights);

let timerIds = {
  red: null,
  orange: null,
  yellow: null,
  green: null,
  skyblue: null,
  blue: null,
  purple: null,
};

start.addEventListener("click", function () {
  console.log(">>> random light on");
  for (const colorName in lights) {
    timerIds[colorName] = setInterval(() => {
      if (Math.random() < 0.5) {
        onLight(colorName);
      } else {
        offLight(colorName);
      }
    }, Math.floor(Math.random() * 500 + 800));
  }
});

document.getElementById("stop").addEventListener("click", function () {
  console.log(">>> stop");
  for (const key in timerIds) {
    clearInterval(timerIds[key]);
  }
});
