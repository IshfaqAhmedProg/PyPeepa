@echo off
rmdir /s /q "build"
echo "Deleted Build!"
@echo off
rmdir /s /q "dist"
echo "Deleted Dist!"
call python setup.py sdist bdist_wheel
@echo off
echo "Built Project!"
call twine upload dist/*
@echo off
echo "Uploaded Project!"