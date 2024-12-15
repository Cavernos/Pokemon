# -*- mode: python ; coding: utf-8 -*-
import os

datas = [('.\\src\\app\\assets', '.\\assets'), ('.\\src\\app\\config', '.\\config')]
for root, directories, files in os.walk('.\\src\\app\\'):
    if "config.py" in files:
        datas.append((os.path.join(root, "config.py"), ''.join(root.split('\src'))))

a = Analysis(
    ['src\\app\\main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
          a.scripts,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon="src\\app\\assets\\img\\icon.ico"
)
coll = COLLECT(
   exe,
   a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
