class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int partSum = nums[0];
    int finalSum = nums[0];
    int size = nums.size();

    for (int i = 1; i < size; i++) {
      if ((partSum + nums[i]) < nums[i]) {
        partSum = nums[i];
      } else {
        partSum += nums[i];
      }

      finalSum = (partSum > finalSum) ? partSum : finalSum;
    }

    return finalSum;
  }
};
