(function($) {

    $(document).ready(function() {
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                productshop_binder: productshop.binder
            });
        }
        productshop.binder(document);
    });

    productshop = {

        // scope callbacks
        scopes: {

            // variant scope callback
            variant: function(params) {
                bdajax.request({
                    url: '@@variant_uid_by_criteria',
                    type: 'json',
                    params: params,
                    success: function(data, status, request) {
                        if (!data.found) {
                            var msg = 'No Product found with defined criteria';
                            bdajax.info(msg);
                            return;
                        }
                        alert(data.url);
                    }
                });
            },

            // productgroup scope callback
            productgroup: function(params) {
                alert('handle productgroup');
            }
        },

        // productshop binder function
        binder: function(context) {
            // bind shopview tabs
            $('ul.shopview_tabs').tabs('div.shopview_panes > div');

            // aspect filter
            $('div.variant_aspects select').bind('change', function(event) {
                var container = $(this).parents('div.variant_aspects');
                var cid = container.attr('id');
                var params = { uid: cid.substring(16, cid.length) };
                $('select', container).each(function() {
                    var selection = $(this);
                    params[selection.attr('name')] = selection.val();
                });
                productshop.scopes[container.data('scope')](params);
            });
        }
    };

})(jQuery);
