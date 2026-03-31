from odoo import models, fields

class ResPartner(models.Model):

    _inherit = 'res.partner'

    is_technician = fields.Boolean (
        string = 'Technician',
        default = False
    )

    employee_id = fields.Char(
        string = 'Employee ID',
    )

    specialization = fields.Selection([
        ('mechanical', 'Mechanical'),
        ('electrical', 'Electrical'),
        ('instrumentation', 'Instrumentation'),
    ],
        string = 'Specialization',
    )