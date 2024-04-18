$(document).ready(function () {
    $(document).on("submit", "form.ajax", function(e){
    e.preventDefault();
    var $this = $(this);

    var url = $this.attr("action");
    var method = $this.attr("method");

    jQuery.ajax({
        type: method,
        url: url,
        dataType: "json",
        data: new FormData(this),
        processData: false,
        contentType: false,
        cache: false,
        success:function (data) {
            var title = data["title"];
            var text = data["message"]
            var status = data["status"]
            Swal.fire({
              title: title,
              text: text,
              icon: status,
             });

            if(status == "success"){
                $this.trigger("reset")
            }
        },
        error:function (error) {
            console.log("error")
        },

    });
});
});

