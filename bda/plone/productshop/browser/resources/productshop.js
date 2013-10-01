(function($) {

    $(document).ready(function() {
        var binder = function(context) {
            // bind shopview tabs
            $('ul.shopview_tabs').tabs('div.shopview_panes > div');

            // replace variant listing
            var replace_productgroup_listing = function(obj_uid, data) {
                if (data.found) {
                    alert(data.url);
                } else {
                }
            }

            // replace variant view
            var replace_variant_view = function(obj_uid, data) {
                if (data.found) {
                    alert(data.url);
                } else {
                }
            }

            // aspect filter
            $('div.variant_aspects select').bind('change', function(event) {
                var container = $(this).parents('div.variant_aspects');
                var cid = container.attr('id');
                var uid = cid.substring(16, cid.length);
                var params = {};
                params.variant_aspects_uid = uid;
                $('select', container).each(function() {
                    var selection = $(this);
                    params[selection.attr('name')] = selection.val();
                });
                bdajax.request({
                    url: '@@variant_uid_by_criteria',
                    type: 'json',
                    params: params,
                    success: function(data, status, request) {
                        if (data.scope == 'productgroup') {
                            replace_productgroup_listing(uid, data);
                        }
                        if (data.scope == 'variant') {
                            replace_variant_view(uid, data);
                        }
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
