const getCount = () => {
  fetch("https://7jsyoco0gb.execute-api.us-west-2.amazonaws.com/Prod/count")
  .then(response => response.text())
  .then(response => document.getElementById('counter').innerText = response)
}
getCount();