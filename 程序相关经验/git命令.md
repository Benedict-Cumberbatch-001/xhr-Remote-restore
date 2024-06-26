## Git命令
1. `github`项目页面按住.键可以跳转至类似VS的页面中，查看项目结构

2. `git` 清屏的方式：快捷键 `Ctrl + L`或者命令`clear`

3. `git init` //初始化仓库

4. `git config --global --list` //查看全局配置
```shell
user.email=1710745401@qq.com
user.name=xuhaoran
http.proxy=http://127.0.0.1:10809
```
5. `git config --global --unset http.proxy`//取消http的现有代理

6. `git config --global http.proxy 127.0.0.1:10809`//设置中查看自己电脑的端口，然后使用系统代理设置
7. `git config --global http.proxy` 代理地址:端口号   //设置http代理

8. `v2rayN`中的监听端口默认设置的是`10808`，这时候系统设置的`http`代理端口是`10809`而且是默认的，系统的端口会比监听端口的数值多1。全局代理的配置文件`.gitconfig`通常在：`C:\Users\你的用户名\.gitconfig`。当`.gitconfig`中的设置的代理端口与系统设置里面的代理端口不一样的时候，git就会出错

9. `git config --global --get http.proxy`//查看当前代理设置
//当设置了系统代理，则必须开启`vpn`才能`push`到`gitee`和`GitHub`
//如果未设置系统代理，只能上传到`gitee`，而不能上传到`github`

10. `git log --pretty=oneline`//在一行显示内容，只显示哈希码和-m

11. `git log --oneline` //比上面的更简洁，显示部分哈希码和-m

12. `git reflog` //显示部分哈希码和-m以及版本步
修改完某个文件应当先添加add，
13. `git add .`  //命令是一次性添加全部修改后的文件
注意看`git status`的状态，红色代表要添加，绿色代表要提交

11. //建立远程库
在`github`上 点击`new repository`，填写表单
码云的私密仓库不收费，`GitHub`收费

12. `git remote -v` //查看当前的本地库储存的远程库地址

13. `git remote add` 地址名命 http://.......... //添加远程库地址

14. `git push` 地址名 分支 //推送本地仓库到远程仓库

15. `git fetch` //抓取远程库，下载到本地，但不会更改本地工作区的文件

16. `git checkout` 仓库名/分支 //查看下载的远程仓库内容

17. `git pull` 远程库名 分支名 //等于`fetch+merge`，直接合并项目
18. `git remote rename <old-name> <new-name>`要给远程仓库改名，你需要使用Git的git remote rename命令。
 
19. `git remote remove <别名>` //移除远程仓库

如果要删除或者清空分支，需要先删除或清空后提交到本地库，然后再push到远程库

19. `git reset --hard+哈希值` //恢复历史版本

20. `git ls-files` //查看本地仓内的文件

21. g`it rm --cached -r .` 命令的含义如下：

	`git rm`: 这是 Git 命令，用于从版本控制中删除文件。
	`--cached`: 这个选项告诉 Git 只删除文件的跟踪记录，但保留实际文件在工作目录中。
	`-r`: 这个选项表示递归地删除文件夹及其内容。
	`.`: 这个点表示当前目录。
	综合起来，`git rm --cached -r .` 命令的作用是将当前目录下的所有文件和文件夹从版本控制中移除，但保留它们在工作目录中的实际副本。

	这个命令通常用于不再需要跟踪的文件或文件夹，但您仍希望保留它们在您的本地环境中。一旦您执行了这个命令并提交了更改，其他协作者在拉取您的更改时将不再看到这些文件或文件夹，但您的本地副本仍然存在于工作目录中。

22. `git log` 命令时，命令末尾出现（end）只需要输入`q`即可解决

23. //解决冲突的方式
当两个不同的人修改了同一个文件的同一处，且修改不同时会出现冲突
<<<<<<< HEAD
// 你的更改
=======
// 远程仓库的更改
\>>>>>>> 2426fcf205c1ed863d83a40f4d6672b2e3a63920
在 <<<<<<< HEAD 和 ======= 之间是你本地分支的更改，在 ======= 和 >>>>>>> 之间是远程分支的更改。你需要决定要保留哪个版本或者进行修改以合并两者。
手动编辑文件，删除不需要的标记并根据需要修改内容，以解决冲突。例如，你可以选择保留本地更改，删除冲突标记后的内容，然后保存文件。

