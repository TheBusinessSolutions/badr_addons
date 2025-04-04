=======================
Purchase Order Approved
=======================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:5a02b270049081dab5afbaaadec26ed42b20d9007124af2c48bcf7a4c0124b6b
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpurchase--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/purchase-workflow/tree/13.0/purchase_order_approved
    :alt: OCA/purchase-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/purchase-workflow-13-0/purchase-workflow-13-0-purchase_order_approved
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/purchase-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends the functionality of purchases adding a new state
*Approved* in purchase orders before the *Purchase Order* state. Additionally
add the possibility to set back to draft a purchase order in all the states
previous to *Purchase Order*.

In this new *Approved* state:

* You cannot modify the purchase order.
* However, you can go back to draft and pass through the workflow again.
* The incoming shipments are not created. You can create them by clicking the
  *Convert to Purchase Order* button, also moving to state *Purchase Order*.

The new state diagram is depicted below:

.. image:: https://raw.githubusercontent.com/OCA/purchase-workflow/12.0/purchase_order_approved/static/description/schema.png
   :width: 500 px
   :alt: New states diagram

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module:

#. Go to 'Purchase > Configuration > Settings'.
#. In the *Orders* section you can set the *State 'Approved' in Purchase
   Orders*.

Usage
=====

To use this module, you need to:

#. Go to a Request for Quotation.
#. Click *Confirm Order*. The state is now *Approved* (if no order approval
   is not set).
#. To move forward to the state *Purchase Order* and release the creation
   of the deliveries, click on *Convert to Purchase Order*.

Changelog
=========

11.0.1.0.0 (2018-06-06)
~~~~~~~~~~~~~~~~~~~~~~~

* [MIG] Migrated to v11.

12.0.1.0.0 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [MIG] Migrated to v12.


12.0.1.0.0 (2020-07-16)
~~~~~~~~~~~~~~~~~~~~~~~

* [MIG] Migrated to v13.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/purchase-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/purchase-workflow/issues/new?body=module:%20purchase_order_approved%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ForgeFlow

Contributors
~~~~~~~~~~~~

* Lois Rilo <lois.rilo@forgeflow.com>
* Rattapong Chokmasermkul <rattapongc@ecosoft.co.th>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/purchase-workflow <https://github.com/OCA/purchase-workflow/tree/13.0/purchase_order_approved>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
