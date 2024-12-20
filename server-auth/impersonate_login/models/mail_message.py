# Copyright (C) 2024 Akretion (<http://www.akretion.com>).
# @author Kévin Roche <kevin.roche@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.http import request
from odoo.tools import html_escape


class Message(models.Model):
    _inherit = "mail.message"

    impersonated_author_id = fields.Many2one(
        comodel_name="res.partner",
        compute="_compute_impersonated_author_id",
        store=True,
    )

    body = fields.Html(
        compute="_compute_message_body",
        inverse="_inverse_message_body",
        store=True,
        readonly=False,
    )

    @api.depends("author_id")
    def _compute_impersonated_author_id(self):
        for rec in self:
            if request and request.session.impersonate_from_uid:
                rec.impersonated_author_id = (
                    self.env["res.users"]
                    .browse(request.session.impersonate_from_uid)
                    .partner_id.id
                )
            else:
                rec.impersonated_author_id = False

    @api.depends("author_id", "impersonated_author_id")
    def _compute_message_body(self):
        for rec in self:
            additional_info = ""
            if (
                request
                and request.session.impersonate_from_uid
                and rec.impersonated_author_id
            ):
                current_partner = (
                    self.env["res.users"].browse(request.session.uid).partner_id
                )
                additional_info = _("Logged in as {}").format(
                    html_escape(current_partner.name)
                )
            if rec.body and additional_info:
                rec.body = f"<b>{additional_info}</b><br/>{rec.body}"
            else:
                rec.body = rec.body

    def _inverse_message_body(self):
        for rec in self:
            additional_info = ""
            if (
                request
                and request.session.impersonate_from_uid
                and rec.impersonated_author_id
            ):
                current_partner = (
                    self.env["res.users"].browse(request.session.uid).partner_id
                )
                additional_info = _("Logged in as {}").format(
                    html_escape(current_partner.name)
                )
            if additional_info:
                start_with = f"<b>{additional_info}</b><br/>"
                if rec.body and rec.body.startswith(start_with):
                    rec.body = rec.body
                else:
                    rec.body = f"{start_with}{rec.body}"
            else:
                rec.body = rec.body
