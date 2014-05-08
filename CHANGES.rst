
Changelog
=========

0.6dev
------

- Display link to manual download in product view description tab if present.
  [rnix]

- Also hide buyable controls overlay if mouse cursor enters empty placeholder
  column.
  [rnix]

- Consider view buyable information permission in product tiles.
  [rnix]

- Consider image field on folder if present in product tiles view.
  [rnix]

- Add ``bda.plone.productshop.behavior.IProductManualBehavior`` and apply it
  to product and variant content types.
  [rnix]

- Add ``bda.plone.shop.dx.IBuyablePeriodBehavior`` to product and variant
  content types.
  [rnix]

- Rename ``shopviews.css`` to ``productshop.css``. Re-applying GS profile
  required.
  [rnix]

- Fix product tiles view, overlay buyable controls are shown only if tile item
  represents buyable item directly.
  [rnix]


0.5
---

- Display buyable controls as overlay on mouse over on product tiles if
  displayed item in tile is buyable.
  [rnix]

- Add ``IProductShopSettings`` and ``IProductTilesViewSettingsBehavior``, both
  providing ``product_tiles_view_columns`` and
  ``product_tiles_view_image_scale`` properties, used in ``ProductTiles`` view.
  [rnix]


0.4
---

- Add product tiles view for plone site and folders.
  [rnix]

- Enable discount settings on productgroup.
  [rnix]

- Absolute imports.
  [rnix]

- Add ``IMaterialBehavior`` variant aspect.
  [rnix]

- Apply notification text behaviors to product shop types.
  [rnix]


0.3
---

- Product listing is now batched.
  [rnix]

- Add ``IAngleBehavior`` variant aspect.
  [rnix]

- Add ``IIPCodeBehavior`` variant aspect.
  [rnix]

- Handle query criteria as unicode to avoid ``UnicodeDecodeError``.
  [rnix]

- Add ``IShippingBehavior`` to product and variant types.
  [rnix]

- Add item number to ``IProduct``.
  [rnix]

- Add variant aspects ``ILengthBehavior``, ``IWidthBehavior`` and
  ``IHeightBehavior``.
  [rnix]


0.2
---

- Productgroup can define default variant aspects.
  [rnix]

- Add german translation.
  [rnix]

- Introduce ``IProductExcludeFromNavigation``.
  [rnix]

- Rename package to ``bda.plone.productshop``.
  [rnix]

- Add content types ``product``, ``productgroup``, ``variant``.
  [rnix]

- Reduce available views.
  [rnix]


0.1
---

- Initial work.
  [espenmn]
