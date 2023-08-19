call python setup.py sdist bdist_wheel
echo "Built Project!"
call twine upload dist/*
echo "Uploaded Project!"