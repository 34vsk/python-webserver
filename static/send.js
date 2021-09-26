function send(val) {
  var message = document.getElementById("message").value;
  console.log(message);
  var xhr = new XMLHttpRequest();
  var params = "message=" + message;
  xhr.open("POST", "/contact", true);

  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.onload = function () {
    if (xhr.status == 200) {
      // if everything is ok, navigate to index.html page
      window.location.href = "/";
    }
  };
  xhr.send(params);
}
