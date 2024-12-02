namespace day1.SolverAOC;
public class SolverAOC
{
    private int total1 { get; set;} = 0;
    private int total2 { get; set;} = 0;

    public string ? AocData { get; set; } = "";
    private List<string> InputData {get; set;} = [];
    private List<int> Left = [];
    private List<int> Right = [];
    public void dataLoader() {
        try{
            StreamReader str = new StreamReader("./input.txt");
            while (AocData != null)
            {
                AocData = str.ReadLine();
                if (AocData != null){
                    InputData.Add(AocData);
                }
            }
            str.Close();
        }
        catch(Exception e)
        {
            Console.WriteLine("Exception: " + e.Message);
        }
        finally
        {
            Console.WriteLine("Executing finally block.");
        }
    }

    public void createLists() {
        foreach (var line in InputData){
            var splitedLine = line.Split("   ");
            Left.Add(int.Parse(splitedLine[0]));
            Right.Add(int.Parse(splitedLine[1]));
        }
        Left.Sort();
        Right.Sort();
    }

    public int partOne() {
        var ziped = Left.Zip(Right, (x, y) => new List<int>() {x, y});
        foreach (var el in ziped){
            total1 += Math.Abs(el[0] - el[1]);
        }
        return total1;
    }

    public int partTwo(){
        foreach (var el in Left){
            var elOccurances = Right.Where(x => x == el).ToList();
            total2 += el * elOccurances.Count;
        }
        return total2;
    }
}