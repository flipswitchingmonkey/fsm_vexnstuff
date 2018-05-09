# fsm_vexnstuff
A collection of various Houdini related scripts and notes

Contains both Python and VEX and maybe some OTLs eventually.

# incremental save
The incremental save script follows these rules:
- retain padding (file001 will become file002)
- increment only last occurrence (file1_v01 will become file1_v02)
- increment also within filename (file01_edit will become file02_edit)
- append versioning if there is none (file will become file_001)
- do not overwrite but skip existing versions (file_001 will become file_003 if file_002 exists)
