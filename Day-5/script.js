// alert("Script Working");

var api_url = "https://jsonplaceholder.typicode.com/users";

function getApiData(URL) {
  // Logic to call API

      setTimeout(() => {
        
         fetch(URL)
           .then((res) => {
             return res.json();
           })
           .then((data) => displayData(data))
           .catch((err) => console.log(err));

    }, 5000);


}

getApiData(api_url);

function displayData(serverData) {
  console.log(serverData);

  for (var i of serverData) {
    // New Row created
    var newTr = document.createElement("tr");

    // New Columns created
    var newTd1 = document.createElement("td");
    var newTd2 = document.createElement("td");
    var newTd3 = document.createElement("td");
    var newTd4 = document.createElement("td");

    // Insert data in new Columns
    newTd1.innerText = "" + i.id;
    newTd2.innerText = "" + i.name;
    newTd3.innerText = "" + i.email;
    newTd4.innerText = "" + i.phone;

    // Connect column to row
    newTr.appendChild(newTd1);
    newTr.appendChild(newTd2);
    newTr.appendChild(newTd3);
    newTr.appendChild(newTd4);

    document.getElementById("myTable").appendChild(newTr);
  }
}
