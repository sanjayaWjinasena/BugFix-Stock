# BugFix-Stock — Permanently Deferred Items

Items intentionally not ported this arc (v0.0.15 → v0.0.25).
Each block: **what**, **why**, **restore path** if we come back.

---

## 1. View 4732 — `stock.picking.form_button` (Studio inherit, priority 999905, 6.8 KB)

**Blocker:** Odoo minor-version drift between Clear-DB and repair-test-101
on the standard `stock.view_picking_form`. Three fields referenced in
attribute-modifier expressions do NOT exist on repair-test-101's
`stock.picking` model:

- `show_mark_as_todo`
- `show_validate`
- `immediate_transfer`

Plus one xpath anchor missing button `action_set_quantities_to_reservation`.

**What it would add:** Request Transfer Approval / Approve Transfer /
Reject Transfer + Update Offset Account + Validate Reject Reason buttons
on the `stock.picking` form header.

**Restore path:** Requires stripping 4 xpath blocks (1 button-name anchor
+ 3 attribute-modifier xpaths that reference the missing fields). At that
point the arch is ~30% smaller than byte-verbatim and mostly just
button-add lines with default visibility conditions. If a future Odoo
version restores the missing fields, revert the strips.

**Files affected:** none (never landed).
**Attempted:** v0.0.23 (reverted, `899f181`).

---

## 2. Act_window 1383 "TP Invoices" + associated button in view 2816

**Blocker:** action's `res_model = x_tp_invoice_header`. That model is
owned by BugFix-Accounting, not a manifest dep of BugFix-Stock. At
BugFix-Stock's data-load time the model isn't in the registry yet
(Odoo topological order places BugFix-Stock before BugFix-Accounting;
they don't depend on each other).

**What it would add:** "TP Invoices" stat button on `x_consignment_header`
form (pointing at TP Invoice records linked via `x_studio_con_no=active_id`).

**Restore paths (two options):**

A. Add `BugFix-Accounting` to `BugFix-Stock`'s manifest depends. Pulls
   in the whole BugFix-Accounting dep tree (account_budget, account_reports,
   BugFix-Sales, BugFix-Purchase, bank-data, seed_master_data_and_settings,
   studio_usermodel_migration, BugFix-Project, Jinasena_Masterdata_Reporting).
   Then re-add act_window 1383 + un-strip the TP Invoices button from
   view 2816.

B. Move act_window 1383 to BugFix-Accounting (where `x_tp_invoice_header`
   lives). Update view 2816's button ref to
   `%(BugFix-Accounting.act_1383_tp_invoices)d`. Still creates a
   `BugFix-Stock → BugFix-Accounting` dep edge (same as option A).

**Files affected currently:**
- `data/act_windows.xml` — 1383 not present (skipped in v0.0.24).
- `views/stock_studio_ported_v5.xml` — view 2816 arch has the TP
  Invoices button surgically removed via lxml etree (see the code
  comment in the file).

**Attempted:** first v0.0.24 attempt shipped 1383 alongside 1306+1322
and crashed. Reverted (`929f449`). Second v0.0.24 attempt shipped only
1306+1322 successfully (`fdabbf9`).

---

## Ancillary skips that are NOT permanent

These are documented in VIEWS_TODO.md's history but landed elsewhere
this arc — kept here as a reminder in case someone reads DEFERRED.md
first:

- **View 2585** (stock.valuation.layer tree) — landed v0.0.19 after
  porting 2 related-field O2Ms (`x_studio_related_field_bPlxa`, `_ygmmJ`).
- **View 4619** (stock.return.picking form) — landed v0.0.20 alongside
  server action 1997 port.
- **Views 2811 + 2816** — landed v0.0.25 after porting
  `x_studio_consignment_line_ids` field (was TODO on-disk) and
  injecting 5 sentinel fields for Odoo 17 strict modifier validation.
- **Views 2810 / 2813 / 2814 / 2817 / 2818 / 2819** — landed v0.0.16
  (x_consignment_* primary + Studio inherits).
