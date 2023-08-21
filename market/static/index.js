
$(document).ready(function(){
    $("#myInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#tables tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });


  $(document).ready(function(){
    $("#myInput1").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#tables1 tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var eyeIcon = document.querySelector(".toggle-password i");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove("fa-eye");
        eyeIcon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove("fa-eye-slash");
        eyeIcon.classList.add("fa-eye");
    }
}



function openNav() {

  var sidebar = document.getElementById("mySidebar");
    var mainContent = document.getElementById("main");
    var header = document.getElementById("myheader");

    if (sidebar.style.width === "259px") {
      sidebar.style.width = "0";
      mainContent.style.marginLeft = "0";
      header.style.marginLeft="100px";
    } else {
      sidebar.style.width = "259px";
      mainContent.style.marginLeft = "259px";
      header.style.marginLeft="13px";
    }
}
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(function () {
  $('[data-toggle="popover"]').popover()
})
$('#example').tooltip(options)


 function openNav() {

  var sidebar = document.getElementById("mySidebar");
    var mainContent = document.getElementById("main");
    var header = document.getElementById("myheader");
    var Sidebar2 =document.getElementById("mySidebar2");

    if (sidebar.style.width === "259px") {
      sidebar.style.width = "0";
      mainContent.style.marginLeft = "0";
      header.style.marginLeft="100px";


    }
     else {
      sidebar.style.width = "259px";
      mainContent.style.marginLeft = "259px";
      header.style.marginLeft="13px";


    }
}

