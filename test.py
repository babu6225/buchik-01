print"welcome to git hub
Devops Tutorial for beginners 17/02/2020
diff --git a/README.md b/README.md is what Git is comparing (i.e., README.md in this example).
--- a/README.md would show anything removed from the file.
+++ b/README.md would show anything added to your file.
Anything added to the file is printed in green text with a + at the beginning of the line.
If we had removed anything, it would be printed in red text with a - sign at the beginning.
Git status now says Changes to be committed: and lists the filename (i.e., README.md) and what happened to that file (i.e., it has been modified and is ready to be committed).
Tip: If you have already run git add, and now you want to see what's different, the usual git diff won't yield anything because you already added the file. Instead, you must use git diff --cached. It will show you the difference between the current version and previous version of files that Git was told to add. Your terminal output would look like this:"
