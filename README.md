## Useful resources:
- **GitHub Actions Documentation** – <https://docs.github.com/en/actions>
    - _Basically_ every job/ matrix strategy/ event trigger/ variable type can be found somewhere in these docs if you know what you're looking for. Even links to examples of workflow or yml syntax 
- **GitHub CLI Manual** – <https://cli.github.com/manual/>
- **GitHub REST API Quickstart** – <https://docs.github.com/en/rest/quickstart?apiVersion=2022-11-28>
    - REST: Get a pull request https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request
- **Published actions** - <https://github.com/actions>
- **General yml ref** - <https://learnxinyminutes.com/yaml/>
- **Example action** - <https://github.com/marketplace/actions/github-action-submodule-updates>
- **Tutorials (from github.com)** - <https://docs.github.com/en/actions/tutorials/create-an-example-workflow>
    - I didnt manually do any of these but I did briefly read over them. 
- **GraphQL ref** - <https://docs.github.com/en/graphql/reference/mutations#revertpullrequest>
- **Octokit** - <https://github.com/octokit>

Base change 1


1. pre-check base for conflicts and approvals 
2. Determine changed submod from PR diff and their sha
3. Parse .gitmodules 
4. enrich submod info with default branches, repo name, base branch pr branch and pr number 
5. pre-check submodules for conflicts and approvals 
6. shallow checkout base 
7. setup GPG and auth for bot user 
8. init submodule pr branches
9. merge submods 
    - squash all commits if needed sign and push back up to pr branch 
    - rebase 
    - pre-form commit title and body (including pr link)
    - merge --ff-only sign and commit submodule merge  
10. bump submodules 
11. squash all commits and push back up to pr branch 
12. manual rebase to resolve pointer conflicts 
13. sign and push up to pr brnach 
14. merge base 
    - pre-form commit title and body including pr link
    - merge --ff-only sign and commit base merge
    

