from odoo import fields, models

class GudangInfo(models.Model):
    _name = "gudang.info"

    name = fields.Char(string="Gudang Name", help="Detail dari nama gudang")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    nomer_gudang = fields.Integer(string="No Gudang")
    provinsi = fields.Selection([('bali','Provinsi Bali'),
                                 ('jawa','Provinsi Jawa'),
                                 ('maluku','Provinsi Maluku'),
                                 ('sumatra','Provinsi Sumatra')],
                                string="Provinsi Gudang")

    is_sharing_gudang = fields.Boolean(String="Support sharing Gudang?")
