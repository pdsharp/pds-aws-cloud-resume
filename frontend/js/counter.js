const functionApi = 'https://t03oo3i6y4.execute-api.us-west-2.amazonaws.com/Prod/count'

const getVisitCount = () => {
    let count = 30;
    fetch(functionApi)
    .then(response => {
        return response.text()
    })
    .then(response => {
        console.log("Website called function API.",response);
        count = response;
        document.getElementById('counter').innerText = count;
    }).catch(function(error) {
        console.log(error);
      });
    return count;
}

getVisitCount();