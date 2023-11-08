console.log("hi");
const f = document.getElementById('form');
const q = document.getElementById('query');

function submitted(event) {
  event.preventDefault();
  const query = q.value;
  console.log(query);
}

f.addEventListener('submit', submitted);
