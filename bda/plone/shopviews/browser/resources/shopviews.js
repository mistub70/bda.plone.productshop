(function($) {

    $(document).ready(function() {
        // bind shopview tabs
        $("ul.shopview_tabs").tabs("div.shopview_panes > div");

        $('div.variations > .False').hide();

        var selected = '.' + $('#fronted').val() + ' input';

        $('#fronted').hide();

        $($(selected)).click();

        $("#filter input").click(function() {
            var $value = 'div.variations div.' + $(this).val();
            $('div.variations > div').hide();
            $($value).show();
        });
    });

})(jQuery);
