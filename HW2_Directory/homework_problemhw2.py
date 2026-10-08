print(f'{" ":<12}'
    f'{"2024":>16}'
    f'{" ":>16}'
    f'{" ":>16}')
print(f'{"Line Item":<12}'
    f'{"Q1":>20}'
    f'{"Q2":>16}'
    f'{"Q3":>16}'
    f'{"Q4":>16}')
print('-' * 90) 

gross_domestic_product_Q1 = 28708.2
gross_domestic_product_Q2 = 29147
gross_domestic_product_Q3 = 29511.7
gross_domestic_product_Q4 = 29825.2

print(f'{"Gross Domestic Product":<12}'
    f'{gross_domestic_product_Q1:>16,.1f}'
    f'{gross_domestic_product_Q2:>16,.1f}'
    f'{gross_domestic_product_Q3:>16,.1f}'
    f'{gross_domestic_product_Q4:>16,.1f}')

personal_consumption_Q1 = 19443.8
personal_consumption_Q2 = 19756.1
personal_consumption_Q3 = 20032.8
personal_consumption_Q4 = 20351.3

print(f'{"Personal Consumption":<12}'
    f'{personal_consumption_Q1:>18,.1f}'
    f'{personal_consumption_Q2:>16,.1f}'
    f'{personal_consumption_Q3:>16,.1f}'
    f'{personal_consumption_Q4:>16,.1f}')

private_investment_Q1 = 5155
private_investment_Q2 = 5290.2
private_investment_Q3 = 5330.2
private_investment_Q4 = 5261.8

print(f'{"Gross Private Investment":<12}'
    f'{private_investment_Q1:>13,.1f}'
    f'{private_investment_Q2:>17,.1f}'
    f'{private_investment_Q3:>16,.1f}'
    f'{private_investment_Q4:>16,.1f}')

net_exports_Q1 = -822.5
net_exports_Q2 = -894.4
net_exports_Q3 = -938.3
net_exports_Q4 = -938.7

print(f'{"Net Exports":<12}'
    f'{net_exports_Q1:>25,.1f}'
    f'{net_exports_Q2:>17,.1f}'
    f'{net_exports_Q3:>15,.1f}'
    f'{net_exports_Q4:>16,.1f}')

government_Q1 = 4931.8
government_Q2 = 4995.2
government_Q3 = 5086.9
government_Q4 = 5150.7

print(f'{"Government Consumption":<12}'
    f'{government_Q1:>15,.1f}'
    f'{government_Q2:>17,.1f}'
    f'{government_Q3:>16,.1f}'
    f'{government_Q4:>17,.1f}')


sum_of_components_Q1 = net_exports_Q1 + private_investment_Q1 + personal_consumption_Q1 + government_Q1
sum_of_components_Q2 = net_exports_Q2 + private_investment_Q2 + personal_consumption_Q2 + government_Q2
sum_of_components_Q3 = net_exports_Q3 + private_investment_Q3 + personal_consumption_Q3 + government_Q3
sum_of_components_Q4 = net_exports_Q4 + private_investment_Q4 + personal_consumption_Q4 + government_Q4

print(f'{"Sum of Components":<12}'
    f'{sum_of_components_Q1:>20,.1f}'
    f'{sum_of_components_Q2:>17,.1f}'
    f'{sum_of_components_Q3:>16,.1f}'
    f'{sum_of_components_Q4:>17,.1f}')

print('-' * 90) 

def check_components(GDP_by_quarter, sum_of_components_by_quarter):
    """
    This function checks if the sum of the four components (Consumption, Investmnet, Net Exports, 
    and Government Expenditures) equals the  nominal GDP for the given Quarter 1 of 2024. 

    Inputs:
        GDP_by_quarter: Nominal GDP in the given quarter, float, in dollars.
        sum_of_components_by_quarter: Sum of all components of GDP in quarter 1, float, in dollars. 
    Output:
        Boolean
    """
    if GDP_by_quarter == sum_of_components_by_quarter:
        return True
    else:
        return False 

