INNODB_PAGE_SIZE = 16 * 1024 * 1024

# Start of the data on the page
FIL_PAGE_DATA = 38

FIL_PAGE_OFFSET = 4  # page offset inside space
FIL_PAGE_TYPE = 24  # File page type

# Types of an undo log segment */
TRX_UNDO_INSERT = 1
TRX_UNDO_UPDATE = 2

# On a page of any file segment, data may be put starting from this offset
FSEG_PAGE_DATA = FIL_PAGE_DATA

# The offset of the undo log page header on pages of the undo log
TRX_UNDO_PAGE_HDR = FSEG_PAGE_DATA

PAGE_LEVEL = 26  # level of the node in an index tree; the leaf level is the level 0 */

innodb_page_type = {
    '0000': 'Freshly Allocated Page',
    '0002': 'Undo Log Page',
    '0003': 'File Segment inode',
    '0004': 'Insert Buffer Free List',
    '0005': 'Insert Buffer Bitmap',
    '0006': 'System Page',
    '0007': 'Transaction system Page',
    '0008': 'File Space Header',
    '0009': '扩展描述页',
    '000a': 'Uncompressed BLOB Page',
    '000b': '1st compressed BLOB Page',
    '000c': 'Subsequent compressed BLOB Page',
    '45bf': 'B-tree Node'
}

innodb_page_direction = {
    '0000': 'Unknown(0x0000)',
    '0001': 'Page Left',
    '0002': 'Page Right',
    '0003': 'Page Same Rec',
    '0004': 'Page Same Page',
    '0005': 'Page No Direction',
    'ffff': 'Unkown2(0xffff)'
}

INNODB_PAGE_SIZE = 1024 * 16  # InnoDB Page 16K
