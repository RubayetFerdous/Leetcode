use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

        let mut answer=HashMap::new();

        for (i, &index) in nums.iter().enumerate(){

            if let Some(&num)=answer.get(&(target-nums[i])){
                return vec![num as i32, i as i32];
            }else{
                answer.insert(index, i);
            }
        }

        vec![]
}
}