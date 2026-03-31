from odoo import models, fields, api

class Equipment(models.Model):

    _name= 'oilgas.equipment'
    _description = 'equipment'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True, required=True)

    serial_number = fields.Char(string='Serial Number',
                                tracking=True)

    location = fields.Char(string='Location', tracking=True)

    equipment_type = fields.Selection([
        ('pump', 'Pump'),
        ('compressor', 'Compressor'),
        ('valve','Valve'),
        ('generator','Generator')
    ],
        string='Equipment Type',
        tracking=True)

    status = fields.Selection([
        ('operational', 'Operational'),
        ('faulty','Faulty'),
        ('under_maintenance','Under maintenance'),
        ('decommissioned','Decommissioned')
    ],
        string='Status',
        default='operational',
        tracking=True)

    technician_id = fields.Many2one ('res.partner', string='Technician ID', tracking=True,
                                     domain = [('is_technician', '=', True)]
    )

    maintenance_request_ids = fields.One2many(
        'oilgas.maintenance.request',
        'equipment_id',
        string='Maintenance Requests',
    )
