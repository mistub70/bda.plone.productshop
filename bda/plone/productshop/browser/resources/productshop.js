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
            variant: function(container, params) {
                bdajax.request({
                    url: '@@variant_uid_by_criteria',
                    type: 'json',
                    params: params,
                    success: function(data, status, request) {
                        if (!data.found) {
                            $('.invalid_aspects', container).show();
                            return;
                        }
                        bdajax.action({
                            url: data.url,
                            params: {},
                            name: 'bda.plone.productshop.variant',
                            mode: 'replace',
                            selector: '.variant_view'
                        });
                    }
                });
            },

            // productgroup scope callback
            productgroup: function(container, params) {
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
                var params = { uid: container.data('uid') };
                $('select', container).each(function() {
                    var selection = $(this);
                    params[selection.attr('name')] = selection.val();
                });
                productshop.scopes[container.data('scope')](container, params);
            });
        }
    };

})(jQuery);
