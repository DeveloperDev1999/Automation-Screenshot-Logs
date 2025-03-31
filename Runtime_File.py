import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Test_Execution.Context_Click import main
from Test_Execution.File_Upload import main2
from Test_Execution.Horizontal_Slider import main3

if __name__ == "__main__":
    main()
    main2()
    main3()
