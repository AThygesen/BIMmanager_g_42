**Group 42 - Assignment A3**

**About the Tool:**

**State the problem/claim that your tool is solving:**

Knowing an estimate of your project's cost at any stage is essential for effective budget management. When you have an idea of the costs upfront, it allows you to make informed decisions about resource allocation, identify potential financial risks early, and make adjustments before expenses spiral out of control. With accurate cost estimates, you can assess whether the project is tracking towards its financial goals and whether you’re staying within budget constraints. This tool helps make rough estimates during the design phase. 

**State where you found that problem:**

The problem was not found directly in the IFC-files but is a general problem when it comes to project management. Many larger building projects in the later years has had issues with keeping to budgets and this tool can help eliveate some of those issues

**Description of the tool:**

The tool pulls available product data from the IFC file. The tool creates a CSV-file/dataframe with a list of the chosen elements and the relevant dimensions for each. The element names/ID are then compared to another database filled with a unit-prices for each element. If a match is found the tool takes the unit-price and dimensions and calculates the total price for each kind of element. The final product of the tool is then a list of each element and their prices. Therefor also a total material cost of the building. In future cases the database could include construction cost which would make the final result even more accurate. 

**Instructions to run the tool:**

Load the chosen IFC file with in you python IDE, then load your database and run the file. We have made an example/mock database to show how it would work. Run the script and you will get an excel sheet with the elements, amounts and prices.


**Advanced Building Design:** 

**What Advanced Building Design Stage (A, B, C or D) would your tool be useful?**

This tool is mostly relevant in stage B and C. The tool can create a quick estimate of an existing design, this can help in the design end of a desgin fase and in the building fase, where the contractor needs to make a bid for the case. The overview that the tool will be able to provide, can become a strong tool for the industry in these fases. 

**Which subjects might use it?** 

The tool could be use full for both consulting and contracting firms. For the consulting firms it can be use to make a more precises price estimate for the projekt porposal an on, when the bim model is more or less finished. The consulting firm can also be used to confirm a contracters bid, before accepting it. 
The contracters could use it in the same way, when giving a bid for a potential construction, a lot of time would be saved if they could run the program, instead of having to count every single element in a drawing or model. 

**What information is required in the model for your tool to work?** 

The model needs both database and an IFC file with needed meassurements, for a concrete beam it could be the length, a wall it would be the total m2. If the tool is utilized by a consulting firm, it would be very benificial for the department of BIM-analyst to co-ordinate with the projekt leaders to make a standard for the IFC classifications. 
