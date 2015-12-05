while read line
do
   echo $line
   $command $line >> "res"
done < "commands"


