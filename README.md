cleanup 
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
