window.onbeforeunload = function() {
	const params = new URLSearchParams(window.location.search);
    // 设置你想传递的参数
    var parameter = params.get('username');
 
    // Flask路由URL
    var route = '/close_page';
 
    // 使用fetch API发送请求
    fetch(route, {
        method: 'POST', // 使用POST方法
        headers: {
            'Content-Type': 'application/json' // 设置请求头为JSON
        },
        body: JSON.stringify({ parameter: parameter }) // 将参数作为JSON发送
    })
    .then(response => response.json()) // 解析响应（如果需要）
    .then(data => console.log(data)) // 处理解析后的数据
    .catch(error => console.error('Error:', error)); // 错误处理
};

document.getElementById('submitButton').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单的默认提交行为
    alert("sadbees");
    setTimeout(() => {
        fetch('/getsubmit')
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应异常');
                }
                return response.json(); // 假设服务器返回的是JSON格式数据
            })
            .then(data => {
                // 使用alert弹窗显示返回的数据
                alert(JSON.stringify(data)); // 将数据转换为字符串形式进行显示
            })
            .catch(error => {
                console.error('请求过程中遇到问题:', error);
                alert('请求失败: ' + error.message); // 显示错误信息
            });
    }, 2000);
});


function uploadOK(){
	alert("代码提交成功！")
}
