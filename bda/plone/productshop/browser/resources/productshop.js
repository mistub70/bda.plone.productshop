(function($) {

    $(document).ready(function() {
        var binder = function(context) {
            // bind shopview tabs
            $('ul.shopview_tabs').tabs('div.shopview_panes > div');

            // aspect filter
            $('div.variant_aspects select').bind('change', function(event) {
                var container = $(this).parents('div.variant_aspects');
                var params = {};
                $('select', container).each(function() {
                    var selection = $(this);
                    params[selection.attr('name')] = selection.val();
                });
                bdajax.request({
                    url: '@@variant_uid_by_criteria',
                    type: 'json',
                    params: params,
                    success: function(data, status, request) {
                        alert(data);
                    }
                });
            });
        }
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                productshop_binder: binder
            });
        }
        binder(document);
    });

})(jQuery);
