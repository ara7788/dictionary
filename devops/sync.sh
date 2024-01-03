#!/bin/bash
COMMIT=""
NEW_COMMIT=""
OLD_COMMIT=$(cat old_commit.txt )
clone_app(){
    git clone https://ara7788:***************@gitlab.com/ara77882/dictionary.git
}
git_pull(){
    echo "*******************git pull***************************" && \
    echo "" && \
    git pull && \
    echo "" && \
    echo "*******************reflog*****************************" && \
    echo "" && \
    git reflog -1 && \
    COMMIT=$(git reflog -1 | awk '{print $1}') && echo "HEAD COMMIT = $COMMIT" && \
    echo "" #&& \
    # echo "*******************log stat***************************" && \
    # echo "" && \
    # git log -1 --stat && \
    # echo "" && \
    # echo "*******************diff main**************************" && \
    # echo "" && \
    # git diff main^1
    # echo ""
}
sync_app(){
#   cd /home/ara7788/repos/dictionary/ && \
    echo "" && \
    echo "*******************rsync files************************" && \
    echo "" && \
    rsync -vrazh --exclude 'local_settings.py' --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' -p /home/ara7788/repos/dictionary/ /home/ara7788/dictionary/ && \
    echo ""
}
requirements_app(){
    cd /home/ara7788/dictionary/ && \
    pip3.9 install --user -r requirements.txt && \
    cd /home/ara7788/repos/dictionary/
}
migrations_app(){
    echo "*******************make migrations *******************" && \
    cd /home/ara7788/dictionary/ && \
    echo "" && \
    python3.9 manage.py makemigrations --merge && \
    echo "" && \
    python3.9 manage.py migrate && \
    echo "" && \
    cd /home/ara7788/repos/dictionary/ && \
    echo "*****************************************************"
}
restart_app(){
    echo "*******************restart web app *******************" && \
    echo "" && \
    pa_reload_webapp.py ara7788.pythonanywhere.com && \
    echo "" #&& \
}
create_admin(){
    cd /home/ara7788/dictionary/ && \
    python3.9 manage.py createsuperuser --username admin --noinput  --email ********** && \
    cd /home/ara7788/repos/dictionary/
    # python3.9 manage.py changepassword admin
}
check_repo(){
    if [ -d '/home/ara7788/repos/dictionary' ]
    then
        cd /home/ara7788/repos/dictionary
    else
        clone_app && \
        /home/ara7788/repos/dictionary
    fi
    git_pull && \
    NEW_COMMIT=$(git reflog -1 | awk '{print $1}') && cd .. && \
    if [[ "$OLD_COMMIT" == "$NEW_COMMIT" ]]
    then
        echo "******************* No updates found. **************************" && \
        echo "OLD_COMMIT=$OLD_COMMIT" && \
        echo "NEW_COMMIT=$NEW_COMMIT"
    else
        echo "******************* Updates detected! **************************" && \
        echo "OLD_COMMIT=$OLD_COMMIT" && \
        echo "NEW_COMMIT=$NEW_COMMIT" && \
        echo "****************************************************************"
        if [ -d '/home/ara7788/repos/dictionary' ]
        then
            sync_app && \
            # requirements_app && \
            migrations_app && \
            restart_app
        else
            clone_app && \
            sync_app && \
            requirements_app && \
            migrations_app && \
            create_admin && \
            restart_app
        fi
    fi && \
    cd /home/ara7788/repos/ && \
    echo $NEW_COMMIT > old_commit.txt && \
    NEW_COMMIT=''
}

check_repo && \
echo "******************* Deploy done! **************************"