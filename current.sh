#echo ${1} ${2}
curl -i -u username:password --silent --output /dev/null -XPOST 'http://yourinfluxdbserver.yourdomain.it:8086/write?db=yourdb' --data-binary "currentcost,type=temperature, meterlocation=whereisit value=${2}
currentcost,type=watt,meterlocation=whereisit value=${1}"