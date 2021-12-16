import os


source_commit = "61bf2aa9449acb94fab703e87673c53885724a11"
target_branches = [
    "quard-4.3.x-1116-hotfix",
]


def main():
    curr_branch = os.popen("git rev-parse --abbrev-ref HEAD")

    for target_branch in target_branches:
        os.popen(f"git checkout -b {target_branch} origin/{target_branch}")
        os.popen(f"git pull -r upstream {target_branch}")
        os.popen(f"git cherry-pick {source_commit}")
        os.popen(f"git push")

    os.popen(f"git checkout {curr_branch}")


if __name__ == '__main__':
    main()
