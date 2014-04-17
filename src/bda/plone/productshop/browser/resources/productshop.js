(function($) {

    $(document).ready(function() {
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                productshop_binder: productshop.binder
            });
        }
        productshop.binder(document);
        $(window).bind('resize', function(evt) {
            productshop.rezize_tiles();
        });
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
                var selector = '.product_listing_' + params.uid;
                var listing = $(selector);
                var url = listing.attr('ajax:target');
                var target = {
                    url: url,
                    params: params
                };
                bdajax.trigger('render_product_listing', selector, target);
            }
        },

        rezize_tiles: function() {
            var tiles = $('div.product_tile');
            tiles.css({'height': tiles.width() + 'px'});
        },

        show_overlay_buyable_controls: function(tile) {
            var buyable_url = tile.data('buyable_url');
            if (!buyable_url) {
                return;
            }
            var tiles = tile.parents('.product_tiles');
            var overlay = $('.overlay_buyable_controls', tiles);
            if (overlay.data('buyable_url') == buyable_url) {
                return;
            }
            var overlay_width = 150;
            var overlay_height = 200;
            overlay.css('min-width', overlay_width + 'px');
            overlay.css('min-height', overlay_height + 'px');
            var tile_position = tile.position();
            var tile_top = tile_position.top;
            overlay.css('top', (tile_top + 50) + 'px');
            var tiles_width = tiles.width();
            var tile_width = tile.width();
            var tile_left = tile_position.left;
            if (tile_left + overlay_width < tiles_width) {
                overlay.css('left', (tile_left + 20) + 'px');
            } else {
                overlay.css('left', (tiles_width - overlay_width - 20) + 'px');
            }
            overlay.empty();
            bdajax.request({
                success: function(data) {
                    overlay.data('buyable_url', buyable_url);
                    overlay.html(data);
                    overlay.bdajax();
                    overlay.show();
                },
                url: buyable_url + '/@@buyable_controls'
            });
        },

        hide_overlay_buyable_controls: function() {
            var overlay = $('.overlay_buyable_controls');
            overlay.data('buyable_url', null);
            overlay.hide();
        },

        // productshop binder function
        binder: function(context) {
            // tile resize
            productshop.rezize_tiles();

            // tile overlay buyable controls
            $('.product_tile', context).unbind()
                                       .bind('mouseenter', function(event) {
                productshop.show_overlay_buyable_controls($(this));
            })
            $('.product_tiles', context).unbind()
                                        .bind('mouseleave', function(event) {
                productshop.hide_overlay_buyable_controls();
            });

            // bind shopview tabs
            $('ul.shopview_tabs').tabs('div.shopview_panes > div');

            // aspect filter
            $('div.variant_aspects select').unbind()
                                           .bind('change', function(event) {
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
