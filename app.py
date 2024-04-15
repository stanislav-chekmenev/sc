import gradio as gr

from app_logic import estimate_net_salary

# Create the slider for salary input.
salary_slider = gr.components.Slider(minimum=80e3, maximum=200e3, label="Gross annual salary")

# Create switch inputs.
self_employed = gr.components.Checkbox(label="Self-employed")

# Create text to explain the taxes calculation
explanation = """
# Salary estimation factors

### Taxes
 - Income tax is 42%. A lump sum of 10600 is deducted after applying the tax rate, which accounts to a tax threshold in the calculation of individual taxes.
 - VAT is 19%. It is only applied to self-employed people.
 - Additional trade tax rate of 3% is to be paid after opening a business.
 - Solidarity 1.6% tax rate. It's a German specific tax to help rebuild Germany after WWII.
  
### Insurances
 - Health insurance is 14.6% capped at 993 Euro a month, which would amount to 11916 a year.
 - Retirement contribution is 18.6% capped at 1311 Euro a month, which would amount to 15735 a year.
 - Unemployment insurance is 2.4% and capped at 170 Euro a month, 2030 a year.
  
### Employment/Self-employment
 - For self-employed people, the health insurance and retirement are to be paid in full.
 - For employees the health insurance and retirement are split 50/50 between the employer and the employee.


### Conclusion

- Some minor and complex tax deductions were not taken into account. 
- **Based on the estimations above and my desire to earn around 4000 Euro a month, the projected self-employed salary would be around 160K Euro a year.**

### How do I know the estimation is correct?

The estimation for the case of regular employment was tested against a German salary calculator and the results were very close. The calculator can be found [here](https://www.brutto-netto-rechner.info/gehalt/gross_net_calculator_germany.php). The data it was tested with is the following:

- Gross salary: 100000 Euro
- Age of the employee: 35
- Federal state: Berlin
- Tax category: 1
- Church tax: No
- Compulsory health, pension and care unemplyoment insurance: Yes
- Health insurance add on: 4 % (not included in the calcualtion in the app)


"""

# Create output interfaces.
net_salary = gr.components.Textbox(label="Estimated net annual salary")

# Define the Gradio interface.
iface = gr.Interface(
    fn=estimate_net_salary,
    inputs=[salary_slider, self_employed],
    outputs=[net_salary],
    title="Salary Estimator",
    description="Adjust the salary and toggle switch to see how the outputs change.",
    article=explanation

)

# Launch the app.
iface.launch()
