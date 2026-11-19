
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len() as i32;
        let cols = grid[0].len() as i32;

        if grid[0][0] == 1
            || grid[(rows - 1) as usize][(cols - 1) as usize] == 1
        {
            return -1;
        }

        let mut que = VecDeque::new();
        que.push_back((0, 0));

        let mut visited = HashSet::new();
        visited.insert((0, 0));

        let mut length = 1;

        let navigate = [
            (0, 1), (0, -1),
            (1, 0), (-1, 0),
            (1, 1), (-1, -1),
            (-1, 1), (1, -1),
        ];

        while !que.is_empty() {
            for _ in 0..que.len() {
                let (r, c) = que.pop_front().unwrap();

                if r == rows - 1 && c == cols - 1 {
                    return length;
                }

                for (i, j) in navigate {
                    let dr = r + i;
                    let dc = c + j;

                    if dr >= 0
                        && dr < rows
                        && dc >= 0
                        && dc < cols
                        && !visited.contains(&(dr, dc))
                        && grid[dr as usize][dc as usize] == 0
                    {
                        que.push_back((dr, dc));
                        visited.insert((dr, dc));
                    }
                }
            }

            length += 1;
        }

        -1
    }
}
