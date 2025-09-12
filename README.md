CHANGE
1234

another one

TODO: add another workflow on submod - when pr is closed update submod sha to tot in base br

here we go again

### PreReqs
- GitHub token must be in secrets with read/write permissions in parent
    <small>_I don’t think yall will need to do this again since I configured for repo but I think it could be helpful to be aware of in case you do want to fork my repo._</small>
    - To create a token:
        - Click your profile picture in upper right corner
        - Go to settings
        - Scroll down go to developer settings
        - Click personal access tokens 
        - Dell will likely use a fine-grained token, I just set up a classic with the permissions that seemed right. 
        - Copy it somewhere safe you will never see it again
    - To add token to secrets: 
        § For Dell this would probably be added to the env for all the repos. I just added it to each repo individually. 
        § Go to each repo settings
        § Under the security section, click secrets and variables
        § Click Actions, add repository secret. 

### Misc notes: 

This was put together quickly just to give an idea of how an action works. There are some known issues that should be improved. For example, can't figure out why the post-action job failing even though the action passes. Also doesnt happen when creating the PR. The commit is happening and the run-action job succeeds, but its like there is cached metadata somewhere. Id also like details in the commit message, linking things into the details of the pr. When I was committing directly without creating a separate branch the sha was nonsense.

Right now fetch depth is 0
0: Represents all history for all branches and tags.
1: Represents the current commit HEAD
2: Represents the current commit and its parent HEAD^1
