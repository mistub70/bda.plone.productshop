===================
bda.plone.shopviews
===================

Views for ``bda.plone.shop``


Views
=====

- @@products_view
- @@productlist_view
- @@productlisting_view
- @@quicksand_view
- @@productboxes_view
- @@colorboxes_view
- @@product_view
- @@variations_view


Checking it out
===============

To test out the views you might want to install
bda.shoptypes, which contains 3 content types for bda.plone.shop:

1) Product ((bda.shoptypes.product) which contains two images and two rich text
   fields. The rich text fields will have their own tabs at the bottom
2) Productgroup (bda.shoptypes.productgroup)
3) Variation (bda.shoptypes.variation) that can be added inside a Productgroup
   folder. You should set the view of Productgroup to one of the Variation
   (in other words: the view of "Productgroup folder" should be one content
   item (the default Variation)

NB: None of the FOLDER views are enabled by default, but you can test them by
adding /@@viewname to the url, like:

- http://mysite.com/product/@@product_view
- http://mysite.com/folder/productlist_view

Or just go to /portal_types and add those views you want to use.


Variation view
==============

The variation view is for use with a Productgroup.

Let's say you have a productgroup "T-shirt", and the following
Variations: "Green", "Yellow", "Blue".

First, you add "Productgroup" (a folderish content type) "Cool T-shirt" and
inside that you add Variations "Blue", "Yellow" and "Green". 

Then you set the "Green" as default view for "Cool T-Shirt" and set to view
on "Blue", "Yellow" and "Green" to "variations_view" (you probably want to
do this in ZMI at /portal_types. You SHOULD hide the "Buy viewlet" by CSS
or by /@@manage-viewlets

The result will be something like this:
http://www.bmh.no/nettbutikk/platespillere/rega-rp1

Currently, the cart is only working with UIDs that are present before the
javascript loads. Because of that, all the Variations is loaded, which might
be a bit slow.

(Suggestions on how to overcome this problem is welcome).

**The views are intended as a starting point for your own views, 
but they can also be customized TTW or used as they are.**


Productview
===========

- The producview is intended as a view for a "Product. The look is something
  like how the items here are presented (click on them):
  http://www.bmh.no/nettbutikk/tilbehor


The folder (listing) views
==========================

- @@products_view
- @@productlist_view
- @@productlisting_view
- @@productboxes_view

All these views are quite similar, for example

- http://www.bmh.no/nettbutikk/forsterkere
- http://www.bokstavogbilde.no/bokhandel
- http://www.bokstavogbilde.no/bokhandel/boker/productlisting_view


The "javascript" views
======================

- @@quicksand_view
- @@productboxes_view
- @@colorboxes_view

The two first views are just used for folders that contain "Products", and
they will sort on Keywords/Tags. Colorboxes will sort on "Colors"


TODO
====

- Fix CSS classes so they never contain illegal charaters.
- make the quicksand view sortable on price, colors etc.
- make the quicksand view work with the cart (the quicksandview is not playing
  well with the add to cart when new content is added to the DOM. )


Installation
============

Add ``bda.plone.shopviews`` to the eggs (in buildout.cfg) and install it as
addon in plone control panel.


Contributors
============

- Espen Moe-Nilssen (Autor)
- Robert Niederreiter


Dummy product image from
========================

- http://thelittlereaper.deviantart.com/art/Test-Crash-Dummy-169618976
