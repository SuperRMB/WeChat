/**
 * Created by Administrator on 2019/6/13.
 */
var app = new Vue({
    el: '#app',
    data: {
        inputVal: ''
    },
    watch: {
        inputVal: function (text) {
            if (text.length == 0) {
                document.getElementById('mobile_tip').innerText = ''
            } else if (text.charAt(0) != '1' || text.length < 11) {
                document.getElementById('mobile_tip').innerText = '手机号格式错误'
            } else if (text.length == 11 && text.charAt(0) == '1') {
                document.getElementById('mobile_tip').innerText = ''
                axios.get('{% url "login:mobile_legal" %}', {
                    params: {
                        mobile: text
                    }
                }).then(function (response) {
                    var data = response.data
                    document.getElementById('mobile_tip').innerText = data.msg
                });
            }
        }
    }
})