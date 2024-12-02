namespace day2.Solver;

class SolverAoc {
    public int tot1 = 0;
    public int tot2 = 0;
    private string ? AocData { get; set; } = "";
    private List<string> data = []; 

    public void dataLoader(){
        try{
            StreamReader str = new StreamReader("./input.txt");

            while (AocData != null){
                AocData = str.ReadLine();
                Console.WriteLine(AocData);
                if (AocData != null){
                    data.Add(AocData);
                }
            }
            str.Close();
        }
        catch(Exception e){
            Console.WriteLine("Exception: " + e.Message);
        }
    }

    public bool isSorted(List<int> level){
        var ascLevel = level.OrderBy(x => x).ToList();
        var dscLevel = level.OrderByDescending(x => x).ToList();

        if (level.SequenceEqual(ascLevel) || level.SequenceEqual(dscLevel)){
            return true;
        }
        return false;

    }
    public int parOne(){
        foreach (var line in data){
            var level = new List<int>{};
            var isValid = true;
            foreach (var el in line.Split()){
                level.Add(int.Parse(el));
            }

            for (int i = 0; i < level.Count - 1; i++){
                var diff = Math.Abs(level[i] - level[i+1]);
                if (diff < 1 || diff > 3){
                    isValid = false;
                }
            }

            if (isSorted(level) == true && isValid){
                tot1 += 1;
            }
        }
        return tot1;
    }
}