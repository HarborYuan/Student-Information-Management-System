$(document).ready(function(){
  $('select').formSelect();
});

$("#submit").click(function(){
  let username = $("#username").val();
  let idcard = $("#idcard").val();
  let password1 = $("#password1").val();
  let password2 = $("#password2").val();
  let major = $("#major").val();
  let email = $("#email").val();
  let phone = $("#phone").val();
  let isGirl = $("#isGirl").prop("checked");
  console.log(username);
  console.log(idcard);
  console.log(password1);
  console.log(password2);
  console.log(major);
  console.log(email);
  console.log(phone);
  console.log(isGirl);
});