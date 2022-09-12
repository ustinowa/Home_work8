import business_logic
import UI

var = UI.input_()

if var == 1:
    business_logic.read_file()
elif var == 2:
    business_logic.write_file()
elif var == 3:
    business_logic.delete_row()
elif var == 4:
    business_logic.next_class()

