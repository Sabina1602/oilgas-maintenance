from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError

class Maintenance_request(models.Model):

    _name = 'oilgas.maintenance.request'
    _description = 'maintenance request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Maintenance Request Title', required=True, tracking=True)

    equipment_id = fields.Many2one('oilgas.equipment', string='Equipment ID', required=True, tracking=True)

    technician_id = fields.Many2one('res.partner', string='Technician ID', required=True, tracking=True,
                                    domain = [('is_technician', '=', True)])

    description = fields.Text(string='Description', required=True, tracking=True)

    priority = fields.Selection ([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ],
        string='Priority', tracking=True
    )

    request_date = fields.Date(string = "Request Date", default = fields.Date.today, tracking=True)

    completion_date = fields.Date(string = "Completion Date", tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ],
        string='Status',
        default='draft',
        tracking=True)

    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise UserError("Only draft records can be confirmed.")
            else:
                record.state = 'confirmed'

    def action_start(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError("Only confirmed requests can be started.")
            else:
                record.state = 'in_progress'

    def action_done(self):
        for record in self:
            if record.state != 'in_progress':
                raise UserError("Only in-progress requests can be marked done.")
            record.state = 'done'


    def action_cancel(self):
        for record in self:
            if record.state in ('done', 'cancelled'):
                raise UserError("You cannot cancel completed or already cancelled requests")
            else:
                record.state = 'cancelled'

    def action_done_date(self):
        for record in self:
            if record.state != 'in_progress':
                raise UserError("Only in-progress requests can be marked done.")
            record.completion_date = fields.Date.today()
            record.state = 'done'