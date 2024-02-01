function searchemail() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("mySearch3");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those that don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[4]; // Change this index to match the column you want to search in
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }

<!--  document.getElementById("myButton").addEventListener("click", searchTable);-->

function searchprn() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("mySearch2");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those that don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[5]; // Change this index to match the column you want to search in
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }

<!--  document.getElementById("myButton").addEventListener("click", searchTable);-->

function searchname() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("mySearch1");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those that don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1]; // Change this index to match the column you want to search in
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }

<!--  document.getElementById("myButton").addEventListener("click", searchTable);-->

