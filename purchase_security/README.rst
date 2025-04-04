=======================
Purchase Order security
=======================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:a46dffe2eedc249451d0681a4c74f146630230628c99a2f645e8769e4e0f13e9
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpurchase--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/purchase-workflow/tree/13.0/purchase_security
    :alt: OCA/purchase-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/purchase-workflow-13-0/purchase-workflow-13-0-purchase_security
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/purchase-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This addon creates a new group called "Purchase (own orders)" in Purchase.

For users in this group, the only Purchase Orders they can see are those where
they are the representative, or all of them if they are managers.

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

#. Go to **Purchase > Orders > Purchase Orders**
#. Create a Purchase Order and assing a **Purchase Representative**
   (in the **Other Information** tab), if you are a Purchase User or Manager.
   If you are a Purchass User (own orders), i'll be automatically assigned,
   and you won't be able to change it
#. Confirm the Purchase Order
#. Go back to the **Purchase Orders** view.
#. If you are a Purchase User or a Purchase Manager, you should be
   able to see all orders. If not, you'll only see your own orders.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/purchase-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/purchase-workflow/issues/new?body=module:%20purchase_security%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_:

  * João Marques
  * Stefan Ungureanu
  * Pedro M. Baeza
* `Solvos <https://www.solvos.es>`_:

  * David Alonso <david.alonso@solvos.es>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-joao-p-marques| image:: https://github.com/joao-p-marques.png?size=40px
    :target: https://github.com/joao-p-marques
    :alt: joao-p-marques

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-joao-p-marques| 

This module is part of the `OCA/purchase-workflow <https://github.com/OCA/purchase-workflow/tree/13.0/purchase_security>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
