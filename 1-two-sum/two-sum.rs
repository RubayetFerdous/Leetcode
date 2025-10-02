impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

        let mut list: Vec<i32>=Vec::new();

        for i in 0..nums.len(){
            if nums[i+1..nums.len()].contains(&(target-nums[i])){
                list.push(i as i32);
                break;
            }
        }
        for j in (0..nums.len()).rev(){
            if nums[0..j].contains(&(target-nums[j])){
                list.push(j as i32);
                break;
            }
        }
        return list;
    }
}