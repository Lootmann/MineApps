const p = document.getElementById("today");

const getCurrentDate = () => {
  const today = new Date();

  const month = today.getMonth() + 1;
  const day = today.getDate();
  const hour = today.getHours();
  const min = today.getMinutes();
  const sec = today.getSeconds();

  let result = "";
  result += month >= 10 ? month : `0${month}`;
  result += "/";
  result += day >= 10 ? day : `0${day}`;
  result += " ";

  result += hour >= 10 ? hour : `0${hour}`;
  result += ":";
  result += min >= 10 ? min : `0${min}`;
  result += ":";
  result += sec >= 10 ? sec : `0${sec}`;

  return result;
};

const timerId = setInterval(() => {
  p.textContent = getCurrentDate();
}, 1000);

window.addEventListener("load", () => {
  p.textContent = getCurrentDate();
});
