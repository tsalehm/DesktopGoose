# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

folderpath="C:\\Users\\saleh\\Desktop\\DesktopGoose\\pylauncher\\"

a = Analysis(
    [folderpath+'src\\installer.py'],
    pathex=[folderpath+"src"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += [('gooseicon.png', folderpath+'files\\gooseicon.png',  'DATA')]
a.datas += [('closegoose.bat', folderpath+'files\\closegoose.bat',  'DATA')]


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='installer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=folderpath+'files\\gooseicon.png',
    uac_admin=True,
)
