# Psychology_Evaluation_Test_Scanner

CASE DISCRIPTION:

Client have had heavy kilogrames of psy-eval papers, that needed to be digitalized quickly.

SOLUTION:

digital scanner -> ftp server -> extractor.sh -> stai(1 | 2).py -> *.txt (result)

I have noticed digital scanner machine with high enough thoruput and functionality to send created pdf's to ftp server.
Using this opportunity, I have created systemd service, that constantly checks ftp://~/pdf directory for new documents.
If any, images are extracted, then converted to *.png format to exvlude any codec incompatibilities.
Images are then processed with coresponding .py scripts. Here, I present only the ones for 'Stait Trait Anxiety Inventory'.
Input data often require normalisation:
  1. 'deskew' library erase non ortogonal scan angles
  2. 'cv2' increase contrast
Later library is also used to find countures around answer box, so it is easy to assume which spots have been menually altered.
