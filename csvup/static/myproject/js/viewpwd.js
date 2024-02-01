function pwdFunction() {
  var x = document.getElementById("mypwd");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}