# Welcome Community Bridges Statistics Website!
Community Bridges is a non-profit based in Santa Cruz County that provides services in their programs. Their programs provide people access to transportation, healthy food, health care, and senior daycare. 
## What is the Purpose of this Website? How will it help Community Bridges?
The purpose of this website is to calculate statistics for individuals who are a representative of Community Bridges. These statistics will help the organization's grant providers understand which program needs more support. 
### Steps On How To Use The Website:
1. Put in the correct username and password authentication 
2. Click on the checkboxes you want
3. Press the "Calculate" button and you will see how many people benefit from the provided criteria
4. To upload a CSV file, please look at the Danger Zone steps below 
5. Log out of the website 

## DANGER ZONE STEPS:

Each individual person in the csv **MUST** have values from at least one of these options. 
They **ARE** Case and Space Sensitive. 
As you can see there are already weird exceptions such as ‘Multi-racial’ and ‘multi-racial’ which are technically the same, but because it is case sensitive the program reads them as different inputs. 
Because of this I added an exception towards this case and another one for Santa Cruz, so it will work with the current csv. In the future when you want to update the csv, to repeat, it must use these values or else the code will need to be updated. Thank you!

If you are ever worried about the program having an error, calculate the amount of people while using no specifications,
then calculate the amount of people with all of the check boxes marked in a certain category. If the number is the same then the program works!

*['La Manzana Community Resources', 'Nueva Vista Community Resources', 'Live Oak Community Resources', 'Mountain Community Resources']*

*['0-5', '19-59', '60 and Over', '6-18', 'Unknown']*

*['Multi-racial', 'multi-racial', 'Asian', 'American Indian or Alaska Native', 'White', 'Latino', 'Other', 'Black or African American', 'Native Hawaiian or Other Pacific Islander']*

*['Female', 'Male', 'Other']*

*['Other', 'Spanish', 'English']*

*['Monterey County', 'Watsonville', 'Santa Cruz ', 'South County', 'Santa Cruz County', 'Mid-County', 'San Benito County', 'Other', 'San Lorenzo Valley', 'Capitola', 'Scotts Valley', ‘Santa Cruz’]*

*['Below 100%', '100%-200%', '100-200%', 'Above 200%']*
