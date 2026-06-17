class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        int maxArea = 0;
        stack<int> stack;

        for (int i = 0; i < n + 1; i ++){
            while (!stack.empty() && (i == n || heights[i] <= heights[stack.top()])){
                int h = heights[stack.top()];
                stack.pop();
                int w = 0;
                if(!stack.empty()){
                    w = i - stack.top() - 1;
                }else{
                    w = i;
                }

                maxArea = max(maxArea, w*h);
            }

            stack.push(i);
        }
        return maxArea;
    }
};
