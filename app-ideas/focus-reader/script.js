const startButton = document.getElementById("start");
const endButton = document.getElementById("end");
const readerArea = document.getElementById("reader");

let timerId;

function getTextarea() {
  return document.getElementById("text").textContent;
}

function showText(text) {
  const words = text.split(" ");
  let idx = 0;

  function yieldText() {
    if (idx === words.length) {
      clearInterval(timerId);
      return;
    }

    readerArea.textContent = words[idx++];
  }

  const intervalTimeMs = document.getElementById("ms").value;
  timerId = setInterval(() => {
    yieldText();
  }, parseInt(intervalTimeMs));
}

startButton.addEventListener("click", function () {
  const text = getTextarea();
  showText(text);
});

endButton.addEventListener("click", function () {
  document.getElementById("reader").textContent = "　";

  clearInterval(timerId);
});

window.addEventListener("load", function () {
  const text = document.getElementById("text");
  text.textContent =
    "Patterns are integral to software engineering and represent potentially reusable components in program logic. However, patterns aren't used only for program logic, they are exist in other domains such as DevOps, user support, and the user interface. A common user interface pattern is to summarize data in one section of a page that consists of some type of list (like text, images, or icons) that describes or categorizes a set of data. When a list item is clicked, the detailed data behind it is displayed in an adjacent pane on the page. For example, on a real estate site clicking an address in a list of properties for sale displays the details about the property in another part of the page.";
});
