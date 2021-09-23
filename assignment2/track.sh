#!/bin/bash

function track {
    LOGFILE=~/.local/share/timer_logfile

    if ! [ -f "$LOGFILE" ]; then
        echo -n > $LOGFILE
    fi

    label=$2
    if [ $1 == "start" ]; then
        #Getting first word of last line
        tag=$( tail -n 1 $LOGFILE)
        #Getting last word
        taskName=${tag##* }
        set -- $tag
        #Checking if task is running
        if ! [ "$1" == "LABEL" ]; then
            #checking if input is valid
            if [ "$label" == "" ]; then
                echo "Please enter name of task. 'track start [taskName]"
            else
                                                    #STARTING TASK
    ##############################################################################################################################
                
                var1=$label

                label="LABEL This is $var1"
                date=$(date)

                startTimer="START $date"


                echo $startTimer >> $LOGFILE
                echo $label >> $LOGFILE

                echo "Started task '$var1'"
                
    ##############################################################################################################################

            fi
        else
            echo "You are already running task '$taskName', end it with 'track stop'"
        fi


    elif [ $1 == "stop" ]; then
        #Getting first word of last line
        tag=$( tail -n 1 $LOGFILE)
        set -- $tag
        #Cheking if task is running
        if [ "$1" == "LABEL" ]; then

                                                    #STOPPING TASK
    ##############################################################################################################################
                
                stopTimer="END $(date)"

                echo $stopTimer >> $LOGFILE
                echo "" >> $LOGFILE

                echo "Task ended"

    ##############################################################################################################################
        else
            echo "You are not running a task, start a task with 'track start [taskName] '"
        fi

    elif [ $1 == "status" ]; then
                                                    #STATUS
    ##############################################################################################################################

        tag=$( tail -n 1 $LOGFILE)
        taskName=${tag##* }
        set -- $tag
        if [ "$1" == "LABEL" ]; then
            echo "You are running a task '$taskName'"
        else
            echo "You have no running task"
        fi
    
    ##############################################################################################################################

    elif [ $1 == "log" ]; then
        
                                                    #LOG
    ##############################################################################################################################
        
        length=$(wc -l < $LOGFILE)

        for i in $(seq 1 4 $length)
        do
            k="$((i+1))"
            j="$((i+2))"

            startDate=$( sed -n "$i"p $LOGFILE)
            endDate=$( sed -n "$j"p $LOGFILE)
            labelSentence=$( sed -n "$k"p $LOGFILE)
            label=$(echo $labelSentence | awk '{print $NF}')

    ##############################################################################################################################


                                                    #CALCULATE DIFFERENCE
    ##############################################################################################################################

            firstWord=$(echo $endDate | awk '{print $1}')

            #If the task is not done yet
            if ! [ "$firstWord" == "END" ];then
                return
            fi

            #getting date in seconds
            startDate=$(echo "$startDate" | cut -d ' ' -f 2-;)
            #This works for mac
            #startDateSeconds=$(date -j -f '%a %b %d %T %Z %Y' "$startDate" '+%s')
            startDateSeconds=$(date -d "${startDate}" +"%s")

            endDate=$(echo "$endDate" | cut -d ' ' -f 2-;)
            #This works for mac
            #endDateSeconds=$(date -j -f '%a %b %d %T %Z %Y' "$endDate" '+%s')
            endDateSeconds=$(date -d "${endDate}" +"%s")

            diff="$((endDateSeconds-startDateSeconds))"
 
            #This works for mac
	        #timeSpent=$(date -j -u -f '%s' "$diff" '+%H:%M:%S')	


	        h=$((diff/3600 ))
            m=$(($((diff-h*3600))/60))
            s=$((diff-h*3600-m*60))

            timeSpent=$h"h":$m"m":$s"s"

            echo $label: $timeSpent

    ##############################################################################################################################

        done


    else
        echo "Invalid input, call script like this: track 'start [taskName]/stop/status/log' "
    fi
}

track $1 $2 $3
