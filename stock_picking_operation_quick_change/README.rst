====================================
Stock Picking Operation Quick Change
====================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:e90e0ee14fcfcc8a1ebf30a6106266552bafda67e54309e28db0458c2d939015
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fstock--logistics--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/stock-logistics-workflow/tree/13.0/stock_picking_operation_quick_change
    :alt: OCA/stock-logistics-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/stock-logistics-workflow-13-0/stock-logistics-workflow-13-0-stock_picking_operation_quick_change
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends standard WMS to allow change destination location for all
picking operations.

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

#. Go to products and create one of type "Stockable".
#. Update quantities on hand to have stock of it.
#. Go to inventory dashboard and click on "Delivery Orders" card to create a new
   transfer.
#. Create a picking and select the product to do the transfer and save it.
#. Click on button *Change Location*, select in wizard the old location or product and
   new location.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/stock-logistics-workflow/issues/new?body=module:%20stock_picking_operation_quick_change%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_:

  * Sergio Teruel
  * Carlos Roca

* Lois Rilo <lois.rilo@forgeflow.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/stock-logistics-workflow <https://github.com/OCA/stock-logistics-workflow/tree/13.0/stock_picking_operation_quick_change>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
