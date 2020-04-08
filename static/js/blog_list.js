$(function () {

    a_herf()

    $("input[name='category']").each(function () {
        $(this).change(function () {
            tag_selection($(this))
            $('#blog_list_form').submit();
        })
    });


    $("input[name='privacy']").change(function () {
        // privacy_cheange($(this));
        $('#blog_list_form').submit();
    });


    $("input[name='recommend']").change(function () {
        // recommend_cheange($(this));
        $('#blog_list_form').submit();
    });


    function a_herf() {
        $("a[name='page_range']").each(function () {
            var next_href = $(this).attr("href") + "&" + $('#blog_list_form').serialize();
            $(this).attr("href", next_href)
        })
    }


    function filter_params(){
            window.location.href = '?' + $('#blog_list_form').serialize();
        }


    // function privacy_cheange(obj) {
    //     if (obj.is(':checked')){
    //         $('#checkbox_recommend').prop('checked', false)
    //     }
    // }
    //
    //
    // function recommend_cheange(obj) {
    //     if (obj.is(':checked')){
    //         $('#privacy').prop('checked', false)
    //     }
    // }


    function tag_selection(obj) {
        var all_len = $("input[name='category']").length-1;
        if (obj.attr("id") == "checkbox_all"){
            obj.parent().siblings().children().prop("checked", obj.is(":checked"));
            $('#privacy').prop("checked", false);
            $('#checkbox_recommend').prop("checked", false);
        } else
            {
                $('#checkbox_all').prop("checked", false);
                var b_len = $("input[name='category']:checked").length;
                if (b_len >= all_len){
                    $('#checkbox_all').prop("checked", true)
                }
        }
    }

})
