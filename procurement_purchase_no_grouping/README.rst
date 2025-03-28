================================
Procurement Purchase No Grouping
================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:54f5a2d877d23c94936e5270fa2e2868928c63ae89cbaf0a1ba6f4b2e4d3090a
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpurchase--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/purchase-workflow/tree/13.0/procurement_purchase_no_grouping
    :alt: OCA/purchase-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/purchase-workflow-13-0/purchase-workflow-13-0-procurement_purchase_no_grouping
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/purchase-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows to not group generated purchase orders from procurements.
The grouping behaviour can be configurable at product category level or fall back
to system default.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Go to each product category, and select one of these values in the field
"Procured purchase grouping":

* *Standard grouping*: With this option, procurements will generate
  purchase orders as always, grouping lines and orders when possible.
* *No line grouping*: With this value, if there are any open purchase order
  for the same supplier, it will be reused, but lines won't be merged.
* *No order grouping*: This option will prevent any kind of grouping.
* *<empty>*: If you select nothing, default value set up in System
  settings will be applied.
* *Product category grouping*: This option groups products in the same purchase order that belongs to the same product category.

System default behaviour can be set up in System settings / Purchase / Procurement
Purchase Grouping

Known issues / Roadmap
======================

- If you reuse the same procurement group between several sales orders, and
  using "No line grouping", they will be grouped anyways, as the criteria for
  grouping or not should be kept to the same procurement group, as it's the only
  way to get proper quantities updates after confirming the sales order.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/purchase-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/purchase-workflow/issues/new?body=module:%20procurement_purchase_no_grouping%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* AvanzOSC
* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_:

  * Pedro M. Baeza
  * Sergio Teruel
  * Carlos Dauden
  * Alexandre Díaz
  * Víctor Martínez

* Ana Juaristi <ajuaristo@gmail.com>
* Alfredo de la Fuente <alfredodelafuente@avanzosc.es>
* Radovan Skolnik <radovan@skolnik.info>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/purchase-workflow <https://github.com/OCA/purchase-workflow/tree/13.0/procurement_purchase_no_grouping>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
