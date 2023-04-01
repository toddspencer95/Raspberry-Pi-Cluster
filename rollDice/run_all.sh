#!/bin/bash

for i in {0..1000}
	do
		#echo "Dice Roll: " $i
		#sbatch --export=ARGS="$i" --output=./results/roll_$i.out run.sh
		sbatch --output=/dev/null --error=/dev/null run.sh
		#sbatch --output=./results/roll_$i.out --error=./results/error_$i.out run.sh
done
