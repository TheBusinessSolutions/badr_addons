========================================
Purchase Requisition Order Remaining Qty
========================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:8d555a38778d14a525717f580d24790b2bd3b92f4b3ee7f1bd75b8732b3c615c
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpurchase--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/purchase-workflow/tree/13.0/purchase_requisition_order_remaining_qty
    :alt: OCA/purchase-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/purchase-workflow-13-0/purchase-workflow-13-0-purchase_requisition_order_remaining_qty
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/purchase-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows you to define agreement types to use the remaining quantity of the
agreement compared with the already proposed RfQs quantity.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

#. Go to **Purchase > Configuration > Purchase Agreement Types**
#. Create or update some record and set "Quantities" to "Use remaining quantities of agreement".

Usage
=====

To use this module, you need to:

#. Go to **Purchase > Order > Purchase Agreements**
#. Create an agreement and set "Remaining Qty" type and create a line with any product and set quantity to 5.
#. Go to "New quotation" button.
#. The RFQ created will have the quantity defined in the line at 5.
#. Update Quantity to 3 according to RFQ line.
#. Go to "New quotation" button.
#. The RFQ created will have the quantity defined in the line at 2.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/purchase-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/purchase-workflow/issues/new?body=module:%20purchase_requisition_order_remaining_qty%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_:

  * Víctor Martínez
  * Pedro M. Baeza

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-victoralmau| image:: https://github.com/victoralmau.png?size=40px
    :target: https://github.com/victoralmau
    :alt: victoralmau

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-victoralmau| 

This module is part of the `OCA/purchase-workflow <https://github.com/OCA/purchase-workflow/tree/13.0/purchase_requisition_order_remaining_qty>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
