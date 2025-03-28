============================
Purchase Delivery Split Date
============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:aafcab72b2ee01db23b4a65cb1f5810c33cb3ba6104d39e11e96c52b13c50982
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpurchase--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/purchase-workflow/tree/13.0/purchase_delivery_split_date
    :alt: OCA/purchase-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/purchase-workflow-13-0/purchase-workflow-13-0-purchase_delivery_split_date
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/purchase-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|


When this module is installed, each Purchase Order you confirm will
generate one Incoming Shipment for each schedule date indicated in the
Purchase Order Lines.

Once the Purchase Order has been confirmed, subsequent changes made to the
scheduled dates in the PO lines will produce a reorganization of the
corresponding stock moves in the Incoming Shipments, creating/deleting new
Incoming Shipments when needed, to ensure that each Incoming Shipment
contains moves to be received in the same date.

This module is also designed for extensibility, so that you can define
in other modules new criteria to split deliveries.

**Table of contents**

.. contents::
   :local:

Usage
=====


When a Purchase Order is confirmed, shipments will be grouped by same scheduled date.

Changelog
=========

12.0.2.0.0 (2020-04-10)
~~~~~~~~~~~~~~~~~~~~~~~

* Improve the module: when changing the date on a purchase line, this will
  cause a split or a merge of the pickings, to keep 1 picking per date.


11.0.1.0.0 (2018-09-16)
~~~~~~~~~~~~~~~~~~~~~~~

* Migration to 11.0.
  (`#461 <https://github.com/OCA/purchase-workflow/issues/461>`_)

* When the scheduled date is changed in the PO after confirmation the
  pickings are reorganized so as to force that every picking will have only
  moves to be delivered on the same date.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/purchase-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/purchase-workflow/issues/new?body=module:%20purchase_delivery_split_date%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Numerigraphe
* ForgeFlow
* Camptocamp

Contributors
~~~~~~~~~~~~


* Philippe Rossi <pr@numerigraphe.com> (initial patch against v6.0)
* Lionel Sausin <ls@numerigraphe.com> (modularization for v7+)
* Jordi Ballester Alomar <jordi.ballester@forgeflow.com> (modularization v8, v9)
* Lois Rilo <lois.rilo@forgeflow.com> (migration to v10)
* Alexandre Fayolle <alexandre.fayolle@camptocamp.com>
* Pimolnat Suntian <pimolnats@ecosoft.co.th>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/purchase-workflow <https://github.com/OCA/purchase-workflow/tree/13.0/purchase_delivery_split_date>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
