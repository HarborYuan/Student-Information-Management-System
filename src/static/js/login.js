$("#submit").click(function(){
    let username = $("#username").val();
    let password = $("#password").val();
    $.post("/api/login/",
    {
        username : username,
        password : password
    },
    function (data, status) {
        console.log(data);
        console.log(status);
    });
  });
