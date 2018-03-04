$("#submit").click(function(){
    let username = $("#username").val();
    let password = $("#password").val();
    $.post("/api/login/",
    {
        username : username,
        password : password
    },
    function (data, status) {
        if (data === 'Login success')
        {
            window.location.href="/";
        }
        else
        {
            if (data === 'Error')
            {
                $("#login-info-span").text("密码错误");
            }
            else 
            {
                $('#login-info-span').text("不存在该用户");
            }
        }
        //console.log(data);
        //console.log(status);
    });
  });
