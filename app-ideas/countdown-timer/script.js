/**
 * result
 */
const result = document.getElementById("result");

const startButton = document.getElementById("start-timer");
startButton.addEventListener("click", function () {
  showRest(dateTimePicker.value);
});

/**
 *
 * @param {number} year
 * @param {number} month
 * @param {number} day
 * @param {number} hour
 * @param {number} min
 * @param {number} sec
 * @returns
 */
function toSec(year, month, day, hour, min, sec) {
  return (
    year * 12 * 30 * 24 * 60 * 60 +
    month * 30 * 24 * 60 * 60 +
    day * 24 * 60 * 60 +
    hour * 60 * 60 +
    min * 60 +
    sec
  );
}

const divmod = (x, y) => [Math.floor(x / y), x % y];

/**
 *
 * @param {number} sec
 */
function toDate(sec) {
  console.log(">>> toDate");
  let year, month, day, hour, min;
  [year, sec] = divmod(sec, 12 * 30 * 24 * 60 * 60);
  [month, sec] = divmod(sec, 30 * 24 * 60 * 60);
  [day, sec] = divmod(sec, 24 * 60 * 60);
  [hour, sec] = divmod(sec, 60 * 60);
  [min, sec] = divmod(sec, 60);

  let result = "";

  if (year >= 1) {
    result += `${year}year `;
  }

  if (month >= 1) {
    result += `${month}month `;
  }

  if (day >= 1) {
    result += `${day}day `;
  }

  if (hour >= 1) {
    result += `${hour}hour `;
  }

  if (min >= 1) {
    result += `${min}min `;
  }

  result += `${sec}sec`;

  return result;
}

// 2022-10-07T20:09
function showRest(dateTime) {
  const year = parseInt(dateTime.substring(0, 4));
  const month = parseInt(dateTime.substring(5, 7));
  const day = parseInt(dateTime.substring(8, 10));
  const hour = parseInt(dateTime.substring(11, 13));
  const min = parseInt(dateTime.substring(14, 16));

  const birthdaySec = toSec(year, month, day, hour, min, 0);

  // closure
  const timerId = setInterval(() => {
    // get current date
    const current = new Date();

    const currentSec = toSec(
      current.getFullYear(),
      current.getMonth() + 1,
      current.getDate(),
      current.getHours(),
      current.getMinutes(),
      current.getSeconds()
    );

    result.textContent = toDate(birthdaySec - currentSec);
  }, 1000);
}

/**
 * date time picker
 */
const dateTimePicker = document.getElementById("date");

// init datetime local with current date
window.addEventListener("load", function () {
  const now = new Date();
  const offset = now.getTimezoneOffset() * 60000;
  const delta = 1000 * 60 * 60 * 24 * 30 * 7;
  const adjustedDate = new Date(now.getTime() + delta - offset);
  const formattedDate = adjustedDate.toISOString().substring(0, 16);
  dateTimePicker.value = formattedDate;
});
