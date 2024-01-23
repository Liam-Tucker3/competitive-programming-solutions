#include <cstring>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int new_face(int curr_face, string direction) {
  if (direction == "Left")
    curr_face -= 1;
  if (direction == "Right")
    curr_face += 1;
  if (curr_face <= 0)
    curr_face += 4;
  if (curr_face >= 5)
    curr_face -= 4;
  return curr_face;
}

int main(int argc, char *argv[]) {

  int x_coord;
  int y_coord;
  cin >> x_coord;
  cin >> y_coord;

  int num_instructions;
  cin >> num_instructions;

  int x_pos = 0;
  int y_pos = 0;
  int facing = 1;

  string poss_instructions[] = {"Right", "Forward", "Left"};
  string instruction_list[num_instructions];
  string this_instruction;
  for (int t = 0; t < num_instructions; t++) {
    cin >> this_instruction;
    instruction_list[t] = this_instruction;
  }

  for (int i = 0; i < num_instructions; i++) {
    // this_instruction is our current instruction we're looking at
    this_instruction = instruction_list[i];

    for (int j = 0; j < 3; j++) {
      // alt_instruction is the alternate instruction we're considering
      string alt_instruction = poss_instructions[j];

      if (this_instruction != alt_instruction) {
        int this_xpos = x_pos;
        int this_ypos = y_pos;
        int this_facing = facing;

        // Executing alternate instruction
        if (alt_instruction == "Forward") {
          if (this_facing == 1)
            this_ypos += 1;
          else if (this_facing == 2)
            this_xpos += 1;
          else if (this_facing == 3)
            this_ypos -= 1;
          else if (this_facing == 4)
            this_xpos -= 1;
        } else {
          this_facing = new_face(this_facing, alt_instruction);
        }
        // Running through the rest of the instructions
        for (int k = i + 1; k < num_instructions; k++) {
          // Current instruction in rest of instructions
          string curr_instruction = instruction_list[k];
          if (curr_instruction == "Forward") {
            if (this_facing == 1)
              this_ypos += 1;
            else if (this_facing == 2)
              this_xpos += 1;
            else if (this_facing == 3)
              this_ypos -= 1;
            else if (this_facing == 4)
              this_xpos -= 1;
          } else {
            this_facing = new_face(this_facing, curr_instruction);
          }
        }
        // Completed rest of instructions in alternate universe
        if (this_xpos == x_coord && this_ypos == y_coord) {
          // Printing desired output
          string output = to_string(i + 1) + " " + alt_instruction;
          cout << output << endl;
          return 0;
        }
      }
    }
    if (this_instruction == "Forward") {
      if (facing == 1)
        y_pos += 1;
      else if (facing == 2)
        x_pos += 1;
      else if (facing == 3)
        y_pos -= 1;
      else if (facing == 4)
        x_pos -= 1;
    } else {
      facing = new_face(facing, this_instruction);
    }
  }

  return 0;
}