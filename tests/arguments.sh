# for p; do printf "(%s)" "$p"; done; echo " [$#]"
echo "$@"
python3 arguments.py $@
