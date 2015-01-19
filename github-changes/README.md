# github-changes

## Running it

To get a changelog for https://www.github.com/aexeagmbh/dockerfiles
```
docker run --rm -v `pwd`/output:/output -ti aexea/github-changes github-changes -o aexeagmbh -r dockerfiles --no-merges
-f /output/CHANGELOG.md
```

More doc on how to use the tool here: https://lalitkapoor.github.io/github-changes/
