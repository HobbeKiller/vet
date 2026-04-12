from odoo import fields, models, api
class Pet(models.Model):
    _inherit = "res.partner"

    pet = fields.One2many("animal", "owner", string="Pet")
