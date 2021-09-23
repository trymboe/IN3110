#!/bin/bash

function move {
	src=$1
	dst=$2
	type=$3

	

	#checking arguments
	if [ -z "$src" ] || [ -z "$dst" ] || [ -z "$3" ] || ! [ -z "$4" ] ; then
		echo "You need three arguments, call the script like this
./move.sh src dst type
Where src is source directory, dst is destination directory and type is the file type."
		return
	fi

	#checking if src and dst is valid
	if ! [ -d "$src" ]; then
  		echo "$src is not a directory."
		return
	fi
	
    if ! [ -d "$dst" ]; then
            echo "$dst is not a directory, do you want to make it?
y/n "

	
		read answer
		while [ $answer != "y" ] && [ $answer != "n" ]; do
			echo "y/n"
			read answer
		done

		#not making directory
		if [ $answer == "n" ]; then
			echo "did not make directory, please run script again and enter valid directory"
			return
		fi		

		#making directory
		if [ $answer == "y" ]; then
			echo "Do you want to add timestamp (YYYY-MM-DD-hh-mm) to the name?
y/n"
		fi
					
		read answer
		while [ $answer != "y" ] && [ $answer != "n" ]; do
			echo "y/n"
			read answer
		done
				
		if [ $answer == "y" ]; then
			mkdir "$dst$(date +%Y-%m-%d-%H-%M)";
			dst="$dst$(date +%Y-%m-%d-%H-%M)"
			echo "made directory $dst"
		fi
		if [ $answer == "n" ]; then
			mkdir "$dst";
			echo "made directory $dst"
		fi


	fi


	
	#Checking if sources are full path
	if [ -d "~/$src" ]; then
		srcUse="~/$src/*"
	else
		srcUse="$src/*"
	fi
	if [ -d "~/$dst" ]; then
		dstUse="~/$dst/"
	else
		dstUse="$dst/"
	fi

	
	if [ $3 = "all" ]; then
		mv -v $srcUse $dstUse
	else
		mv -v $srcUse$3 $dstUse
	fi

	
		
}

move $1 $2 $3 $4  

