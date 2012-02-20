
var softgis = {};
softgis.proto = (function() {
    return {
        "pageload_callback": function(data) {
          $(".content").html(data);
          softgis.proto.pageload();  
        },
        "init": function(callback_function) {
            $.ajax({
                    url: "/form/",
                    type: "GET",
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
                    dataType: "html"
                });
        },
        "pageload": function () {
            $(".submit").click(function(){
                $.ajax({
                    url: "/form/",
                    type: "POST",
                    data: $('form[name=questform]').serializeArray(),
                    //contentType: "application/json",
                    success: function(data) {
                        //console.log(data);
                        softgis.proto.pageload_callback(data);
//                        if(callback_function !== undefined) {
//                            callback_function(data);
//                            }
                        },
                    error: function(e) {
                        console.log(e);
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
            $(".first_step").click(function(){
                var formData = $('form[name=questform]').serializeArray();
                formData.push({"name": "wizard_goto_step", "value": $(".first_step").val()});
                $.ajax({
                    url: "/form/",
                    type: "POST",
                    data: formData,
                    contentType: "application/json",
                    success: function(data) {
                        softgis.proto.pageload_callback(data);
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
            $(".prev_step").click(function(){
                var formData = $('form[name=questform]').serializeArray();
                formData.push({"name": "wizard_goto_step", "value": $(".prev_step").val()});
                $.ajax({
                    url: "/form/",
                    type: "POST",
                    data: formData,
                    contentType: "application/json",
                    success: function(data) {
                        softgis.proto.pageload_callback(data);
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

