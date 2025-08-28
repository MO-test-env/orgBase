play with REST API to commit stuff

PreReqs
    - Parent repo has .gitmodules configured
    - GitHub token must be in secrets with read/write permissions in parent
        I don’t think yall will need to do this again since I configured for repo but I think it could be helpful to be aware of in case you do want to fork my repo. 
        ○ To create a token:
            § Click your profile picture in upper right corner
            § Go to settings
            § Scroll down go to developer settings
            § Click personal access tokens 
            § Dell will likely use a fine-grained token, I just set up a classic with the permissions that seemed right. 
            § Copy it somewhere safe you will never see it again
        ○ To add token to secrets: 
            § For Dell this would probably be added to the env for all the repos. I just added it to each repo individually. 
            § Go to each repo settings
            § Under the security section, click secrets and variables
            § Click Actions, add repository secret. 
    - Submodule must have a .github/workflows/any-file-name.yml
    - There must be a branch in the parent repo that you want the submodule update commit to be added to 
        ○ For now I specifed it as CHECKOUT_BRANCH and PR_AGAINST_BRANCH of sup.yml
    - There must be a branch in the submodule repo that you want to create and close a pr for
        ○ For now I specified in the trigger "mo/br5"
For actual implementation, the parent and child branches would be the same and not need specifying. 
    

How it works right now:
    - I know the workflow looks like it fails. There is an unknown post run action that reaches an index out of range error. The functionality of action.yml, post checkout parent, and cleaning orphan processes are fine. I did not get a chance to read enough to fix that. Sorry. 
    - What kicks off a workflow
        ○ In .github/workflows/sup.yml, that "on" section means currently it triggers when there is a push to main && the pull request on branch mo/br5 is closed. 
        ○ For testing, if you are the only one messing with the repo (like in a fork) it can be nice to change the "main" in branches to "**" and remove the pull requests section then the workflow will run on every push. 
        
    - Example workflow and its commit directly on mo/br5 
        ○ https://github.com/MOvenshire/submod/actions/runs/17304127942
        ○ https://github.com/MOvenshire/base/commit/cbf0d9dc8e61c3c9a7bb06da52339edc0e4b3a65
    - Example workflow and its pull request with the option 2 uncommented 
        ○ https://github.com/MOvenshire/submod/actions/runs/17303801102/job/49121445043
            § #45 That 17303801102 is the GITHUB_RUN_ID
            § https://github.com/MOvenshire/base/pull/14
    
    


Misc notes: sup is my git alias for submodule update. It was just easier to type the shorthand to get something together quickly.
This was put together quickly just to give an idea of how an action works. There are some known issues that should be improved. For example, why is the post-action job failing. The commit is happening and the run-action job succeeds, but its like there is cached metadata somewhere. Id also like details in the commit message, linking things into the details of the pr. When I was committing directly without creating a separate branch the sha was nonsense.

Right now fetch depth is 0
0: Represents all history for all branches and tags.
1: Represents the current commit HEAD
2: Represents the current commit and its parent HEAD^1
 
