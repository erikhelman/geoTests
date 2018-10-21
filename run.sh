export PATH="$PATH":/home/erik/jmeter/bin

FOLDER=`date +%Y%m%d%H%M%S`
mkdir $FOLDER

pytest test_geo_functional.py --html=$FOLDER/geo_functional_`date +%Y%m%d%H%M%S`.html
pytest test_geo_negative.py --html=$FOLDER/geo_negative_`date +%Y%m%d%H%M%S`.html

jmeter -n -t geo_perf_test.jmx -l geo_perf_log_`date +%Y%m%d%H%M%S`.jtl -e -o $FOLDER/perf

