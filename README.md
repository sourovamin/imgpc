# imgpc
Python scripts for bulk image processing (resize, convert, merge, resize to a certain size preserving best quality possible and so on) with command lines.

Features
```
- Bulk Image Processing
- Command Line Operation
- Resize, Convert and Merge
- Bulk Resize to a specific filesize keeping the best quality possible
```
Setup
```
Get the whole "imgpc" and run "imgpc.py" file from command line with parameters.
```
Bulk Convert Image Type
```
Parameters:
    --dir or -d: Directory containing images (Current directory, if no directory choosen) [optional]
    --action or -a (-a convert): Bulk Convert Image Type [required]
    --format or -f: Target format of the images [required]
    --destination or -df: Destination directory of the processed images [optional]
    
Example:
    python3 imgpc.py -d /Pictures -a convert -f png -df /Images/Converted 
```
Bulk Resize
```
Parameters:
    --dir or -d: Directory containing images (Current directory, if no directory choosen) [optional]
    --action or -a (-a resize): Bulk resize Images [required]
    --width or -w: Maximum width [required]
    --height or -ht: Maximum height [required]
    --fixed or -fx: Fixed dimensions (default: False) [optional]
    --format or -f: Target format of the images [optional]
    --destination or -df: Destination directory of the processed images [optional]
    
Example:
    python3 imgpc.py -d /Pictures -a resize -w 200 -ht 250 -f png -df /Images/Converted 
```
Bulk Resize up to a specific filesize
```
Parameters:
    --dir or -d: Directory containing images (Current directory, if no directory choosen) [optional]
    --action or -a (-a sizeup): Bulk resize Images up to a specific filesize [required]
    --size or -s: Maximum image size in bytes [required]
    --destination or -df: Destination directory of the processed images [optional]
    
Example:
    python3 imgpc.py -d /Pictures -a sizeup -s 50000
```
