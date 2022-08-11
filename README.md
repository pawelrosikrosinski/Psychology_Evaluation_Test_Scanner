# Psychology_Evaluation_Test_Scanner

CASE DESCRIPTION:

Over the years, Client have had produced heavy kilogrames of psy-eval papers with an urgency for digitalization.

SOLUTION:

digital scanner -> ftp server -> extractor.sh -> stai(1 | 2).py -> *.txt (result)

I have noticed digital scanner machine with high enough throughput and functionality to send created pdf's into a ftp server.
Using this opportunity, I have created systemd service, that constantly checks ftp://~/pdf directory for new documents.
If any, images are extracted, then converted to .png format to exclude any codec incompatibilities.
Images are then processed with coresponding .py scripts. Here, I present only the ones for 'Stait Trait Anxiety Inventory'.
Input data often require normalization:
  1. 'deskew' library to erase non orthogonal scan angles
  2. 'cv2' to increase contrast
  
Later library is also used to find countures around answer box, so it is easy to assume which spots have been manually altered.

---
