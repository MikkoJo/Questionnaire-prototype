
var softgis = {};
softgis.proto = (function() {
    return {
        "init": function () {
            $(".submit").click(function(){
                $.ajax({
                    url: "",
                    type: "POST",
                    data: $('form[name=questform]').serializeArray(),
                    contentType: "application/json",
                    success: function(data) {
                        console.log(data);
                        if(callback_function !== undefined) {
                            callback_function(data);
                            }
                        },
                    error: function(e) {
                        console.log(data);
                        if(callback_function !== undefined) {
                            callback_function(e);
                        }
                    },
                    dataType: "html",
                    beforeSend: function(xhr) {
                        xhr.withCredentials = true;
                    }
                });
        });
        }
    };
})();

