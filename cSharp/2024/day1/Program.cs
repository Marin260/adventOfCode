using day1.SolverAOC;

SolverAOC day1 = new SolverAOC();

day1.dataLoader();
day1.createLists();

var partOneSolution = day1.partOne();
Console.WriteLine(partOneSolution);

var partTwoSolution = day1.partTwo();
Console.WriteLine(partTwoSolution);

