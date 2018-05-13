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
  /*
  console.log(username);
  console.log(idcard);
  console.log(password1);
  console.log(password2);
  console.log(major);
  console.log(email);
  console.log(phone);
  console.log(isGirl);
*/
  if(username=="" || username==null)
  {
    $("#register-info-span").text("用户名不得为空");
    return;
  }

  if(idcard=="" || idcard==null)
  {
    $("#register-info-span").text("身份证号不得为空");
    return;
  }

  if(password1=="" || password1==null)
  {
    $("#register-info-span").text("密码不得为空");
    return;
  }
  if(password2=="" || password2==null)
  {
    $("#register-info-span").text("重复密码不得为空");
    return;
  }
  if(password1!=password2)
  {
    $("#register-info-span").text("两次输入不一致");
    return;
  }
  if(major==null)
  {
    $("#register-info-span").text("请选择专业");
    return;
  }
  if(email=="" || password2==null)
  {
    $("#register-info-span").text("邮箱不得为空");
    return;
  }
  if(phone=="" || phone==null)
  {
    $("#register-info-span").text("手机号码不得为空");
    return;
  }
  $("#register-info-span").text("");
  $.post("/api/register/",
    {
        username : username,
        idcard : idcard,
        password1 : password1,
        password2 : password2,
        major : major,
        email : email,
        phone : phone,
        isGirl : isGirl
    },
    function (data, status) {
        switch(data)
        {
          case "0":
            $("#register-info-span").text("");
            window.location.href="/";
            break;
          case "1":
            $("#register-info-span").text("不存在该学生");
            break;
          case "2":
            $('#register-info-span').text("身份证与学号不匹配");
            break;
          case "3":
            $('#register-info-span').text("两次输入密码不一致");
            break;
          case "4":
            $('#register-info-span').text("密码太短，请重新设置");
            break;
          case "5":
            $('#register-info-span').text("您已注册过，请勿重新注册");
            break;
          case "6":
            $('#register-info-span').text("请选择专业 500");
            break;
          case "7":
            $('#register-info-span').text("手机号码格式错误");
            break;
          case "8":
            $('#register-info-span').text("邮箱格式错误");
            break;
          case "9":
            $('#register-info-span').text("未知错误");
            break;
          default:
        }
    });
});