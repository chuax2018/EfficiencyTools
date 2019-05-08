
if [ x$1 != x ]; then
	echo "making project $1"
else
	echo "init_prj.sh [prj_name]: project name is null."
	exit 1
fi

mkdir -p $1/build
cd $1
mkdir bin
mkdir src
mkdir libs
mkdir include
cd ..
python3 ./gen_CMakeLists.py $1
echo "project $1 init done."
echo "enjoy your coding time."