components_vs_GDP_Q1 = check_components(gross_domestic_product_Q1, sum_of_components_Q1)

components_vs_GDP_Q2 = check_components(gross_domestic_product_Q2, sum_of_components_Q2)

components_vs_GDP_Q3 = check_components(gross_domestic_product_Q3, sum_of_components_Q3)

components_vs_GDP_Q4 = check_components(gross_domestic_product_Q4, sum_of_components_Q4)

print(f'{"Compenents Equal GDP?":<12}'
    f'{str(components_vs_GDP_Q1):>14}'
    f'{str(components_vs_GDP_Q2):>17}'
    f'{str(components_vs_GDP_Q3):>16}'
    f'{str(components_vs_GDP_Q4):>17}')

print('-' * 90) 

def calculate_component_share_of_GDP(component, GDP):
    """
    This function calculates what share each component makes up of GDP. 

    Input:
        component: the component of GDP in a specific quarter, float, in dollars. 
        GDP: the nominal GDP of a specific quarter, float, in dollars. 
    Output: the component's share of GDP as a percentage. 
    """
    return component / GDP * 100

consumption_share_Q1 = calculate_component_share_of_GDP(personal_consumption_Q1, gross_domestic_product_Q1)

consumption_share_Q2 = calculate_component_share_of_GDP(personal_consumption_Q2, gross_domestic_product_Q2)

consumption_share_Q3 = calculate_component_share_of_GDP(personal_consumption_Q3, gross_domestic_product_Q3)

consumption_share_Q4 = calculate_component_share_of_GDP(personal_consumption_Q4, gross_domestic_product_Q4)

print(f'{"Consumption Share of GDP":<12}'
    f'{consumption_share_Q1:>13,.1f}'
    f'{consumption_share_Q2:>17,.1f}'
    f'{consumption_share_Q3:>16,.1f}'
    f'{consumption_share_Q4:>17,.1f}')

investment_share_Q1 = calculate_component_share_of_GDP(private_investment_Q1, gross_domestic_product_Q1)

investment_share_Q2 = calculate_component_share_of_GDP(private_investment_Q2, gross_domestic_product_Q2)

investment_share_Q3 = calculate_component_share_of_GDP(private_investment_Q3, gross_domestic_product_Q3)

investment_share_Q4 = calculate_component_share_of_GDP(private_investment_Q4, gross_domestic_product_Q4)

print(f'{"Investment Share of GDP":<12}'
    f'{investment_share_Q1:>14,.1f}'
    f'{investment_share_Q2:>17,.1f}'
    f'{investment_share_Q3:>16,.1f}'
    f'{investment_share_Q4:>17,.1f}')

net_export_share_Q1 = calculate_component_share_of_GDP(net_exports_Q1, gross_domestic_product_Q1)

net_export_share_Q2 = calculate_component_share_of_GDP(net_exports_Q2, gross_domestic_product_Q2)

net_export_share_Q3 = calculate_component_share_of_GDP(net_exports_Q3, gross_domestic_product_Q3)

net_export_share_Q4 = calculate_component_share_of_GDP(net_exports_Q4, gross_domestic_product_Q4)

print(f'{"Net Exports Share of GDP":<12}'
    f'{net_export_share_Q1:>13,.1f}'
    f'{net_export_share_Q2:>17,.1f}'
    f'{net_export_share_Q3:>16,.1f}'
    f'{net_export_share_Q4:>17,.1f}')

government_share_Q1 = calculate_component_share_of_GDP(government_Q1, gross_domestic_product_Q1)

government_share_Q2 = calculate_component_share_of_GDP(government_Q2, gross_domestic_product_Q2)

government_share_Q3 = calculate_component_share_of_GDP(government_Q3, gross_domestic_product_Q3)

government_share_Q4 = calculate_component_share_of_GDP(government_Q4, gross_domestic_product_Q4)

print(f'{"Government Share of GDP":<12}'
    f'{government_share_Q1:>14,.1f}'
    f'{government_share_Q2:>17,.1f}'
    f'{government_share_Q3:>16,.1f}'
    f'{government_share_Q4:>17,.1f}')