在终端中运行以下命令来标记冲突已解决：
git add Manuscript.docx
git commit -m "解决合并冲突"
git push fp master
//然而对于一些非代码或者txt类文件，只能从远程库下载并替换本地库文件，然后再次提交。
这时候git就会认为你遵从了远程库的提交

24. `git pull origin master --force`这将会强制拉取origin远程仓库的master分支并覆盖本地分支。

25. `git push origin master --force`这将会强制将本地分支的更改推送到origin远程仓库的master分支，覆盖远程分支的历史记录。



```shell

$ git help -a
See 'git help <command>' to read about a specific subcommand

Main Porcelain Commands
   add                  Add file contents to the index
   am                   Apply a series of patches from a mailbox
   archive              Create an archive of files from a named tree
   bisect               Use binary search to find the commit that introduced a bug
   branch               List, create, or delete branches
   bundle               Move objects and refs by archive
   checkout             Switch branches or restore working tree files
   cherry-pick          Apply the changes introduced by some existing commits
   citool               Graphical alternative to git-commit
   clean                Remove untracked files from the working tree
   clone                Clone a repository into a new directory
   commit               Record changes to the repository
   describe             Give an object a human readable name based on an available ref
   diff                 Show changes between commits, commit and working tree, etc
   fetch                Download objects and refs from another repository
   format-patch         Prepare patches for e-mail submission
   gc                   Cleanup unnecessary files and optimize the local reposit:...skipping...
See 'git help <command>' to read about a specific subcommand

Main Porcelain Commands
   add                  Add file contents to the index
   am                   Apply a series of patches from a mailbox
   archive              Create an archive of files from a named tree
   bisect               Use binary search to find the commit that introduced a bug
   branch               List, create, or delete branches
   bundle               Move objects and refs by archive
   checkout             Switch branches or restore working tree files
   cherry-pick          Apply the changes introduced by some existing commits
   citool               Graphical alternative to git-commit
   clean                Remove untracked files from the working tree
   clone                Clone a repository into a new directory
   commit               Record changes to the repository
   describe             Give an object a human readable name based on an available ref
   diff                 Show changes between commits, commit and working tree, etc
   fetch                Download objects and refs from another repository
   format-patch         Prepare patches for e-mail submission
   gc                   Cleanup unnecessary files and optimize the local repository
   gitk                 The Git repository browser
   grep                 Print lines matching a pattern
   gui                  A portable graphical interface to Git
   init                 Create an empty Git repository or reinitialize an existing one
   log                  Show commit logs
   merge                Join two or more development histories together
   mv                   Move or rename a file, a directory, or a symlink
   notes                Add or inspect object notes
   pull                 Fetch from and integrate with another repository or a local branch
   push                 Update remote refs along with associated objects
   range-diff           Compare two commit ranges (e.g. two versions of a branch)
   rebase               Reapply commits on top of another base tip
   reset                Reset current HEAD to the specified state
   restore              Restore working tree files
   revert               Revert some existing commits
   rm                   Remove files from the working tree and from the index
   shortlog             Summarize 'git log' output
   show                 Show various types of objects
   sparse-checkout      Initialize and modify the sparse-checkout
   stash                Stash the changes in a dirty working directory away
   status               Show the working tree status
   submodule            Initialize, update or inspect submodules
   switch               Switch branches
   tag                  Create, list, delete or verify a tag object signed with GPG
   worktree             Manage multiple working trees

Ancillary Commands / Manipulators
   config               Get and set repository or global options
   fast-export          Git data exporter
   fast-import          Backend for fast Git data importers
   filter-branch        Rewrite branches
   mergetool            Run merge conflict resolution tools to resolve merge conflicts
   pack-refs            Pack heads and tags for efficient repository access
   prune                Prune all unreachable objects from the object database
   reflog               Manage reflog information
   remote               Manage set of tracked repositories
   repack               Pack unpacked objects in a repository
   replace              Create, list, delete refs to replace objects

Ancillary Commands / Interrogators
   annotate             Annotate file lines with commit information
   blame                Show what revision and author last modified each line of a file
   bugreport            Collect information for user to file a bug report
   count-objects        Count unpacked number of objects and their disk consumption
   difftool             Show changes using common diff tools
   fsck                 Verifies the connectivity and validity of the objects in the database
   gitweb               Git web interface (web frontend to Git repositories)
   help                 Display help information about Git
   instaweb             Instantly browse your working repository in gitweb
   merge-tree           Show three-way merge without touching index
   rerere               Reuse recorded resolution of conflicted merges
   show-branch          Show branches and their commits
   verify-commit        Check the GPG signature of commits
   verify-tag           Check the GPG signature of tags
   whatchanged          Show logs with difference each commit introduces

Interacting with Others
   archimport           Import a GNU Arch repository into Git
   cvsexportcommit      Export a single commit to a CVS checkout
   cvsimport            Salvage your data out of another SCM people love to hate
   cvsserver            A CVS server emulator for Git
   imap-send            Send a collection of patches from stdin to an IMAP folder
   p4                   Import from and submit to Perforce repositories
   quiltimport          Applies a quilt patchset onto the current branch
   request-pull         Generates a summary of pending changes
   send-email           Send a collection of patches as emails
   svn                  Bidirectional operation between a Subversion repository and Git

Low-level Commands / Manipulators
   apply                Apply a patch to files and/or to the index
   checkout-index       Copy files from the index to the working tree
   commit-graph         Write and verify Git commit-graph files
   commit-tree          Create a new commit object
   hash-object          Compute object ID and optionally creates a blob from a file
   index-pack           Build pack index file for an existing packed archive
   merge-file           Run a three-way file merge
   merge-index          Run a merge for files needing merging
   mktag                Creates a tag object
   mktree               Build a tree-object from ls-tree formatted text
   multi-pack-index     Write and verify multi-pack-indexes
   pack-objects         Create a packed archive of objects
   prune-packed         Remove extra objects that are already in pack files
   read-tree            Reads tree information into the index
   symbolic-ref         Read, modify and delete symbolic refs
   unpack-objects       Unpack objects from a packed archive
   update-index         Register file contents in the working tree to the index
   update-ref           Update the object name stored in a ref safely
   write-tree           Create a tree object from the current index

Low-level Commands / Interrogators
   cat-file             Provide content or type and size information for repository objects
   cherry               Find commits yet to be applied to upstream
   diff-files           Compares files in the working tree and the index
   diff-index           Compare a tree to the working tree or index
   diff-tree            Compares the content and mode of blobs found via two tree objects
   for-each-ref         Output information on each ref
   get-tar-commit-id    Extract commit ID from an archive created using git-archive
   ls-files             Show information about files in the index and the working tree
   ls-remote            List references in a remote repository
   ls-tree              List the contents of a tree object
   merge-base           Find as good common ancestors as possible for a merge
   name-rev             Find symbolic names for given revs
   pack-redundant       Find redundant pack files
   rev-list             Lists commit objects in reverse chronological order
   rev-parse            Pick out and massage parameters
   show-index           Show packed archive index
   show-ref             List references in a local repository
   unpack-file          Creates a temporary file with a blob's contents
   var                  Show a Git logical variable
   verify-pack          Validate packed Git archive files

Low-level Commands / Syncing Repositories
   daemon               A really simple server for Git repositories
   fetch-pack           Receive missing objects from another repository
   http-backend         Server side implementation of Git over HTTP
   send-pack            Push objects over Git protocol to another repository
   update-server-info   Update auxiliary info file to help dumb servers

Low-level Commands / Internal Helpers
   check-attr           Display gitattributes information
   check-ignore         Debug gitignore / exclude files
   check-mailmap        Show canonical names and email addresses of contacts
   check-ref-format     Ensures that a reference name is well formed
   column               Display data in columns
   credential           Retrieve and store user credentials
   credential-store     Helper to store credentials on disk
   fmt-merge-msg        Produce a merge commit message
   interpret-trailers   Add or parse structured information in commit messages
   mailinfo             Extracts patch and authorship from a single e-mail message
   mailsplit            Simple UNIX mbox splitter program
   merge-one-file       The standard helper program to use with git-merge-index
   patch-id             Compute unique ID for a patch
   sh-i18n              Git's i18n setup code for shell scripts
   sh-setup             Common Git shell script setup code
   stripspace           Remove unnecessary whitespace

External commands
   askyesno
   credential-helper-selector
   cvsserver
   flow
   lfs
   shell
```


