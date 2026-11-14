class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap map = new HashMap(nums.length);
        int count = 0;
        while(count < nums.length) {
            int temp = target - nums[count];
            if(map.get(temp) != null) {
                int value = (int)  map.get(temp);
                return new int [] {value, count};
            } 

            map.put(nums[count], count);
            count = count + 1;
        }
       return null; 
    }
}
