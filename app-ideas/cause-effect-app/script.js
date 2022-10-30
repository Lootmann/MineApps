function makeid(length) {
  var result = "";
  var characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

function makeTelephone() {
  let result = "";
  const characters = "0123456789";
  for (let i = 0; i < 4; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

const users = [];

function renderUl() {
  const ul = document.createElement("ul");

  for (let i = 0; i < users.length; ++i) {
    let li = document.createElement("li");
    let span = document.createElement("span");
    span.textContent = `name: ${users[i].name}\nstreet: ${users[i].street}, telephone: ${users[i].telephone}`;
    span.style.cssText =
      "border: 1px solid black; padding: 10px; margin: 10px;";

    li.classList.add("li");
    li.appendChild(span);

    li.addEventListener("click", function () {
      const elem = this.firstChild;

      const p = document.getElementById("show-info");
      p.textContent = elem.textContent;
    });

    ul.classList.add("ul");
    ul.appendChild(li);
  }

  const personList = document.getElementById("person-list");
  while (personList.firstChild) {
    personList.removeChild(personList.firstChild);
  }

  personList.appendChild(ul);
}

window.addEventListener("load", () => {
  // init
  for (let i = 0; i < 10; i++) {
    users.push({
      name: makeid(10),
      street: makeid(30),
      telephone: `090-${makeTelephone()}-${makeTelephone()}`,
    });
  }

  renderUl();
});
