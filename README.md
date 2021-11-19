<head><b>Ex1 Elevator</b></head></br>
<u>authors: Dima Sanin, Josef Sokolov, Sali Sharfman</u></br></br>
We have a problem and it is the management of an elevator system in a high-rise building
 Describing the working method of mrmattandmrchay first, we watched two videos of </br>https://www.youtube.com/watch?v=BCN9mQOT3RQ</br> single elevator</br>
https://www.youtube.com/watch?v=oY1QlCqWOss</br>
This video gave us the idea to model the problem, to build an object that would describe an elevator and meet all the requirements we would like to get from a single elevator so we could integrate the elevators into the system of the entire building.
We then read an article by Brendan Paris describing how to deal with the problem of optimizing elevator management and we got ideas that we used to find a solution to the problem.</br>
https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30 </br>
After reviewing the literature we have done, the main conclusions we have reached are that first we will have to build a department that will describe an elevator, this elevator is given parameters that will help us decide whether to send it for summons or another and through additional departments we will solve the problem.



This is an offline algorithms of elevator algorithms, we're going to split this project to five classes Elevator, CallForElevator, Building, Calls_List and Ex1. We going to seed building class with json data. CallForElevator with csv data. Ex1 class uses building as argument for its constructor. 



The UML diagram presents the division of our classes:  [UML class Ex1.pdf](https://github.com/SaliSharfman/Ex1/files/7558381/UML.class.Ex1.pdf) 

<img width="1093" alt="Screen Shot 2021-11-18 at 0 26 08" src="https://user-images.githubusercontent.com/77780368/142292660-9e334563-a6ea-4cb0-819f-b4cb4172e69d.png">
</br>
Our Algorithm goes over a list of calls and for each call it goes over each elevator and allocates the elevator with a minimal time for processing the current call.</br>In this way we have a couple of casses.</br> Case 1: There are not previous calls to current an Elevator, so algorithms just calculates the time that will take to the current Elevator to finsh the call, Because in each Elevator we have different settings(speed, time for open/close etc.)</br>Our algorith will find the most suitable elevator to the call.</br> Case 2: There are previous calls to the current Elevator, so the algorithm just calculates a global time, how much it will take to finish all the calls that the elevator has, and our algoritm will find the best elevator with the minimal time to ariive to the call and finish it.</br>Just like in case1 it depends on the settings of the Elevator but in this case we also calculate the previous calls. </br></br>
After writing the algorithm we got 4 different calls lists in csv files and 5 different buildings in json files.</br>
we have checked our algorithm with a run file that simulate the elevators activities and give us information about the algorithm execution including avarage waiting time, Number on incomplete calls and Certificate.</br>
</br><b>Instrucciones for running the jar file from the cmd:</b></br>
1.open cmd.</br>
2.cd the direction of the project folder.</br>
4. write the next command: python Ex1.py B1.json Calls_b.csv out.csv </br>  (example for building 1 and calls b case, if you have python 3 in your computer start the command with python3.)</br>
<b> the algorithem will be runned on your computer and the file "out.csv" with the elevators allocations is saved in the project folder.</b></br>
5.write the next command:java -jar Ex1_checker_V1.2_obf.jar 209128966,337959928,324466671 B2.json out.csv out.log (write the same building you used before)</br>
 <b>now you will see the case log and results the file "out.log" with the case log an results is saved in the project folder.</b></br>
 </br><b>example for cmd output of call_a.csv and b2.json</b></br>
<img width="1093" alt="Screen Shot 2021-11-18 at 0 26 08" src="https://user-images.githubusercontent.com/86108478/142305794-c6a3a919-7bdd-4ee6-90df-ccb12c22f5b5.png">
<img width="1093" alt="Screen Shot 2021-11-18 at 0 26 08" src="https://user-images.githubusercontent.com/86108478/142690292-89c20fcb-3c84-4407-aff5-943a71c3db10.png">

</br><b>the results of our algorithm in the different cases:</b></br><img width="1093" alt="Screen Shot 2021-11-18 at 0 26 08" src="https://user-images.githubusercontent.com/86108478/142301108-c36181ee-7ade-4904-a6b4-99515c45532d.png"></br>Also we did tests to our programm. First test checks if our algorithm works correctly: allocates the elevator with minimal time. Second test cheks if our function to load scv file to list of calls works correctly and loads from csv for real. 
