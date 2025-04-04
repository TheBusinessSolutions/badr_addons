=================================================
Stock Picking Restrict Cancel with Original Moves
=================================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:86c378c589459b51f0a70b7032e7fef7fb7c9aa623ffc6b5a671ce98e15f6b81
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fstock--logistics--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/stock-logistics-workflow/tree/13.0/stock_picking_restrict_cancel_with_orig_move
    :alt: OCA/stock-logistics-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/stock-logistics-workflow-13-0/stock-logistics-workflow-13-0-stock_picking_restrict_cancel_with_orig_move
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-workflow&target_branch=13.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module restricts the cancellation of stock picking, if any move is linked
to a previous move, which is not canceled or done yet.

**Table of contents**

.. contents::
   :local:

Usage
=====

Odoo allows to cancel any picking in a chain of moves between locations, and
will automatically cancel the ensuing moves but leaves the previous ones in
their actual state.

This module restricts this possibility and displays an error to the user,
listing all the stock pickings containing stock moves linked to the picking the
user is trying to cancel, so he can delete the original, ensuring all the
following pickings will be canceled as well.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/stock-logistics-workflow/issues/new?body=module:%20stock_picking_restrict_cancel_with_orig_move%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Camptocamp

Contributors
~~~~~~~~~~~~

* Vincent Renaville <vincent.renaville@camptocamp.com>
* Akim Juillerat <akim.juillerat@camptocamp.com>
* Kitti Upariphutthiphong <kittiu@ecosoft.co.th>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/stock-logistics-workflow <https://github.com/OCA/stock-logistics-workflow/tree/13.0/stock_picking_restrict_cancel_with_orig_move>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
