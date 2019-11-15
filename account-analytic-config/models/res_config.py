# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_analytic_distribution_required = fields.Boolean(string='account analytic distribution required',
        help=' This module extends account_analytic_required and adds 2 policies to \n' 
              ' control the use of analytic distributions. The policies behave as follow \n' 

              ' * never: no analytic account nor analytic distribution allowed \n' 
              ' * always: analytic account required \n' 
              ' * always_plan: analytic_distribution required \n' 
              ' * always_plan_or_account: analytic distribution or analytic account required \n' 
              ' * optional: do what you like, \n' 

              ' In any case analytic account and analytic distribution are mutually exclusive. \n'
             '-This installs the module account_analytic_distribution_required.')
    
    module_account_analytic_parent = fields.Boolean(string='account analytic parent',
        help=' This module reintroduces the hierarchy to the analytic accounts as \n' 
              ' it was in previous versions of Odoo. This module is a base module for \n' 
              ' other modules to manage the hierarchy concept in analytics. \n' )

    module_account_analytic_required = fields.Boolean(string='account analytic required',
        help='This module adds an option *analytic policy* on account types. \n'
            'You have the choice between 4 policies : *always*, *never*, *posted moves* and *optional*. \n')

    module_account_analytic_sequence = fields.Boolean(string='account analytic sequence',
        help='This module restores the sequence for an analytic account\n'
             '-This installs the module account_analytic_sequence.')


    module_analytic_base_department = fields.Boolean(string='analytic_base_department',
        help='This module add Department to Analytic Account lines. \n'
              'It will set current user by default on the lines. \n'
             '-This installs the module analytic_base_department . \n')

    module_analytic_partner = fields.Boolean(string='analytic partner',
        help= 'This module adds a commercial partner on each analytic item for allowing to \n'
              'have another dimension for data analysis. \n'

              'It also handles the proper propagation of this field to the created analytic \n'
              'entries when validating invoices. \n'
              '-This installs the module analytic_partner .')

    module_analytic_partner_hr_timesheet = fields.Boolean(string='analytic partner hr timesheet',
        help='This module adds another partner on HR timesheets and propagate it to the \n'
              'auto-generated analytic entries on the "Other partner" field. \n'
             '-This installs the module analytic_partner_hr_timesheet .')

    module_analytic_tag_dimension = fields.Boolean(string='analytic tag dimension',
        help=' This module allows to group Analytic Tags on Dimensions. \n' 
            ' Dimensions are created as custom field, then you can group by Dimensions on: \n' 
            ' * Account/Adviser/Journal Items \n' 
            ' * Account/Reports/Business Intelligence/Analytic Entries \n' 
            ' When you set Tags on Analytic Entries, each custom field for dimensions is updated with its Tag. \n' 
            ' One Tag is only allowed on one Dimension, and you can not set more than one Tag from same Dimensions on Analytic Entry. \n'  
             '-This installs the module analytic_tag_dimension .')

    module_mrp_analytic = fields.Boolean(string='mrp analytic',
        help='This module links the manufacturing area with analytic management. \n'
              'For now, it adds analytic account configuration for manufacturing orders, \n'
              'and their corresponding shortcuts. Other modules can take advantage of \n'
              'this link for other usages. \n'
             '-This installs the module mrp_analytic .')

    module_procurement_mto_analytic = fields.Boolean(string='Procurement Mto Analytic',
        help='This module takes account analytic value from sale order to the created \n'
              'purchase order line. \n'
             '-This installs the module procurement_mto_analytic .')

    module_product_analytic = fields.Boolean(string='Product Analytic',
        help='This module allows to define an analytic account at product or category level \n'
              'for using it when creating invoices. \n'

              'This module is an alternative to the official module \n'
              '*account_analytic_default*. The advantages of this module are: \n'

              '* it only depends on the *account* module, whereas the \n'
               ' *account_analytic_default* module depends on *sale_stock* ; \n'

              '* the analytic account is configured on the product form or the product \n'
               ' category form, and not on a separate object. \n'
             '-This installs the module product_analytic .')


    module_purchase_analytic = fields.Boolean(string='Purchase Analytic',
        help='The goal of this module is to ease analytic account management on purchase order. \n'
              'This module add analytic account on purchase order. \n'
              'If all lines of the purchase order have the same analytic account, the analytic account on the purchase order \n'
              'is automatically set with this value.\n'
              'If a analytic account is set on the purchase order, all lines of the purchase will take this value. \n'
             '-This installs the module purchase_analytic .')

    module_purchase_request_analytic = fields.Boolean(string='Purchase Request Analytic',
        help='TThis module adds the analytic account field to Purchase Requests. \n'
             '-This installs the module purchase_request_analytic .')

    module_stock_analytic = fields.Boolean(string='Stock Analytic',
        help='Adds an analytic account in stock move to be able to get analytic information \n'
              'when generating the journal items. \n'
             '-This installs the module stock_analytic .')

    module_stock_inventory_analytic = fields.Boolean(string='Stock Inventory Analytic',
        help='This module allow to add analytic accounts on stock inventory line whether \n'
              'using Inventory Adjustments or updating quantity on hand product wizard. \n'
              '-This installs the module stock_inventory_analytic .')

   