# Python_VS_Rust
Rust takes on Python for the performance fight

# PROBLEM -  Loop and Count to 200 Million

## PYTHON
$> time python3.14 Loop_and_Count_to_200M.py  
Python Count: 200000000  
Python Time Taken: 7.9861 seconds  
python3.14 test.py  7.98s user 0.03s system 99% cpu 8.043 total  
$>    

## RUST  
$> rustc Loop_and_Count_to_200M.rs  
$> time ./Loop_and_Count_to_200M  
Rust Count: 200000000  
Rust Time Taken: 925.4450ms seconds  
./test  0.92s user 0.01s system 61% cpu 1.509 total  
$>  

## GO
$> go run test.go  
Go took: 41.187542ms
$>  
