NAME=$1
echo $NAME
obsidian-export . --start-at "$NAME" "./exp_$NAME"
mv "$NAME" "old_$NAME"
mv "exp_$NAME" "$NAME"





#pandoc -t html --css mystyles.css input.md -o output.pdf


