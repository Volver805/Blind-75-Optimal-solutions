public class Solution {
    public int[] TwoSum(int[] arr, int target) {
        Dictionary<int, int> lookUp = new Dictionary<int, int>();
        for (int i = 0; i < arr.Length; i++)
        {
            int comp = target - arr[i];
            if (lookUp.ContainsKey(comp))
            {
                return new int[] {lookUp[comp], i};
            }
            lookUp[arr[i]] = i;
        }
        return null;
    }
}