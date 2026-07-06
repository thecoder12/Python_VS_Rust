# Python_VS_Rust
Rust takes on Python for the performance fight

# PROBLEM -  Loop and Count to 200 Million

## PYTHON MULTI-THREADING
$> time python3.14 Multi-threading.py  
Python threads starting... (Grab a coffee, this will take a bit)  
Python threaded execution time: 34.96 seconds  
python3.14 Multi-threading.py  34.81s user 0.16s system 99% cpu 35.041 total  
$>  
## PYTHON MULTI-PROCESSING
$> time python3.14 multi_processing.py  
Python multiprocessing starting... (Watch your CPU usage spike to 200%!)  
Python multiprocess execution time: 17.46 seconds  
python3.14 multi_processing.py  34.67s user 0.09s system 198% cpu 17.516 total  
$>  

## RUST
$> time ./NO_GIL  
Rust threads starting... Done!  
Results to prevent compiler skipping: 179700 and 179700  
Rust threaded execution time: 4.7751s seconds  
./NO_GIL  9.52s user 0.02s system 198% cpu 4.815 total  
$>  