from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class LegalDocumentForm(FlaskForm):
    agreement_type = SelectField('Select Agreement Type', choices=[
        ('partnership', 'Partnership Agreement: "The partners agree to share profits and losses equally."'),
        ('lease', 'Lease Agreement: "The landlord and the tenant agree on the rental rate and the duration of the lease."'),
        ('employment', 'Employment Agreement: "The employer and the employee agree on the terms of employment, including salary, benefits, and duties."'),
        ('nda', 'Non-Disclosure Agreement (NDA): "The parties agree to keep the shared information confidential."'),
        ('licensing', 'Licensing Agreement: "The licensor agrees to grant the licensee the right to use its intellectual property."'),
        ('service', 'Service Agreement: "The service provider and the client agree on the scope and price of the services."'),
        ('settlement', 'Settlement Agreement: "The parties agree to settle the dispute and release each other from any further claims."'),
        ('purchase', 'Purchase Agreement: "The buyer and the seller agree on the terms of the sale, including the price and the delivery date."')
    ], validators=[DataRequired()])
    
    party_1 = StringField('Party 1', validators=[DataRequired()])
    party_2 = StringField('Party 2', validators=[DataRequired()])
    specific_terms = StringField('Specific Terms', validators=[DataRequired()])
    submit = SubmitField('Generate Document')
