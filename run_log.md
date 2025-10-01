2025-10-01T21:48:02.3473968Z Current runner version: '2.328.0'
2025-10-01T21:48:02.3497603Z ##[group]Runner Image Provisioner
2025-10-01T21:48:02.3498393Z Hosted Compute Agent
2025-10-01T21:48:02.3498904Z Version: 20250912.392
2025-10-01T21:48:02.3499577Z Commit: d921fda672a98b64f4f82364647e2f10b2267d0b
2025-10-01T21:48:02.3500217Z Build Date: 2025-09-12T15:23:14Z
2025-10-01T21:48:02.3500794Z ##[endgroup]
2025-10-01T21:48:02.3501349Z ##[group]Operating System
2025-10-01T21:48:02.3501963Z Ubuntu
2025-10-01T21:48:02.3502406Z 24.04.3
2025-10-01T21:48:02.3502912Z LTS
2025-10-01T21:48:02.3503397Z ##[endgroup]
2025-10-01T21:48:02.3503857Z ##[group]Runner Image
2025-10-01T21:48:02.3504456Z Image: ubuntu-24.04
2025-10-01T21:48:02.3504927Z Version: 20250922.53.1
2025-10-01T21:48:02.3505913Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20250922.53/images/ubuntu/Ubuntu2404-Readme.md
2025-10-01T21:48:02.3507820Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20250922.53
2025-10-01T21:48:02.3508795Z ##[endgroup]
2025-10-01T21:48:02.3509905Z ##[group]GITHUB_TOKEN Permissions
2025-10-01T21:48:02.3511991Z Contents: read
2025-10-01T21:48:02.3512532Z Metadata: read
2025-10-01T21:48:02.3513096Z Packages: read
2025-10-01T21:48:02.3513586Z ##[endgroup]
2025-10-01T21:48:02.3515676Z Secret source: Actions
2025-10-01T21:48:02.3517059Z Prepare workflow directory
2025-10-01T21:48:02.3855976Z Prepare all required actions
2025-10-01T21:48:02.3911267Z Getting action download info
2025-10-01T21:48:02.9222443Z Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)
2025-10-01T21:48:03.3812355Z Download action repository 'docker/setup-buildx-action@v3' (SHA:e468171a9de216ec08956ac3ada2f0791b6bd435)
2025-10-01T21:48:04.0155401Z Download action repository 'docker/login-action@v3' (SHA:5e57cd118135c172c3672efd75eb46360885c0ef)
2025-10-01T21:48:04.6627973Z Download action repository 'docker/build-push-action@v5' (SHA:ca052bb54ab0790a636c9b5f226502c73d547a25)
2025-10-01T21:48:05.2667930Z Download action repository 'anchore/sbom-action@v0' (SHA:f8bdd1d8ac5e901a77a92f111440fdb1b593736b)
2025-10-01T21:48:05.9591825Z Download action repository 'aquasecurity/trivy-action@0.24.0' (SHA:6e7b7d1fd3e4fef0c5fa8cce1229c54b2c9bd0d8)
2025-10-01T21:48:06.4152811Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2025-10-01T21:48:06.6227492Z Complete job name: container-scan
2025-10-01T21:48:06.6639641Z ##[group]Build container for action use: '/home/runner/work/_actions/aquasecurity/trivy-action/0.24.0/Dockerfile'.
2025-10-01T21:48:06.6687847Z ##[command]/usr/bin/docker build -t b2e41d:9d5bea7102e54c1cb0feb61344069cd4 -f "/home/runner/work/_actions/aquasecurity/trivy-action/0.24.0/Dockerfile" "/home/runner/work/_actions/aquasecurity/trivy-action/0.24.0"
2025-10-01T21:48:09.3340051Z #0 building with "default" instance using docker driver
2025-10-01T21:48:09.3340613Z 
2025-10-01T21:48:09.3340822Z #1 [internal] load build definition from Dockerfile
2025-10-01T21:48:09.3341345Z #1 transferring dockerfile: 194B done
2025-10-01T21:48:09.3341732Z #1 DONE 0.0s
2025-10-01T21:48:09.3341909Z 
2025-10-01T21:48:09.3342140Z #2 [internal] load metadata for ghcr.io/aquasecurity/trivy:0.53.0
2025-10-01T21:48:10.3042461Z #2 DONE 1.1s
2025-10-01T21:48:10.4244795Z 
2025-10-01T21:48:10.4245036Z #3 [internal] load .dockerignore
2025-10-01T21:48:10.4245516Z #3 transferring context: 2B done
2025-10-01T21:48:10.4245890Z #3 DONE 0.0s
2025-10-01T21:48:10.4246613Z 
2025-10-01T21:48:10.4246772Z #4 [internal] load build context
2025-10-01T21:48:10.4248389Z #4 transferring context: 5.71kB done
2025-10-01T21:48:10.4248958Z #4 DONE 0.0s
2025-10-01T21:48:10.4249168Z 
2025-10-01T21:48:10.4249876Z #5 [1/4] FROM ghcr.io/aquasecurity/trivy:0.53.0@sha256:53e6715d5c67e80e629f0dfa3bd6ed2bc74bdcaa4bdbe934a5a1811a249db6b9
2025-10-01T21:48:10.4251190Z #5 resolve ghcr.io/aquasecurity/trivy:0.53.0@sha256:53e6715d5c67e80e629f0dfa3bd6ed2bc74bdcaa4bdbe934a5a1811a249db6b9 done
2025-10-01T21:48:10.4252638Z #5 sha256:8082d8d128f3e39d28a7df824e43c655d764ca76a19b096968b5c3a1906f14a0 1.16kB / 1.16kB done
2025-10-01T21:48:10.4253560Z #5 sha256:00698f09a9fdaa2b495079eb2d56e73c67f988eedaa888269303f03cf6a0d8f0 1.98kB / 1.98kB done
2025-10-01T21:48:10.4254317Z #5 sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b883634f 0B / 3.62MB 0.1s
2025-10-01T21:48:10.4255041Z #5 sha256:037a6c10ef0d4338f603f72108344ad8298876f20af8a80f9b57efe70327293b 0B / 6.15MB 0.1s
2025-10-01T21:48:10.4255742Z #5 sha256:03a75a75154a30e4e14bcc8aa0680ce816ed3492cabfbdddfcead8b36cf807f2 0B / 38.15MB 0.1s
2025-10-01T21:48:10.4256696Z #5 sha256:53e6715d5c67e80e629f0dfa3bd6ed2bc74bdcaa4bdbe934a5a1811a249db6b9 1.36kB / 1.36kB done
2025-10-01T21:48:10.5488554Z #5 sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b883634f 1.05MB / 3.62MB 0.2s
2025-10-01T21:48:10.5489866Z #5 sha256:03a75a75154a30e4e14bcc8aa0680ce816ed3492cabfbdddfcead8b36cf807f2 7.34MB / 38.15MB 0.2s
2025-10-01T21:48:10.5490826Z #5 extracting sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b883634f
2025-10-01T21:48:10.6761138Z #5 sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b883634f 3.62MB / 3.62MB 0.2s done
2025-10-01T21:48:10.6762418Z #5 sha256:037a6c10ef0d4338f603f72108344ad8298876f20af8a80f9b57efe70327293b 2.10MB / 6.15MB 0.3s
2025-10-01T21:48:10.6765449Z #5 sha256:03a75a75154a30e4e14bcc8aa0680ce816ed3492cabfbdddfcead8b36cf807f2 38.15MB / 38.15MB 0.3s
2025-10-01T21:48:10.6769873Z #5 extracting sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b883634f 0.1s done
2025-10-01T21:48:10.6771763Z #5 sha256:c1cc37e8c713b93158c39141166a340d11b7d42ed2c0019cee0b9d994fee75eb 0B / 4.37kB 0.3s
2025-10-01T21:48:10.6772782Z #5 extracting sha256:037a6c10ef0d4338f603f72108344ad8298876f20af8a80f9b57efe70327293b
2025-10-01T21:48:10.7774454Z #5 sha256:037a6c10ef0d4338f603f72108344ad8298876f20af8a80f9b57efe70327293b 6.15MB / 6.15MB 0.3s done
2025-10-01T21:48:10.7775606Z #5 sha256:03a75a75154a30e4e14bcc8aa0680ce816ed3492cabfbdddfcead8b36cf807f2 38.15MB / 38.15MB 0.3s done
2025-10-01T21:48:10.7776955Z #5 sha256:c1cc37e8c713b93158c39141166a340d11b7d42ed2c0019cee0b9d994fee75eb 4.37kB / 4.37kB 0.3s done
2025-10-01T21:48:10.9507048Z #5 extracting sha256:037a6c10ef0d4338f603f72108344ad8298876f20af8a80f9b57efe70327293b 0.1s done
2025-10-01T21:48:11.2688560Z #5 extracting sha256:03a75a75154a30e4e14bcc8aa0680ce816ed3492cabfbdddfcead8b36cf807f2
2025-10-01T21:48:11.8067538Z #5 extracting sha256:03a75a75154a30e4e14bcc8aa0680ce816ed3492cabfbdddfcead8b36cf807f2 0.5s done
2025-10-01T21:48:11.8068786Z #5 extracting sha256:c1cc37e8c713b93158c39141166a340d11b7d42ed2c0019cee0b9d994fee75eb done
2025-10-01T21:48:11.8069463Z #5 DONE 1.5s
2025-10-01T21:48:11.9680827Z 
2025-10-01T21:48:11.9681275Z #6 [2/4] COPY entrypoint.sh /
2025-10-01T21:48:11.9681777Z #6 DONE 0.0s
2025-10-01T21:48:11.9681963Z 
2025-10-01T21:48:11.9682190Z #7 [3/4] RUN apk --no-cache add bash curl npm
2025-10-01T21:48:11.9717167Z #7 0.155 fetch https://dl-cdn.alpinelinux.org/alpine/v3.20/main/x86_64/APKINDEX.tar.gz
2025-10-01T21:48:12.1161935Z #7 0.299 fetch https://dl-cdn.alpinelinux.org/alpine/v3.20/community/x86_64/APKINDEX.tar.gz
2025-10-01T21:48:12.3647728Z #7 0.548 (1/14) Installing ncurses-terminfo-base (6.4_p20240420-r2)
2025-10-01T21:48:12.4925104Z #7 0.565 (2/14) Installing libncursesw (6.4_p20240420-r2)
2025-10-01T21:48:12.4925651Z #7 0.594 (3/14) Installing readline (8.2.10-r0)
2025-10-01T21:48:12.4926093Z #7 0.616 (4/14) Installing bash (5.2.26-r0)
2025-10-01T21:48:12.4926646Z #7 0.644 Executing bash-5.2.26-r0.post-install
2025-10-01T21:48:12.4927130Z #7 0.647 (5/14) Upgrading libcurl (8.8.0-r0 -> 8.12.1-r0)
2025-10-01T21:48:12.4927517Z #7 0.676 (6/14) Installing curl (8.12.1-r0)
2025-10-01T21:48:12.6215179Z #7 0.694 (7/14) Installing libgcc (13.2.1_git20240309-r1)
2025-10-01T21:48:12.6216053Z #7 0.708 (8/14) Installing libstdc++ (13.2.1_git20240309-r1)
2025-10-01T21:48:12.6218563Z #7 0.737 (9/14) Installing ada-libs (2.7.8-r0)
2025-10-01T21:48:12.6219057Z #7 0.768 (10/14) Installing icu-data-en (74.2-r1)
2025-10-01T21:48:12.6220039Z #7 0.805 Executing icu-data-en-74.2-r1.post-install
2025-10-01T21:48:12.8392926Z #7 0.807 *
2025-10-01T21:48:12.8393707Z #7 0.807 * If you need ICU with non-English locales and legacy charset support, install
2025-10-01T21:48:12.8394625Z #7 0.807 * package icu-data-full.
2025-10-01T21:48:12.8395092Z #7 0.807 *
2025-10-01T21:48:12.8395503Z #7 0.808 (11/14) Installing icu-libs (74.2-r1)
2025-10-01T21:48:12.8396109Z #7 0.857 (12/14) Installing libuv (1.48.0-r0)
2025-10-01T21:48:12.8396867Z #7 0.872 (13/14) Installing nodejs-current (21.7.3-r0)
2025-10-01T21:48:13.0105605Z #7 1.194 (14/14) Installing npm (10.9.1-r0)
2025-10-01T21:48:13.2503593Z #7 1.433 Executing busybox-1.36.1-r28.trigger
2025-10-01T21:48:13.4058739Z #7 1.442 OK: 94 MiB in 40 packages
2025-10-01T21:48:13.4059209Z #7 DONE 1.6s
2025-10-01T21:48:13.5209628Z 
2025-10-01T21:48:13.5210092Z #8 [4/4] RUN chmod +x /entrypoint.sh
2025-10-01T21:48:13.5210541Z #8 DONE 0.1s
2025-10-01T21:48:13.6731143Z 
2025-10-01T21:48:13.6731520Z #9 exporting to image
2025-10-01T21:48:14.0114031Z #9 exporting layers
2025-10-01T21:48:14.0114434Z #9 exporting layers 0.5s done
2025-10-01T21:48:14.0297730Z #9 writing image sha256:b9b4ce7e20433fe05a35ce14870cf909e522f9a195187e0583df96e41b384438 done
2025-10-01T21:48:14.0298679Z #9 naming to docker.io/library/b2e41d:9d5bea7102e54c1cb0feb61344069cd4 done
2025-10-01T21:48:14.0299333Z #9 DONE 0.5s
2025-10-01T21:48:14.0365563Z ##[endgroup]
2025-10-01T21:48:14.0617942Z ##[group]Run actions/checkout@v4
2025-10-01T21:48:14.0618463Z with:
2025-10-01T21:48:14.0618653Z   repository: Baragji/N_grade
2025-10-01T21:48:14.0619011Z   token: ***
2025-10-01T21:48:14.0619192Z   ssh-strict: true
2025-10-01T21:48:14.0619368Z   ssh-user: git
2025-10-01T21:48:14.0619559Z   persist-credentials: true
2025-10-01T21:48:14.0619763Z   clean: true
2025-10-01T21:48:14.0619963Z   sparse-checkout-cone-mode: true
2025-10-01T21:48:14.0620180Z   fetch-depth: 1
2025-10-01T21:48:14.0620354Z   fetch-tags: false
2025-10-01T21:48:14.0620545Z   show-progress: true
2025-10-01T21:48:14.0620730Z   lfs: false
2025-10-01T21:48:14.0620885Z   submodules: false
2025-10-01T21:48:14.0621067Z   set-safe-directory: true
2025-10-01T21:48:14.0621458Z ##[endgroup]
2025-10-01T21:48:14.1675794Z Syncing repository: Baragji/N_grade
2025-10-01T21:48:14.1677416Z ##[group]Getting Git version info
2025-10-01T21:48:14.1677778Z Working directory is '/home/runner/work/N_grade/N_grade'
2025-10-01T21:48:14.1678357Z [command]/usr/bin/git version
2025-10-01T21:48:14.1703465Z git version 2.51.0
2025-10-01T21:48:14.1729205Z ##[endgroup]
2025-10-01T21:48:14.1744103Z Temporarily overriding HOME='/home/runner/work/_temp/6e3831f0-90fc-4110-94d9-8314bc5e4612' before making global git config changes
2025-10-01T21:48:14.1749954Z Adding repository directory to the temporary git global config as a safe directory
2025-10-01T21:48:14.1751017Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/N_grade/N_grade
2025-10-01T21:48:14.1785859Z Deleting the contents of '/home/runner/work/N_grade/N_grade'
2025-10-01T21:48:14.1789824Z ##[group]Initializing the repository
2025-10-01T21:48:14.1793979Z [command]/usr/bin/git init /home/runner/work/N_grade/N_grade
2025-10-01T21:48:14.1902815Z hint: Using 'master' as the name for the initial branch. This default branch name
2025-10-01T21:48:14.1903430Z hint: is subject to change. To configure the initial branch name to use in all
2025-10-01T21:48:14.1904028Z hint: of your new repositories, which will suppress this warning, call:
2025-10-01T21:48:14.1904447Z hint:
2025-10-01T21:48:14.1904793Z hint: 	git config --global init.defaultBranch <name>
2025-10-01T21:48:14.1905153Z hint:
2025-10-01T21:48:14.1905491Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2025-10-01T21:48:14.1906044Z hint: 'development'. The just-created branch can be renamed via this command:
2025-10-01T21:48:14.1906685Z hint:
2025-10-01T21:48:14.1906964Z hint: 	git branch -m <name>
2025-10-01T21:48:14.1907267Z hint:
2025-10-01T21:48:14.1908122Z hint: Disable this message with "git config set advice.defaultBranchName false"
2025-10-01T21:48:14.1908841Z Initialized empty Git repository in /home/runner/work/N_grade/N_grade/.git/
2025-10-01T21:48:14.1918372Z [command]/usr/bin/git remote add origin https://github.com/Baragji/N_grade
2025-10-01T21:48:14.1949200Z ##[endgroup]
2025-10-01T21:48:14.1949591Z ##[group]Disabling automatic garbage collection
2025-10-01T21:48:14.1953389Z [command]/usr/bin/git config --local gc.auto 0
2025-10-01T21:48:14.1980422Z ##[endgroup]
2025-10-01T21:48:14.1981033Z ##[group]Setting up auth
2025-10-01T21:48:14.1988081Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2025-10-01T21:48:14.2017619Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2025-10-01T21:48:14.2346738Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2025-10-01T21:48:14.2375039Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2025-10-01T21:48:14.2590901Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2025-10-01T21:48:14.2624121Z ##[endgroup]
2025-10-01T21:48:14.2625109Z ##[group]Fetching the repository
2025-10-01T21:48:14.2633465Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +a1cf2d4c3b413f8978b506689c21ced0203514d7:refs/remotes/pull/1/merge
2025-10-01T21:48:14.7028325Z From https://github.com/Baragji/N_grade
2025-10-01T21:48:14.7028959Z  * [new ref]         a1cf2d4c3b413f8978b506689c21ced0203514d7 -> pull/1/merge
2025-10-01T21:48:14.7059594Z ##[endgroup]
2025-10-01T21:48:14.7060179Z ##[group]Determining the checkout info
2025-10-01T21:48:14.7062992Z ##[endgroup]
2025-10-01T21:48:14.7068402Z [command]/usr/bin/git sparse-checkout disable
2025-10-01T21:48:14.7149633Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2025-10-01T21:48:14.7176222Z ##[group]Checking out the ref
2025-10-01T21:48:14.7180535Z [command]/usr/bin/git checkout --progress --force refs/remotes/pull/1/merge
2025-10-01T21:48:14.7330130Z Note: switching to 'refs/remotes/pull/1/merge'.
2025-10-01T21:48:14.7330540Z 
2025-10-01T21:48:14.7330853Z You are in 'detached HEAD' state. You can look around, make experimental
2025-10-01T21:48:14.7331618Z changes and commit them, and you can discard any commits you make in this
2025-10-01T21:48:14.7332353Z state without impacting any branches by switching back to a branch.
2025-10-01T21:48:14.7332794Z 
2025-10-01T21:48:14.7333070Z If you want to create a new branch to retain commits you create, you may
2025-10-01T21:48:14.7333722Z do so (now or later) by using -c with the switch command. Example:
2025-10-01T21:48:14.7334184Z 
2025-10-01T21:48:14.7334335Z   git switch -c <new-branch-name>
2025-10-01T21:48:14.7334599Z 
2025-10-01T21:48:14.7334753Z Or undo this operation with:
2025-10-01T21:48:14.7335020Z 
2025-10-01T21:48:14.7335143Z   git switch -
2025-10-01T21:48:14.7335345Z 
2025-10-01T21:48:14.7335580Z Turn off this advice by setting config variable advice.detachedHead to false
2025-10-01T21:48:14.7335860Z 
2025-10-01T21:48:14.7336185Z HEAD is now at a1cf2d4 Merge fb17e559f4dea83f6df3554b81f1bc9924b28bbc into aea3734e03e8f13503fb9259cb96ccdf179fe23b
2025-10-01T21:48:14.7339020Z ##[endgroup]
2025-10-01T21:48:14.7371348Z [command]/usr/bin/git log -1 --format=%H
2025-10-01T21:48:14.7391767Z a1cf2d4c3b413f8978b506689c21ced0203514d7
2025-10-01T21:48:14.7574483Z ##[group]Run docker/setup-buildx-action@v3
2025-10-01T21:48:14.7574745Z with:
2025-10-01T21:48:14.7574923Z   driver: docker-container
2025-10-01T21:48:14.7575116Z   install: false
2025-10-01T21:48:14.7575282Z   use: true
2025-10-01T21:48:14.7575439Z   keep-state: false
2025-10-01T21:48:14.7575796Z   cache-binary: true
2025-10-01T21:48:14.7575971Z   cleanup: true
2025-10-01T21:48:14.7576135Z ##[endgroup]
2025-10-01T21:48:15.0570805Z ##[group]Docker info
2025-10-01T21:48:15.0597891Z [command]/usr/bin/docker version
2025-10-01T21:48:15.0804416Z Client: Docker Engine - Community
2025-10-01T21:48:15.0804876Z  Version:           28.0.4
2025-10-01T21:48:15.0805241Z  API version:       1.48
2025-10-01T21:48:15.0805588Z  Go version:        go1.23.7
2025-10-01T21:48:15.0805943Z  Git commit:        b8034c0
2025-10-01T21:48:15.0806634Z  Built:             Tue Mar 25 15:07:16 2025
2025-10-01T21:48:15.0807050Z  OS/Arch:           linux/amd64
2025-10-01T21:48:15.0807482Z  Context:           default
2025-10-01T21:48:15.0807700Z 
2025-10-01T21:48:15.0807844Z Server: Docker Engine - Community
2025-10-01T21:48:15.0808208Z  Engine:
2025-10-01T21:48:15.0808435Z   Version:          28.0.4
2025-10-01T21:48:15.0808679Z   API version:      1.48 (minimum version 1.24)
2025-10-01T21:48:15.0808957Z   Go version:       go1.23.7
2025-10-01T21:48:15.0809169Z   Git commit:       6430e49
2025-10-01T21:48:15.0809387Z   Built:            Tue Mar 25 15:07:16 2025
2025-10-01T21:48:15.0809635Z   OS/Arch:          linux/amd64
2025-10-01T21:48:15.0809846Z   Experimental:     false
2025-10-01T21:48:15.0810037Z  containerd:
2025-10-01T21:48:15.0810204Z   Version:          1.7.27
2025-10-01T21:48:15.0810446Z   GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
2025-10-01T21:48:15.0810719Z  runc:
2025-10-01T21:48:15.0810871Z   Version:          1.2.5
2025-10-01T21:48:15.0811072Z   GitCommit:        v1.2.5-0-g59923ef
2025-10-01T21:48:15.0811332Z  docker-init:
2025-10-01T21:48:15.0811497Z   Version:          0.19.0
2025-10-01T21:48:15.0811703Z   GitCommit:        de40ad0
2025-10-01T21:48:15.0855307Z [command]/usr/bin/docker info
2025-10-01T21:48:17.1401669Z Client: Docker Engine - Community
2025-10-01T21:48:17.1402215Z  Version:    28.0.4
2025-10-01T21:48:17.1403602Z  Context:    default
2025-10-01T21:48:17.1403946Z  Debug Mode: false
2025-10-01T21:48:17.1404226Z  Plugins:
2025-10-01T21:48:17.1404503Z   buildx: Docker Buildx (Docker Inc.)
2025-10-01T21:48:17.1404879Z     Version:  v0.28.0
2025-10-01T21:48:17.1405263Z     Path:     /usr/libexec/docker/cli-plugins/docker-buildx
2025-10-01T21:48:17.1405751Z   compose: Docker Compose (Docker Inc.)
2025-10-01T21:48:17.1406437Z     Version:  v2.38.2
2025-10-01T21:48:17.1406860Z     Path:     /usr/libexec/docker/cli-plugins/docker-compose
2025-10-01T21:48:17.1407207Z 
2025-10-01T21:48:17.1407402Z Server:
2025-10-01T21:48:17.1407710Z  Containers: 0
2025-10-01T21:48:17.1408001Z   Running: 0
2025-10-01T21:48:17.1408372Z   Paused: 0
2025-10-01T21:48:17.1408896Z   Stopped: 0
2025-10-01T21:48:17.1409235Z  Images: 1
2025-10-01T21:48:17.1409518Z  Server Version: 28.0.4
2025-10-01T21:48:17.1409861Z  Storage Driver: overlay2
2025-10-01T21:48:17.1410217Z   Backing Filesystem: extfs
2025-10-01T21:48:17.1410575Z   Supports d_type: true
2025-10-01T21:48:17.1410907Z   Using metacopy: false
2025-10-01T21:48:17.1411265Z   Native Overlay Diff: false
2025-10-01T21:48:17.1411626Z   userxattr: false
2025-10-01T21:48:17.1411933Z  Logging Driver: json-file
2025-10-01T21:48:17.1412158Z  Cgroup Driver: systemd
2025-10-01T21:48:17.1412353Z  Cgroup Version: 2
2025-10-01T21:48:17.1412530Z  Plugins:
2025-10-01T21:48:17.1412689Z   Volume: local
2025-10-01T21:48:17.1412920Z   Network: bridge host ipvlan macvlan null overlay
2025-10-01T21:48:17.1413278Z   Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
2025-10-01T21:48:17.1413602Z  Swarm: inactive
2025-10-01T21:48:17.1413794Z  Runtimes: io.containerd.runc.v2 runc
2025-10-01T21:48:17.1414028Z  Default Runtime: runc
2025-10-01T21:48:17.1414544Z  Init Binary: docker-init
2025-10-01T21:48:17.1414814Z  containerd version: 05044ec0a9a75232cad458027ca83437aae3f4da
2025-10-01T21:48:17.1415108Z  runc version: v1.2.5-0-g59923ef
2025-10-01T21:48:17.1415321Z  init version: de40ad0
2025-10-01T21:48:17.1415506Z  Security Options:
2025-10-01T21:48:17.1415842Z   apparmor
2025-10-01T21:48:17.1415996Z   seccomp
2025-10-01T21:48:17.1416145Z    Profile: builtin
2025-10-01T21:48:17.1416818Z   cgroupns
2025-10-01T21:48:17.1417105Z  Kernel Version: 6.11.0-1018-azure
2025-10-01T21:48:17.1417357Z  Operating System: Ubuntu 24.04.3 LTS
2025-10-01T21:48:17.1417587Z  OSType: linux
2025-10-01T21:48:17.1417837Z  Architecture: x86_64
2025-10-01T21:48:17.1418038Z  CPUs: 4
2025-10-01T21:48:17.1418194Z  Total Memory: 15.62GiB
2025-10-01T21:48:17.1418382Z  Name: runnervm3ublj
2025-10-01T21:48:17.1418578Z  ID: fc682960-a2cc-4975-884a-ddab89401ab0
2025-10-01T21:48:17.1418825Z  Docker Root Dir: /var/lib/docker
2025-10-01T21:48:17.1419035Z  Debug Mode: false
2025-10-01T21:48:17.1419224Z  Username: githubactions
2025-10-01T21:48:17.1419416Z  Experimental: false
2025-10-01T21:48:17.1419600Z  Insecure Registries:
2025-10-01T21:48:17.1423507Z   ::1/128
2025-10-01T21:48:17.1423700Z   127.0.0.0/8
2025-10-01T21:48:17.1423895Z  Live Restore Enabled: false
2025-10-01T21:48:17.1424058Z 
2025-10-01T21:48:17.1424407Z ##[endgroup]
2025-10-01T21:48:17.2092678Z ##[group]Buildx version
2025-10-01T21:48:17.2120567Z [command]/usr/bin/docker buildx version
2025-10-01T21:48:17.2593248Z github.com/docker/buildx v0.28.0 b1281b81bba797b21d9eaf256e6a13eb14419836
2025-10-01T21:48:17.2625267Z ##[endgroup]
2025-10-01T21:48:17.2824309Z ##[group]Inspecting default docker context
2025-10-01T21:48:17.2958443Z [
2025-10-01T21:48:17.2958722Z   {
2025-10-01T21:48:17.2958979Z     "Name": "default",
2025-10-01T21:48:17.2959298Z     "Metadata": {},
2025-10-01T21:48:17.2959555Z     "Endpoints": {
2025-10-01T21:48:17.2959739Z       "docker": {
2025-10-01T21:48:17.2959951Z         "Host": "unix:///var/run/docker.sock",
2025-10-01T21:48:17.2960243Z         "SkipTLSVerify": false
2025-10-01T21:48:17.2960449Z       }
2025-10-01T21:48:17.2960689Z     },
2025-10-01T21:48:17.2960849Z     "TLSMaterial": {},
2025-10-01T21:48:17.2961026Z     "Storage": {
2025-10-01T21:48:17.2961214Z       "MetadataPath": "<IN MEMORY>",
2025-10-01T21:48:17.2961554Z       "TLSPath": "<IN MEMORY>"
2025-10-01T21:48:17.2961798Z     }
2025-10-01T21:48:17.2961942Z   }
2025-10-01T21:48:17.2962075Z ]
2025-10-01T21:48:17.2962422Z ##[endgroup]
2025-10-01T21:48:17.2962750Z ##[group]Creating a new builder instance
2025-10-01T21:48:17.4132413Z [command]/usr/bin/docker buildx create --name builder-54d1668b-0a40-40ea-89c4-8b5572363844 --driver docker-container --buildkitd-flags --allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host --use
2025-10-01T21:48:17.4725957Z builder-54d1668b-0a40-40ea-89c4-8b5572363844
2025-10-01T21:48:17.4760044Z ##[endgroup]
2025-10-01T21:48:17.4760454Z ##[group]Booting builder
2025-10-01T21:48:17.4791401Z [command]/usr/bin/docker buildx inspect --bootstrap --builder builder-54d1668b-0a40-40ea-89c4-8b5572363844
2025-10-01T21:48:17.5287089Z #1 [internal] booting buildkit
2025-10-01T21:48:17.6790157Z #1 pulling image moby/buildkit:buildx-stable-1
2025-10-01T21:48:22.2275651Z #1 pulling image moby/buildkit:buildx-stable-1 4.7s done
2025-10-01T21:48:22.3788239Z #1 creating container buildx_buildkit_builder-54d1668b-0a40-40ea-89c4-8b55723638440
2025-10-01T21:48:22.5877816Z #1 creating container buildx_buildkit_builder-54d1668b-0a40-40ea-89c4-8b55723638440 0.4s done
2025-10-01T21:48:22.5890661Z #1 DONE 5.1s
2025-10-01T21:48:22.6182844Z Name:          builder-54d1668b-0a40-40ea-89c4-8b5572363844
2025-10-01T21:48:22.6183392Z Driver:        docker-container
2025-10-01T21:48:22.6183738Z Last Activity: 2025-10-01 21:48:17 +0000 UTC
2025-10-01T21:48:22.6184035Z 
2025-10-01T21:48:22.6184144Z Nodes:
2025-10-01T21:48:22.6184508Z Name:                  builder-54d1668b-0a40-40ea-89c4-8b55723638440
2025-10-01T21:48:22.6185390Z Endpoint:              unix:///var/run/docker.sock
2025-10-01T21:48:22.6185805Z Status:                running
2025-10-01T21:48:22.6186563Z BuildKit daemon flags: --allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host
2025-10-01T21:48:22.6187067Z BuildKit version:      v0.24.0
2025-10-01T21:48:22.6187579Z Platforms:             linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386
2025-10-01T21:48:22.6187890Z Labels:
2025-10-01T21:48:22.6188123Z  org.mobyproject.buildkit.worker.executor:         oci
2025-10-01T21:48:22.6188508Z  org.mobyproject.buildkit.worker.hostname:         7fbcd70e05d4
2025-10-01T21:48:22.6188877Z  org.mobyproject.buildkit.worker.network:          host
2025-10-01T21:48:22.6189234Z  org.mobyproject.buildkit.worker.oci.process-mode: sandbox
2025-10-01T21:48:22.6189613Z  org.mobyproject.buildkit.worker.selinux.enabled:  false
2025-10-01T21:48:22.6189979Z  org.mobyproject.buildkit.worker.snapshotter:      overlayfs
2025-10-01T21:48:22.6190275Z GC Policy rule#0:
2025-10-01T21:48:22.6190462Z  All:            false
2025-10-01T21:48:22.6190769Z  Filters:        type==source.local,type==exec.cachemount,type==source.git.checkout
2025-10-01T21:48:22.6191122Z  Keep Duration:  48h0m0s
2025-10-01T21:48:22.6191313Z  Max Used Space: 488.3MiB
2025-10-01T21:48:22.6191516Z GC Policy rule#1:
2025-10-01T21:48:22.6191682Z  All:            false
2025-10-01T21:48:22.6191865Z  Keep Duration:  1440h0m0s
2025-10-01T21:48:22.6192055Z  Reserved Space: 7.451GiB
2025-10-01T21:48:22.6192476Z  Max Used Space: 54.02GiB
2025-10-01T21:48:22.6192672Z  Min Free Space: 13.97GiB
2025-10-01T21:48:22.6192850Z GC Policy rule#2:
2025-10-01T21:48:22.6193015Z  All:            false
2025-10-01T21:48:22.6193187Z  Reserved Space: 7.451GiB
2025-10-01T21:48:22.6193377Z  Max Used Space: 54.02GiB
2025-10-01T21:48:22.6193557Z  Min Free Space: 13.97GiB
2025-10-01T21:48:22.6193739Z GC Policy rule#3:
2025-10-01T21:48:22.6193899Z  All:            true
2025-10-01T21:48:22.6194077Z  Reserved Space: 7.451GiB
2025-10-01T21:48:22.6194263Z  Max Used Space: 54.02GiB
2025-10-01T21:48:22.6194455Z  Min Free Space: 13.97GiB
2025-10-01T21:48:22.6230720Z ##[endgroup]
2025-10-01T21:48:22.7194112Z ##[group]Inspect builder
2025-10-01T21:48:22.7196890Z {
2025-10-01T21:48:22.7197179Z   "nodes": [
2025-10-01T21:48:22.7197501Z     {
2025-10-01T21:48:22.7197877Z       "name": "builder-54d1668b-0a40-40ea-89c4-8b55723638440",
2025-10-01T21:48:22.7198465Z       "endpoint": "unix:///var/run/docker.sock",
2025-10-01T21:48:22.7198942Z       "status": "running",
2025-10-01T21:48:22.7199797Z       "buildkitd-flags": "--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host",
2025-10-01T21:48:22.7200703Z       "buildkit": "v0.24.0",
2025-10-01T21:48:22.7201238Z       "platforms": "linux/amd64,linux/amd64/v2,linux/amd64/v3,linux/386",
2025-10-01T21:48:22.7201846Z       "features": {
2025-10-01T21:48:22.7202355Z         "Automatically load images to the Docker Engine image store": true,
2025-10-01T21:48:22.7202984Z         "Cache export": true,
2025-10-01T21:48:22.7203363Z         "Direct push": true,
2025-10-01T21:48:22.7203758Z         "Docker exporter": true,
2025-10-01T21:48:22.7204198Z         "Multi-platform build": true,
2025-10-01T21:48:22.7204618Z         "OCI exporter": true
2025-10-01T21:48:22.7204982Z       },
2025-10-01T21:48:22.7205259Z       "labels": {
2025-10-01T21:48:22.7205679Z         "org.mobyproject.buildkit.worker.executor": "oci",
2025-10-01T21:48:22.7206524Z         "org.mobyproject.buildkit.worker.hostname": "7fbcd70e05d4",
2025-10-01T21:48:22.7207116Z         "org.mobyproject.buildkit.worker.network": "host",
2025-10-01T21:48:22.7207708Z         "org.mobyproject.buildkit.worker.oci.process-mode": "sandbox",
2025-10-01T21:48:22.7208343Z         "org.mobyproject.buildkit.worker.selinux.enabled": "false",
2025-10-01T21:48:22.7208947Z         "org.mobyproject.buildkit.worker.snapshotter": "overlayfs"
2025-10-01T21:48:22.7209426Z       },
2025-10-01T21:48:22.7209685Z       "gcPolicy": [
2025-10-01T21:48:22.7210253Z         {
2025-10-01T21:48:22.7210523Z           "all": false,
2025-10-01T21:48:22.7210819Z           "filter": [
2025-10-01T21:48:22.7211099Z             "type==source.local",
2025-10-01T21:48:22.7211438Z             "type==exec.cachemount",
2025-10-01T21:48:22.7211795Z             "type==source.git.checkout"
2025-10-01T21:48:22.7212374Z           ],
2025-10-01T21:48:22.7212655Z           "keepDuration": "48h0m0s",
2025-10-01T21:48:22.7213024Z           "maxUsedSpace": "488.3MiB"
2025-10-01T21:48:22.7213367Z         },
2025-10-01T21:48:22.7213614Z         {
2025-10-01T21:48:22.7213850Z           "all": false,
2025-10-01T21:48:22.7214166Z           "keepDuration": "1440h0m0s",
2025-10-01T21:48:22.7214553Z           "reservedSpace": "7.451GiB",
2025-10-01T21:48:22.7214947Z           "maxUsedSpace": "54.02GiB",
2025-10-01T21:48:22.7215323Z           "minFreeSpace": "13.97GiB"
2025-10-01T21:48:22.7215675Z         },
2025-10-01T21:48:22.7215915Z         {
2025-10-01T21:48:22.7216171Z           "all": false,
2025-10-01T21:48:22.7216675Z           "reservedSpace": "7.451GiB",
2025-10-01T21:48:22.7217059Z           "maxUsedSpace": "54.02GiB",
2025-10-01T21:48:22.7217443Z           "minFreeSpace": "13.97GiB"
2025-10-01T21:48:22.7217786Z         },
2025-10-01T21:48:22.7218030Z         {
2025-10-01T21:48:22.7218282Z           "all": true,
2025-10-01T21:48:22.7218591Z           "reservedSpace": "7.451GiB",
2025-10-01T21:48:22.7218972Z           "maxUsedSpace": "54.02GiB",
2025-10-01T21:48:22.7219352Z           "minFreeSpace": "13.97GiB"
2025-10-01T21:48:22.7219701Z         }
2025-10-01T21:48:22.7219941Z       ]
2025-10-01T21:48:22.7220176Z     }
2025-10-01T21:48:22.7220408Z   ],
2025-10-01T21:48:22.7220739Z   "name": "builder-54d1668b-0a40-40ea-89c4-8b5572363844",
2025-10-01T21:48:22.7221200Z   "driver": "docker-container",
2025-10-01T21:48:22.7221587Z   "lastActivity": "2025-10-01T21:48:17.000Z"
2025-10-01T21:48:22.7221963Z }
2025-10-01T21:48:22.7223476Z ##[endgroup]
2025-10-01T21:48:22.7224015Z ##[group]BuildKit version
2025-10-01T21:48:22.7224434Z builder-54d1668b-0a40-40ea-89c4-8b55723638440: v0.24.0
2025-10-01T21:48:22.7225101Z ##[endgroup]
2025-10-01T21:48:22.7380547Z ##[group]Run docker/login-action@v3
2025-10-01T21:48:22.7380847Z with:
2025-10-01T21:48:22.7381014Z   registry: ghcr.io
2025-10-01T21:48:22.7381225Z   username: Baragji
2025-10-01T21:48:22.7381699Z   password: ***
2025-10-01T21:48:22.7381881Z   logout: true
2025-10-01T21:48:22.7382056Z ##[endgroup]
2025-10-01T21:48:23.0271656Z Logging into ghcr.io...
2025-10-01T21:48:23.3949634Z Login Succeeded!
2025-10-01T21:48:23.4084318Z ##[group]Run docker/build-push-action@v5
2025-10-01T21:48:23.4084582Z with:
2025-10-01T21:48:23.4084742Z   context: .
2025-10-01T21:48:23.4084921Z   file: docker/Dockerfile
2025-10-01T21:48:23.4085108Z   push: false
2025-10-01T21:48:23.4085274Z   load: true
2025-10-01T21:48:23.4085446Z   tags: ghcr.io/example/phase0:latest
2025-10-01T21:48:23.4085682Z   no-cache: false
2025-10-01T21:48:23.4085847Z   pull: false
2025-10-01T21:48:23.4086130Z   github-token: ***
2025-10-01T21:48:23.4086767Z ##[endgroup]
2025-10-01T21:48:23.6292236Z ##[group]GitHub Actions runtime token ACs
2025-10-01T21:48:23.6302826Z refs/pull/1/merge: read/write
2025-10-01T21:48:23.6303323Z refs/heads/main: read
2025-10-01T21:48:23.6304195Z ##[endgroup]
2025-10-01T21:48:23.6304779Z ##[group]Docker info
2025-10-01T21:48:23.6343431Z [command]/usr/bin/docker version
2025-10-01T21:48:23.6521918Z Client: Docker Engine - Community
2025-10-01T21:48:23.6524683Z  Version:           28.0.4
2025-10-01T21:48:23.6525115Z  API version:       1.48
2025-10-01T21:48:23.6525484Z  Go version:        go1.23.7
2025-10-01T21:48:23.6525829Z  Git commit:        b8034c0
2025-10-01T21:48:23.6526176Z  Built:             Tue Mar 25 15:07:16 2025
2025-10-01T21:48:23.6526781Z  OS/Arch:           linux/amd64
2025-10-01T21:48:23.6527121Z  Context:           default
2025-10-01T21:48:23.6527342Z 
2025-10-01T21:48:23.6527484Z Server: Docker Engine - Community
2025-10-01T21:48:23.6527841Z  Engine:
2025-10-01T21:48:23.6528095Z   Version:          28.0.4
2025-10-01T21:48:23.6528377Z   API version:      1.48 (minimum version 1.24)
2025-10-01T21:48:23.6528646Z   Go version:       go1.23.7
2025-10-01T21:48:23.6528856Z   Git commit:       6430e49
2025-10-01T21:48:23.6529075Z   Built:            Tue Mar 25 15:07:16 2025
2025-10-01T21:48:23.6529619Z   OS/Arch:          linux/amd64
2025-10-01T21:48:23.6529825Z   Experimental:     false
2025-10-01T21:48:23.6530020Z  containerd:
2025-10-01T21:48:23.6530186Z   Version:          1.7.27
2025-10-01T21:48:23.6530429Z   GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
2025-10-01T21:48:23.6530692Z  runc:
2025-10-01T21:48:23.6530843Z   Version:          1.2.5
2025-10-01T21:48:23.6531040Z   GitCommit:        v1.2.5-0-g59923ef
2025-10-01T21:48:23.6531265Z  docker-init:
2025-10-01T21:48:23.6531434Z   Version:          0.19.0
2025-10-01T21:48:23.6531621Z   GitCommit:        de40ad0
2025-10-01T21:48:23.6569910Z [command]/usr/bin/docker info
2025-10-01T21:48:23.6945234Z Client: Docker Engine - Community
2025-10-01T21:48:23.6945714Z  Version:    28.0.4
2025-10-01T21:48:23.6946449Z  Context:    default
2025-10-01T21:48:23.6947128Z  Debug Mode: false
2025-10-01T21:48:23.6947727Z  Plugins:
2025-10-01T21:48:23.6948226Z   buildx: Docker Buildx (Docker Inc.)
2025-10-01T21:48:23.6948702Z     Version:  v0.28.0
2025-10-01T21:48:23.6949110Z     Path:     /usr/libexec/docker/cli-plugins/docker-buildx
2025-10-01T21:48:23.6949646Z   compose: Docker Compose (Docker Inc.)
2025-10-01T21:48:23.6950064Z     Version:  v2.38.2
2025-10-01T21:48:23.6950493Z     Path:     /usr/libexec/docker/cli-plugins/docker-compose
2025-10-01T21:48:23.6950881Z 
2025-10-01T21:48:23.6950996Z Server:
2025-10-01T21:48:23.6951275Z  Containers: 1
2025-10-01T21:48:23.6951577Z   Running: 1
2025-10-01T21:48:23.6951868Z   Paused: 0
2025-10-01T21:48:23.6952137Z   Stopped: 0
2025-10-01T21:48:23.6952429Z  Images: 2
2025-10-01T21:48:23.6952711Z  Server Version: 28.0.4
2025-10-01T21:48:23.6953052Z  Storage Driver: overlay2
2025-10-01T21:48:23.6953425Z   Backing Filesystem: extfs
2025-10-01T21:48:23.6953810Z   Supports d_type: true
2025-10-01T21:48:23.6954146Z   Using metacopy: false
2025-10-01T21:48:23.6954487Z   Native Overlay Diff: false
2025-10-01T21:48:23.6954846Z   userxattr: false
2025-10-01T21:48:23.6955182Z  Logging Driver: json-file
2025-10-01T21:48:23.6955550Z  Cgroup Driver: systemd
2025-10-01T21:48:23.6955869Z  Cgroup Version: 2
2025-10-01T21:48:23.6956169Z  Plugins:
2025-10-01T21:48:23.6956632Z   Volume: local
2025-10-01T21:48:23.6957434Z   Network: bridge host ipvlan macvlan null overlay
2025-10-01T21:48:23.6958089Z   Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
2025-10-01T21:48:23.6958796Z  Swarm: inactive
2025-10-01T21:48:23.6959165Z  Runtimes: io.containerd.runc.v2 runc
2025-10-01T21:48:23.6959563Z  Default Runtime: runc
2025-10-01T21:48:23.6959889Z  Init Binary: docker-init
2025-10-01T21:48:23.6960333Z  containerd version: 05044ec0a9a75232cad458027ca83437aae3f4da
2025-10-01T21:48:23.6960856Z  runc version: v1.2.5-0-g59923ef
2025-10-01T21:48:23.6961212Z  init version: de40ad0
2025-10-01T21:48:23.6961514Z  Security Options:
2025-10-01T21:48:23.6961776Z   apparmor
2025-10-01T21:48:23.6962045Z   seccomp
2025-10-01T21:48:23.6962305Z    Profile: builtin
2025-10-01T21:48:23.6962622Z   cgroupns
2025-10-01T21:48:23.6962807Z  Kernel Version: 6.11.0-1018-azure
2025-10-01T21:48:23.6963093Z  Operating System: Ubuntu 24.04.3 LTS
2025-10-01T21:48:23.6963414Z  OSType: linux
2025-10-01T21:48:23.6963591Z  Architecture: x86_64
2025-10-01T21:48:23.6963784Z  CPUs: 4
2025-10-01T21:48:23.6963943Z  Total Memory: 15.62GiB
2025-10-01T21:48:23.6964133Z  Name: runnervm3ublj
2025-10-01T21:48:23.6964331Z  ID: fc682960-a2cc-4975-884a-ddab89401ab0
2025-10-01T21:48:23.6964581Z  Docker Root Dir: /var/lib/docker
2025-10-01T21:48:23.6964788Z  Debug Mode: false
2025-10-01T21:48:23.6964971Z  Username: githubactions
2025-10-01T21:48:23.6965159Z  Experimental: false
2025-10-01T21:48:23.6965348Z  Insecure Registries:
2025-10-01T21:48:23.6965547Z   ::1/128
2025-10-01T21:48:23.6965694Z   127.0.0.0/8
2025-10-01T21:48:23.6965863Z  Live Restore Enabled: false
2025-10-01T21:48:23.6965999Z 
2025-10-01T21:48:23.6966988Z ##[endgroup]
2025-10-01T21:48:23.6967500Z ##[group]Proxy configuration
2025-10-01T21:48:23.6970770Z No proxy configuration found
2025-10-01T21:48:23.6971715Z ##[endgroup]
2025-10-01T21:48:23.7557619Z ##[group]Buildx version
2025-10-01T21:48:23.7588012Z [command]/usr/bin/docker buildx version
2025-10-01T21:48:23.8112594Z github.com/docker/buildx v0.28.0 b1281b81bba797b21d9eaf256e6a13eb14419836
2025-10-01T21:48:23.8143373Z ##[endgroup]
2025-10-01T21:48:23.8144081Z ##[group]Builder info
2025-10-01T21:48:23.9058487Z {
2025-10-01T21:48:23.9058773Z   "nodes": [
2025-10-01T21:48:23.9058956Z     {
2025-10-01T21:48:23.9059199Z       "name": "builder-54d1668b-0a40-40ea-89c4-8b55723638440",
2025-10-01T21:48:23.9059538Z       "endpoint": "unix:///var/run/docker.sock",
2025-10-01T21:48:23.9059805Z       "status": "running",
2025-10-01T21:48:23.9060265Z       "buildkitd-flags": "--allow-insecure-entitlement security.insecure --allow-insecure-entitlement network.host",
2025-10-01T21:48:23.9060741Z       "buildkit": "v0.24.0",
2025-10-01T21:48:23.9061031Z       "platforms": "linux/amd64,linux/amd64/v2,linux/amd64/v3,linux/386",
2025-10-01T21:48:23.9061363Z       "features": {
2025-10-01T21:48:23.9061632Z         "Automatically load images to the Docker Engine image store": true,
2025-10-01T21:48:23.9061955Z         "Cache export": true,
2025-10-01T21:48:23.9062181Z         "Direct push": true,
2025-10-01T21:48:23.9062387Z         "Docker exporter": true,
2025-10-01T21:48:23.9062620Z         "Multi-platform build": true,
2025-10-01T21:48:23.9062846Z         "OCI exporter": true
2025-10-01T21:48:23.9063036Z       },
2025-10-01T21:48:23.9063182Z       "labels": {
2025-10-01T21:48:23.9063411Z         "org.mobyproject.buildkit.worker.executor": "oci",
2025-10-01T21:48:23.9063767Z         "org.mobyproject.buildkit.worker.hostname": "7fbcd70e05d4",
2025-10-01T21:48:23.9064121Z         "org.mobyproject.buildkit.worker.network": "host",
2025-10-01T21:48:23.9064489Z         "org.mobyproject.buildkit.worker.oci.process-mode": "sandbox",
2025-10-01T21:48:23.9064883Z         "org.mobyproject.buildkit.worker.selinux.enabled": "false",
2025-10-01T21:48:23.9065272Z         "org.mobyproject.buildkit.worker.snapshotter": "overlayfs"
2025-10-01T21:48:23.9065559Z       },
2025-10-01T21:48:23.9065710Z       "gcPolicy": [
2025-10-01T21:48:23.9065875Z         {
2025-10-01T21:48:23.9066028Z           "all": false,
2025-10-01T21:48:23.9067140Z           "filter": [
2025-10-01T21:48:23.9067412Z             "type==source.local",
2025-10-01T21:48:23.9067651Z             "type==exec.cachemount",
2025-10-01T21:48:23.9067906Z             "type==source.git.checkout"
2025-10-01T21:48:23.9068131Z           ],
2025-10-01T21:48:23.9068301Z           "keepDuration": "48h0m0s"
2025-10-01T21:48:23.9068508Z         },
2025-10-01T21:48:23.9068650Z         {
2025-10-01T21:48:23.9068803Z           "all": false,
2025-10-01T21:48:23.9068993Z           "keepDuration": "1440h0m0s"
2025-10-01T21:48:23.9069208Z         },
2025-10-01T21:48:23.9069349Z         {
2025-10-01T21:48:23.9069504Z           "all": false
2025-10-01T21:48:23.9069670Z         },
2025-10-01T21:48:23.9069814Z         {
2025-10-01T21:48:23.9069966Z           "all": true
2025-10-01T21:48:23.9070136Z         }
2025-10-01T21:48:23.9070281Z       ]
2025-10-01T21:48:23.9070423Z     }
2025-10-01T21:48:23.9070565Z   ],
2025-10-01T21:48:23.9070769Z   "name": "builder-54d1668b-0a40-40ea-89c4-8b5572363844",
2025-10-01T21:48:23.9071057Z   "driver": "docker-container",
2025-10-01T21:48:23.9071281Z   "lastActivity": "2025-10-01T21:48:17.000Z"
2025-10-01T21:48:23.9071502Z }
2025-10-01T21:48:23.9071887Z ##[endgroup]
2025-10-01T21:48:24.0540792Z [command]/usr/bin/docker buildx build --file docker/Dockerfile --iidfile /home/runner/work/_temp/docker-actions-toolkit-qmXfnc/build-iidfile-e7f045b501.txt --tag ghcr.io/example/phase0:latest --load --metadata-file /home/runner/work/_temp/docker-actions-toolkit-qmXfnc/build-metadata-18f1c14f1a.json .
2025-10-01T21:48:24.3146773Z #0 building with "builder-54d1668b-0a40-40ea-89c4-8b5572363844" instance using docker-container driver
2025-10-01T21:48:24.3152185Z 
2025-10-01T21:48:24.3152732Z #1 [internal] load build definition from Dockerfile
2025-10-01T21:48:24.3155523Z #1 transferring dockerfile: 1.29kB done
2025-10-01T21:48:24.3157807Z #1 DONE 0.0s
2025-10-01T21:48:24.3158354Z 
2025-10-01T21:48:24.3158693Z #2 [auth] docker/dockerfile:pull token for registry-1.docker.io
2025-10-01T21:48:24.4647634Z #2 DONE 0.0s
2025-10-01T21:48:24.4647775Z 
2025-10-01T21:48:24.4648030Z #3 resolve image config for docker-image://docker.io/docker/dockerfile:1.5
2025-10-01T21:48:24.7902864Z #3 DONE 0.6s
2025-10-01T21:48:24.9516953Z 
2025-10-01T21:48:24.9519290Z #4 docker-image://docker.io/docker/dockerfile:1.5@sha256:39b85bbfa7536a5feceb7372a0817649ecb2724562a38360f4d6a7782a409b14
2025-10-01T21:48:24.9521428Z #4 resolve docker.io/docker/dockerfile:1.5@sha256:39b85bbfa7536a5feceb7372a0817649ecb2724562a38360f4d6a7782a409b14 done
2025-10-01T21:48:24.9538058Z #4 sha256:a47ff7046597eea0123ea02817165350e3680f75000dc5d69c9a310258e1bedd 3.15MB / 11.55MB 0.2s
2025-10-01T21:48:25.0906838Z #4 sha256:a47ff7046597eea0123ea02817165350e3680f75000dc5d69c9a310258e1bedd 11.55MB / 11.55MB 0.2s done
2025-10-01T21:48:25.0908073Z #4 extracting sha256:a47ff7046597eea0123ea02817165350e3680f75000dc5d69c9a310258e1bedd 0.1s done
2025-10-01T21:48:25.0908830Z #4 DONE 0.3s
2025-10-01T21:48:25.3324684Z 
2025-10-01T21:48:25.3325247Z #5 [internal] load .dockerignore
2025-10-01T21:48:25.3325599Z #5 transferring context: 2B done
2025-10-01T21:48:25.3325876Z #5 DONE 0.0s
2025-10-01T21:48:25.3326001Z 
2025-10-01T21:48:25.3326184Z #6 [auth] library/python:pull token for registry-1.docker.io
2025-10-01T21:48:25.3326744Z #6 DONE 0.0s
2025-10-01T21:48:25.3326866Z 
2025-10-01T21:48:25.3327100Z #7 [internal] load metadata for docker.io/library/python:3.11-slim-bookworm
2025-10-01T21:48:25.5417776Z #7 DONE 0.4s
2025-10-01T21:48:25.6511956Z 
2025-10-01T21:48:25.6513352Z #8 [internal] load build context
2025-10-01T21:48:25.6513793Z #8 transferring context: 33.19kB done
2025-10-01T21:48:25.6514181Z #8 DONE 0.0s
2025-10-01T21:48:25.6514366Z 
2025-10-01T21:48:25.6514944Z #9 [base 1/2] FROM docker.io/library/python:3.11-slim-bookworm@sha256:86adf8dbadc3d6e82ee5dd2c74bec2e1c2467cdad47886280501df722372d2e1
2025-10-01T21:48:25.6516517Z #9 resolve docker.io/library/python:3.11-slim-bookworm@sha256:86adf8dbadc3d6e82ee5dd2c74bec2e1c2467cdad47886280501df722372d2e1 done
2025-10-01T21:48:25.6517460Z #9 sha256:d61a97008ede65db3758de8f7a677cf8517b7f116afef669aed832e67e2c356d 248B / 248B 0.1s done
2025-10-01T21:48:25.8131619Z #9 sha256:38b7e0d95f778b3fc0d776da12ef5667ee21184575681b6b9f6dd4745dc73117 3.52MB / 3.52MB 0.2s done
2025-10-01T21:48:25.8133105Z #9 sha256:5c32499ab806884c5725c705c2bf528662d034ed99de13d3205309e0d9ef0375 0B / 28.23MB 0.2s
2025-10-01T21:48:25.8134037Z #9 sha256:a64c132cd1a4c24753f5f9e42368aee15e25618d5238443af101322c19ffc38b 0B / 16.21MB 0.2s
2025-10-01T21:48:26.0401072Z #9 sha256:5c32499ab806884c5725c705c2bf528662d034ed99de13d3205309e0d9ef0375 14.68MB / 28.23MB 0.5s
2025-10-01T21:48:26.0402227Z #9 sha256:a64c132cd1a4c24753f5f9e42368aee15e25618d5238443af101322c19ffc38b 2.10MB / 16.21MB 0.3s
2025-10-01T21:48:26.2900095Z #9 sha256:5c32499ab806884c5725c705c2bf528662d034ed99de13d3205309e0d9ef0375 28.23MB / 28.23MB 0.5s done
2025-10-01T21:48:26.2901336Z #9 sha256:a64c132cd1a4c24753f5f9e42368aee15e25618d5238443af101322c19ffc38b 16.21MB / 16.21MB 0.5s done
2025-10-01T21:48:26.2902375Z #9 extracting sha256:5c32499ab806884c5725c705c2bf528662d034ed99de13d3205309e0d9ef0375
2025-10-01T21:48:26.8438843Z #9 extracting sha256:5c32499ab806884c5725c705c2bf528662d034ed99de13d3205309e0d9ef0375 0.7s done
2025-10-01T21:48:26.8439360Z #9 DONE 1.3s
2025-10-01T21:48:27.0872488Z 
2025-10-01T21:48:27.0873436Z #9 [base 1/2] FROM docker.io/library/python:3.11-slim-bookworm@sha256:86adf8dbadc3d6e82ee5dd2c74bec2e1c2467cdad47886280501df722372d2e1
2025-10-01T21:48:27.0874768Z #9 extracting sha256:38b7e0d95f778b3fc0d776da12ef5667ee21184575681b6b9f6dd4745dc73117 0.1s done
2025-10-01T21:48:27.0875773Z #9 extracting sha256:a64c132cd1a4c24753f5f9e42368aee15e25618d5238443af101322c19ffc38b
2025-10-01T21:48:27.3736776Z #9 extracting sha256:a64c132cd1a4c24753f5f9e42368aee15e25618d5238443af101322c19ffc38b 0.4s done
2025-10-01T21:48:27.3737512Z #9 DONE 1.8s
2025-10-01T21:48:27.4812526Z 
2025-10-01T21:48:27.4814125Z #9 [base 1/2] FROM docker.io/library/python:3.11-slim-bookworm@sha256:86adf8dbadc3d6e82ee5dd2c74bec2e1c2467cdad47886280501df722372d2e1
2025-10-01T21:48:27.4815472Z #9 extracting sha256:d61a97008ede65db3758de8f7a677cf8517b7f116afef669aed832e67e2c356d done
2025-10-01T21:48:27.4816167Z #9 DONE 1.8s
2025-10-01T21:48:27.4816483Z 
2025-10-01T21:48:27.4816626Z #10 [base 2/2] WORKDIR /app
2025-10-01T21:48:27.4816959Z #10 DONE 0.1s
2025-10-01T21:48:27.6129801Z 
2025-10-01T21:48:27.6130763Z #11 [builder 1/3] RUN apt-get update &&     apt-get install -y --no-install-recommends build-essential git &&     rm -rf /var/lib/apt/lists/*
2025-10-01T21:48:27.6131717Z #11 0.130 Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
2025-10-01T21:48:27.7369361Z #11 0.221 Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
2025-10-01T21:48:27.7371194Z #11 0.255 Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
2025-10-01T21:48:27.9207514Z #11 0.288 Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8791 kB]
2025-10-01T21:48:27.9969524Z #11 0.514 Get:5 http://deb.debian.org/debian bookworm-updates/main amd64 Packages [6924 B]
2025-10-01T21:48:28.1472890Z #11 0.515 Get:6 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [280 kB]
2025-10-01T21:48:28.7150283Z #11 1.233 Fetched 9333 kB in 1s (8022 kB/s)
2025-10-01T21:48:29.0932407Z #11 1.233 Reading package lists...
2025-10-01T21:48:29.4755594Z #11 1.628 Reading package lists...
2025-10-01T21:48:29.6526555Z #11 2.003 Building dependency tree...
2025-10-01T21:48:29.6527370Z #11 2.083 Reading state information...
2025-10-01T21:48:29.6528126Z #11 2.170 The following additional packages will be installed:
2025-10-01T21:48:29.6529073Z #11 2.170   binutils binutils-common binutils-x86-64-linux-gnu bzip2 cpp cpp-12 dpkg-dev
2025-10-01T21:48:29.8046188Z #11 2.170   g++ g++-12 gcc gcc-12 git-man libasan8 libatomic1 libbinutils libbrotli1
2025-10-01T21:48:29.8047288Z #11 2.170   libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0 libctf0
2025-10-01T21:48:29.8048477Z #11 2.170   libcurl3-gnutls libdpkg-perl liberror-perl libexpat1 libgcc-12-dev
2025-10-01T21:48:29.8049302Z #11 2.170   libgdbm-compat4 libgomp1 libgprofng0 libisl23 libitm1 libjansson4
2025-10-01T21:48:29.8050143Z #11 2.171   libldap-2.5-0 liblsan0 libmpc3 libmpfr6 libnghttp2-14 libnsl-dev libperl5.36
2025-10-01T21:48:29.8051007Z #11 2.171   libpsl5 libquadmath0 librtmp1 libsasl2-2 libsasl2-modules-db libssh2-1
2025-10-01T21:48:29.8051861Z #11 2.171   libstdc++-12-dev libtirpc-dev libtsan2 libubsan1 linux-libc-dev make patch
2025-10-01T21:48:29.8052581Z #11 2.171   perl perl-modules-5.36 rpcsvc-proto xz-utils
2025-10-01T21:48:29.8053057Z #11 2.172 Suggested packages:
2025-10-01T21:48:29.8053636Z #11 2.172   binutils-doc bzip2-doc cpp-doc gcc-12-locales cpp-12-doc debian-keyring
2025-10-01T21:48:29.8054466Z #11 2.172   g++-multilib g++-12-multilib gcc-12-doc gcc-multilib manpages-dev autoconf
2025-10-01T21:48:29.8055276Z #11 2.172   automake libtool flex bison gdb gcc-doc gcc-12-multilib gettext-base
2025-10-01T21:48:29.8056097Z #11 2.172   git-daemon-run | git-daemon-sysvinit git-doc git-email git-gui gitk gitweb
2025-10-01T21:48:29.8057193Z #11 2.172   git-cvs git-mediawiki git-svn glibc-doc gnupg | sq | sqop | pgpainless-cli
2025-10-01T21:48:29.8058024Z #11 2.172   sensible-utils bzr libstdc++-12-doc make-doc ed diffutils-doc perl-doc
2025-10-01T21:48:29.8058776Z #11 2.172   libterm-readline-gnu-perl | libterm-readline-perl-perl
2025-10-01T21:48:29.8059365Z #11 2.172   libtap-harness-archive-perl
2025-10-01T21:48:29.8059795Z #11 2.172 Recommended packages:
2025-10-01T21:48:29.8060352Z #11 2.172   fakeroot gnupg | sq | sqop | pgpainless-cli libalgorithm-merge-perl less
2025-10-01T21:48:29.8061168Z #11 2.172   ssh-client manpages manpages-dev libc-devtools libfile-fcntllock-perl
2025-10-01T21:48:29.8062254Z #11 2.172   liblocale-gettext-perl libldap-common publicsuffix libsasl2-modules
2025-10-01T21:48:29.8821132Z #11 2.399 The following NEW packages will be installed:
2025-10-01T21:48:29.8822095Z #11 2.399   binutils binutils-common binutils-x86-64-linux-gnu build-essential bzip2 cpp
2025-10-01T21:48:30.0272444Z #11 2.399   cpp-12 dpkg-dev g++ g++-12 gcc gcc-12 git git-man libasan8 libatomic1
2025-10-01T21:48:30.0273534Z #11 2.400   libbinutils libbrotli1 libc-dev-bin libc6-dev libcc1-0 libcrypt-dev
2025-10-01T21:48:30.0274560Z #11 2.400   libctf-nobfd0 libctf0 libcurl3-gnutls libdpkg-perl liberror-perl libexpat1
2025-10-01T21:48:30.0275360Z #11 2.400   libgcc-12-dev libgdbm-compat4 libgomp1 libgprofng0 libisl23 libitm1
2025-10-01T21:48:30.0276166Z #11 2.400   libjansson4 libldap-2.5-0 liblsan0 libmpc3 libmpfr6 libnghttp2-14 libnsl-dev
2025-10-01T21:48:30.0277167Z #11 2.400   libperl5.36 libpsl5 libquadmath0 librtmp1 libsasl2-2 libsasl2-modules-db
2025-10-01T21:48:30.0277985Z #11 2.400   libssh2-1 libstdc++-12-dev libtirpc-dev libtsan2 libubsan1 linux-libc-dev
2025-10-01T21:48:30.0278758Z #11 2.400   make patch perl perl-modules-5.36 rpcsvc-proto xz-utils
2025-10-01T21:48:30.0279475Z #11 2.462 0 upgraded, 59 newly installed, 0 to remove and 2 not upgraded.
2025-10-01T21:48:30.0279996Z #11 2.462 Need to get 84.3 MB of archives.
2025-10-01T21:48:30.0280536Z #11 2.462 After this operation, 366 MB of additional disk space will be used.
2025-10-01T21:48:30.0281440Z #11 2.462 Get:1 http://deb.debian.org/debian bookworm/main amd64 perl-modules-5.36 all 5.36.0-7+deb12u3 [2815 kB]
2025-10-01T21:48:30.0282449Z #11 2.545 Get:2 http://deb.debian.org/debian bookworm/main amd64 libgdbm-compat4 amd64 1.23-3 [48.2 kB]
2025-10-01T21:48:30.1799697Z #11 2.546 Get:3 http://deb.debian.org/debian bookworm/main amd64 libperl5.36 amd64 5.36.0-7+deb12u3 [4196 kB]
2025-10-01T21:48:30.1800519Z #11 2.563 Get:4 http://deb.debian.org/debian bookworm/main amd64 perl amd64 5.36.0-7+deb12u3 [239 kB]
2025-10-01T21:48:30.1801257Z #11 2.564 Get:5 http://deb.debian.org/debian bookworm/main amd64 bzip2 amd64 1.0.8-5+b1 [49.8 kB]
2025-10-01T21:48:30.1802155Z #11 2.571 Get:6 http://deb.debian.org/debian bookworm/main amd64 xz-utils amd64 5.4.1-1 [471 kB]
2025-10-01T21:48:30.1802888Z #11 2.626 Get:7 http://deb.debian.org/debian bookworm/main amd64 binutils-common amd64 2.40-2 [2487 kB]
2025-10-01T21:48:30.1803603Z #11 2.698 Get:8 http://deb.debian.org/debian bookworm/main amd64 libbinutils amd64 2.40-2 [572 kB]
2025-10-01T21:48:30.2803447Z #11 2.710 Get:9 http://deb.debian.org/debian bookworm/main amd64 libctf-nobfd0 amd64 2.40-2 [153 kB]
2025-10-01T21:48:30.2804747Z #11 2.727 Get:10 http://deb.debian.org/debian bookworm/main amd64 libctf0 amd64 2.40-2 [89.8 kB]
2025-10-01T21:48:30.2805580Z #11 2.732 Get:11 http://deb.debian.org/debian bookworm/main amd64 libgprofng0 amd64 2.40-2 [812 kB]
2025-10-01T21:48:30.2806560Z #11 2.748 Get:12 http://deb.debian.org/debian bookworm/main amd64 libjansson4 amd64 2.14-2 [40.8 kB]
2025-10-01T21:48:30.2807303Z #11 2.751 Get:13 http://deb.debian.org/debian bookworm/main amd64 binutils-x86-64-linux-gnu amd64 2.40-2 [2246 kB]
2025-10-01T21:48:30.2808293Z #11 2.771 Get:14 http://deb.debian.org/debian bookworm/main amd64 binutils amd64 2.40-2 [65.0 kB]
2025-10-01T21:48:30.2809189Z #11 2.772 Get:15 http://deb.debian.org/debian bookworm/main amd64 libc-dev-bin amd64 2.36-9+deb12u13 [47.4 kB]
2025-10-01T21:48:30.2809995Z #11 2.775 Get:16 http://deb.debian.org/debian-security bookworm-security/main amd64 linux-libc-dev amd64 6.1.153-1 [2192 kB]
2025-10-01T21:48:30.2810782Z #11 2.793 Get:17 http://deb.debian.org/debian bookworm/main amd64 libcrypt-dev amd64 1:4.4.33-2 [118 kB]
2025-10-01T21:48:30.2811461Z #11 2.798 Get:18 http://deb.debian.org/debian bookworm/main amd64 libtirpc-dev amd64 1.3.3+ds-1 [191 kB]
2025-10-01T21:48:30.3844414Z #11 2.805 Get:19 http://deb.debian.org/debian bookworm/main amd64 libnsl-dev amd64 1.3.0-2 [66.4 kB]
2025-10-01T21:48:30.3845966Z #11 2.807 Get:20 http://deb.debian.org/debian bookworm/main amd64 rpcsvc-proto amd64 1.4.3-1 [63.3 kB]
2025-10-01T21:48:30.3847479Z #11 2.809 Get:21 http://deb.debian.org/debian bookworm/main amd64 libc6-dev amd64 2.36-9+deb12u13 [1904 kB]
2025-10-01T21:48:30.3848775Z #11 2.822 Get:22 http://deb.debian.org/debian bookworm/main amd64 libisl23 amd64 0.25-1.1 [683 kB]
2025-10-01T21:48:30.3849618Z #11 2.826 Get:23 http://deb.debian.org/debian bookworm/main amd64 libmpfr6 amd64 4.2.0-1 [701 kB]
2025-10-01T21:48:30.3850300Z #11 2.831 Get:24 http://deb.debian.org/debian bookworm/main amd64 libmpc3 amd64 1.3.1-1 [51.5 kB]
2025-10-01T21:48:30.3851017Z #11 2.832 Get:25 http://deb.debian.org/debian bookworm/main amd64 cpp-12 amd64 12.2.0-14+deb12u1 [9768 kB]
2025-10-01T21:48:30.3851726Z #11 2.879 Get:26 http://deb.debian.org/debian bookworm/main amd64 cpp amd64 4:12.2.0-3 [6836 B]
2025-10-01T21:48:30.3852434Z #11 2.879 Get:27 http://deb.debian.org/debian bookworm/main amd64 libcc1-0 amd64 12.2.0-14+deb12u1 [41.7 kB]
2025-10-01T21:48:30.3853207Z #11 2.880 Get:28 http://deb.debian.org/debian bookworm/main amd64 libgomp1 amd64 12.2.0-14+deb12u1 [116 kB]
2025-10-01T21:48:30.3853968Z #11 2.881 Get:29 http://deb.debian.org/debian bookworm/main amd64 libitm1 amd64 12.2.0-14+deb12u1 [26.1 kB]
2025-10-01T21:48:30.3854736Z #11 2.881 Get:30 http://deb.debian.org/debian bookworm/main amd64 libatomic1 amd64 12.2.0-14+deb12u1 [9376 B]
2025-10-01T21:48:30.3855392Z #11 2.882 Get:31 http://deb.debian.org/debian bookworm/main amd64 libasan8 amd64 12.2.0-14+deb12u1 [2193 kB]
2025-10-01T21:48:30.3855980Z #11 2.890 Get:32 http://deb.debian.org/debian bookworm/main amd64 liblsan0 amd64 12.2.0-14+deb12u1 [969 kB]
2025-10-01T21:48:30.3856837Z #11 2.894 Get:33 http://deb.debian.org/debian bookworm/main amd64 libtsan2 amd64 12.2.0-14+deb12u1 [2197 kB]
2025-10-01T21:48:30.3857408Z #11 2.902 Get:34 http://deb.debian.org/debian bookworm/main amd64 libubsan1 amd64 12.2.0-14+deb12u1 [883 kB]
2025-10-01T21:48:30.5780977Z #11 2.906 Get:35 http://deb.debian.org/debian bookworm/main amd64 libquadmath0 amd64 12.2.0-14+deb12u1 [145 kB]
2025-10-01T21:48:30.5781990Z #11 2.915 Get:36 http://deb.debian.org/debian bookworm/main amd64 libgcc-12-dev amd64 12.2.0-14+deb12u1 [2437 kB]
2025-10-01T21:48:30.5782939Z #11 2.945 Get:37 http://deb.debian.org/debian bookworm/main amd64 gcc-12 amd64 12.2.0-14+deb12u1 [19.3 MB]
2025-10-01T21:48:30.6231281Z #11 3.141 Get:38 http://deb.debian.org/debian bookworm/main amd64 gcc amd64 4:12.2.0-3 [5216 B]
2025-10-01T21:48:30.7414144Z #11 3.196 Get:39 http://deb.debian.org/debian bookworm/main amd64 libstdc++-12-dev amd64 12.2.0-14+deb12u1 [2047 kB]
2025-10-01T21:48:30.7415229Z #11 3.259 Get:40 http://deb.debian.org/debian bookworm/main amd64 g++-12 amd64 12.2.0-14+deb12u1 [10.7 MB]
2025-10-01T21:48:30.9350840Z #11 3.452 Get:41 http://deb.debian.org/debian bookworm/main amd64 g++ amd64 4:12.2.0-3 [1356 B]
2025-10-01T21:48:31.0383595Z #11 3.453 Get:42 http://deb.debian.org/debian bookworm/main amd64 make amd64 4.3-4.1 [396 kB]
2025-10-01T21:48:31.0384811Z #11 3.455 Get:43 http://deb.debian.org/debian bookworm/main amd64 libdpkg-perl all 1.21.22 [603 kB]
2025-10-01T21:48:31.0385779Z #11 3.462 Get:44 http://deb.debian.org/debian bookworm/main amd64 patch amd64 2.7.6-7 [128 kB]
2025-10-01T21:48:31.0386761Z #11 3.471 Get:45 http://deb.debian.org/debian bookworm/main amd64 dpkg-dev all 1.21.22 [1353 kB]
2025-10-01T21:48:31.0387393Z #11 3.535 Get:46 http://deb.debian.org/debian bookworm/main amd64 build-essential amd64 12.9 [7704 B]
2025-10-01T21:48:31.0388025Z #11 3.540 Get:47 http://deb.debian.org/debian bookworm/main amd64 libbrotli1 amd64 1.0.9-2+b6 [275 kB]
2025-10-01T21:48:31.0388705Z #11 3.556 Get:48 http://deb.debian.org/debian bookworm/main amd64 libsasl2-modules-db amd64 2.1.28+dfsg-10 [20.3 kB]
2025-10-01T21:48:31.1382331Z #11 3.569 Get:49 http://deb.debian.org/debian bookworm/main amd64 libsasl2-2 amd64 2.1.28+dfsg-10 [59.7 kB]
2025-10-01T21:48:31.1383448Z #11 3.584 Get:50 http://deb.debian.org/debian bookworm/main amd64 libldap-2.5-0 amd64 2.5.13+dfsg-5 [183 kB]
2025-10-01T21:48:31.1385715Z #11 3.593 Get:51 http://deb.debian.org/debian bookworm/main amd64 libnghttp2-14 amd64 1.52.0-1+deb12u2 [73.0 kB]
2025-10-01T21:48:31.1386740Z #11 3.596 Get:52 http://deb.debian.org/debian bookworm/main amd64 libpsl5 amd64 0.21.2-1 [58.7 kB]
2025-10-01T21:48:31.1387527Z #11 3.598 Get:53 http://deb.debian.org/debian bookworm/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d.1-2+b2 [60.8 kB]
2025-10-01T21:48:31.1388428Z #11 3.603 Get:54 http://deb.debian.org/debian bookworm/main amd64 libssh2-1 amd64 1.10.0-3+b1 [179 kB]
2025-10-01T21:48:31.1389220Z #11 3.623 Get:55 http://deb.debian.org/debian bookworm/main amd64 libcurl3-gnutls amd64 7.88.1-10+deb12u14 [386 kB]
2025-10-01T21:48:31.1389833Z #11 3.652 Get:56 http://deb.debian.org/debian bookworm/main amd64 libexpat1 amd64 2.5.0-1+deb12u2 [99.9 kB]
2025-10-01T21:48:31.1390438Z #11 3.656 Get:57 http://deb.debian.org/debian bookworm/main amd64 liberror-perl all 0.17029-2 [29.0 kB]
2025-10-01T21:48:31.2869474Z #11 3.658 Get:58 http://deb.debian.org/debian bookworm/main amd64 git-man all 1:2.39.5-0+deb12u2 [2053 kB]
2025-10-01T21:48:31.2870307Z #11 3.683 Get:59 http://deb.debian.org/debian bookworm/main amd64 git amd64 1:2.39.5-0+deb12u2 [7260 kB]
2025-10-01T21:48:31.2871013Z #11 3.804 debconf: delaying package configuration, since apt-utils is not installed
2025-10-01T21:48:31.4792110Z #11 3.826 Fetched 84.3 MB in 1s (64.6 MB/s)
2025-10-01T21:48:31.4793095Z #11 3.839 Selecting previously unselected package perl-modules-5.36.
2025-10-01T21:48:31.4793720Z #11 3.839 (Reading database ... 
2025-10-01T21:48:31.4794106Z (Reading database ... 5%
2025-10-01T21:48:31.4794456Z (Reading database ... 10%
2025-10-01T21:48:31.4794812Z (Reading database ... 15%
2025-10-01T21:48:31.4795149Z (Reading database ... 20%
2025-10-01T21:48:31.4795495Z (Reading database ... 25%
2025-10-01T21:48:31.4795829Z (Reading database ... 30%
2025-10-01T21:48:31.4796169Z (Reading database ... 35%
2025-10-01T21:48:31.4796711Z (Reading database ... 40%
2025-10-01T21:48:31.4797089Z (Reading database ... 45%
2025-10-01T21:48:31.4797425Z (Reading database ... 50%
2025-10-01T21:48:31.4797761Z (Reading database ... 55%
2025-10-01T21:48:31.4798103Z (Reading database ... 60%
2025-10-01T21:48:31.4798715Z (Reading database ... 65%
2025-10-01T21:48:31.4799060Z (Reading database ... 70%
2025-10-01T21:48:31.4799392Z (Reading database ... 75%
2025-10-01T21:48:31.4799727Z (Reading database ... 80%
2025-10-01T21:48:31.4800059Z (Reading database ... 85%
2025-10-01T21:48:31.4800395Z (Reading database ... 90%
2025-10-01T21:48:31.4800725Z (Reading database ... 95%
2025-10-01T21:48:31.4801062Z (Reading database ... 100%
2025-10-01T21:48:31.4801573Z (Reading database ... 6694 files and directories currently installed.)
2025-10-01T21:48:31.4802344Z #11 3.845 Preparing to unpack .../00-perl-modules-5.36_5.36.0-7+deb12u3_all.deb ...
2025-10-01T21:48:31.4803040Z #11 3.846 Unpacking perl-modules-5.36 (5.36.0-7+deb12u3) ...
2025-10-01T21:48:31.6228404Z #11 4.140 Selecting previously unselected package libgdbm-compat4:amd64.
2025-10-01T21:48:31.7959277Z #11 4.142 Preparing to unpack .../01-libgdbm-compat4_1.23-3_amd64.deb ...
2025-10-01T21:48:31.7959958Z #11 4.144 Unpacking libgdbm-compat4:amd64 (1.23-3) ...
2025-10-01T21:48:31.7960614Z #11 4.161 Selecting previously unselected package libperl5.36:amd64.
2025-10-01T21:48:31.7961315Z #11 4.162 Preparing to unpack .../02-libperl5.36_5.36.0-7+deb12u3_amd64.deb ...
2025-10-01T21:48:31.7961965Z #11 4.163 Unpacking libperl5.36:amd64 (5.36.0-7+deb12u3) ...
2025-10-01T21:48:31.9230980Z #11 4.441 Selecting previously unselected package perl.
2025-10-01T21:48:32.0267302Z #11 4.442 Preparing to unpack .../03-perl_5.36.0-7+deb12u3_amd64.deb ...
2025-10-01T21:48:32.0269795Z #11 4.448 Unpacking perl (5.36.0-7+deb12u3) ...
2025-10-01T21:48:32.0270356Z #11 4.476 Selecting previously unselected package bzip2.
2025-10-01T21:48:32.0270950Z #11 4.477 Preparing to unpack .../04-bzip2_1.0.8-5+b1_amd64.deb ...
2025-10-01T21:48:32.0271473Z #11 4.478 Unpacking bzip2 (1.0.8-5+b1) ...
2025-10-01T21:48:32.0272357Z #11 4.496 Selecting previously unselected package xz-utils.
2025-10-01T21:48:32.0272878Z #11 4.497 Preparing to unpack .../05-xz-utils_5.4.1-1_amd64.deb ...
2025-10-01T21:48:32.0273214Z #11 4.498 Unpacking xz-utils (5.4.1-1) ...
2025-10-01T21:48:32.0273540Z #11 4.544 Selecting previously unselected package binutils-common:amd64.
2025-10-01T21:48:32.1795355Z #11 4.546 Preparing to unpack .../06-binutils-common_2.40-2_amd64.deb ...
2025-10-01T21:48:32.1796022Z #11 4.547 Unpacking binutils-common:amd64 (2.40-2) ...
2025-10-01T21:48:32.1947773Z #11 4.712 Selecting previously unselected package libbinutils:amd64.
2025-10-01T21:48:32.3598525Z #11 4.714 Preparing to unpack .../07-libbinutils_2.40-2_amd64.deb ...
2025-10-01T21:48:32.3599468Z #11 4.715 Unpacking libbinutils:amd64 (2.40-2) ...
2025-10-01T21:48:32.3599944Z #11 4.763 Selecting previously unselected package libctf-nobfd0:amd64.
2025-10-01T21:48:32.3600497Z #11 4.765 Preparing to unpack .../08-libctf-nobfd0_2.40-2_amd64.deb ...
2025-10-01T21:48:32.3600960Z #11 4.765 Unpacking libctf-nobfd0:amd64 (2.40-2) ...
2025-10-01T21:48:32.3601344Z #11 4.788 Selecting previously unselected package libctf0:amd64.
2025-10-01T21:48:32.3601827Z #11 4.789 Preparing to unpack .../09-libctf0_2.40-2_amd64.deb ...
2025-10-01T21:48:32.3602151Z #11 4.790 Unpacking libctf0:amd64 (2.40-2) ...
2025-10-01T21:48:32.3602529Z #11 4.810 Selecting previously unselected package libgprofng0:amd64.
2025-10-01T21:48:32.3602974Z #11 4.811 Preparing to unpack .../10-libgprofng0_2.40-2_amd64.deb ...
2025-10-01T21:48:32.3603368Z #11 4.812 Unpacking libgprofng0:amd64 (2.40-2) ...
2025-10-01T21:48:32.3603751Z #11 4.877 Selecting previously unselected package libjansson4:amd64.
2025-10-01T21:48:32.5307171Z #11 4.879 Preparing to unpack .../11-libjansson4_2.14-2_amd64.deb ...
2025-10-01T21:48:32.5307808Z #11 4.880 Unpacking libjansson4:amd64 (2.14-2) ...
2025-10-01T21:48:32.5308452Z #11 4.896 Selecting previously unselected package binutils-x86-64-linux-gnu.
2025-10-01T21:48:32.5309275Z #11 4.897 Preparing to unpack .../12-binutils-x86-64-linux-gnu_2.40-2_amd64.deb ...
2025-10-01T21:48:32.5309934Z #11 4.898 Unpacking binutils-x86-64-linux-gnu (2.40-2) ...
2025-10-01T21:48:32.5565295Z #11 5.074 Selecting previously unselected package binutils.
2025-10-01T21:48:32.7515962Z #11 5.076 Preparing to unpack .../13-binutils_2.40-2_amd64.deb ...
2025-10-01T21:48:32.7516822Z #11 5.077 Unpacking binutils (2.40-2) ...
2025-10-01T21:48:32.7517302Z #11 5.097 Selecting previously unselected package libc-dev-bin.
2025-10-01T21:48:32.7517748Z #11 5.098 Preparing to unpack .../14-libc-dev-bin_2.36-9+deb12u13_amd64.deb ...
2025-10-01T21:48:32.7518156Z #11 5.099 Unpacking libc-dev-bin (2.36-9+deb12u13) ...
2025-10-01T21:48:32.7518533Z #11 5.116 Selecting previously unselected package linux-libc-dev:amd64.
2025-10-01T21:48:32.7518952Z #11 5.118 Preparing to unpack .../15-linux-libc-dev_6.1.153-1_amd64.deb ...
2025-10-01T21:48:32.7519315Z #11 5.119 Unpacking linux-libc-dev:amd64 (6.1.153-1) ...
2025-10-01T21:48:32.7876813Z #11 5.305 Selecting previously unselected package libcrypt-dev:amd64.
2025-10-01T21:48:32.8884156Z #11 5.307 Preparing to unpack .../16-libcrypt-dev_1%3a4.4.33-2_amd64.deb ...
2025-10-01T21:48:32.8885062Z #11 5.312 Unpacking libcrypt-dev:amd64 (1:4.4.33-2) ...
2025-10-01T21:48:32.8885720Z #11 5.332 Selecting previously unselected package libtirpc-dev:amd64.
2025-10-01T21:48:32.8886685Z #11 5.334 Preparing to unpack .../17-libtirpc-dev_1.3.3+ds-1_amd64.deb ...
2025-10-01T21:48:32.8887095Z #11 5.337 Unpacking libtirpc-dev:amd64 (1.3.3+ds-1) ...
2025-10-01T21:48:32.8887700Z #11 5.362 Selecting previously unselected package libnsl-dev:amd64.
2025-10-01T21:48:32.8888321Z #11 5.364 Preparing to unpack .../18-libnsl-dev_1.3.0-2_amd64.deb ...
2025-10-01T21:48:32.8888663Z #11 5.365 Unpacking libnsl-dev:amd64 (1.3.0-2) ...
2025-10-01T21:48:32.8889008Z #11 5.383 Selecting previously unselected package rpcsvc-proto.
2025-10-01T21:48:32.8889449Z #11 5.384 Preparing to unpack .../19-rpcsvc-proto_1.4.3-1_amd64.deb ...
2025-10-01T21:48:32.8890390Z #11 5.385 Unpacking rpcsvc-proto (1.4.3-1) ...
2025-10-01T21:48:32.8890998Z #11 5.405 Selecting previously unselected package libc6-dev:amd64.
2025-10-01T21:48:32.8891709Z #11 5.406 Preparing to unpack .../20-libc6-dev_2.36-9+deb12u13_amd64.deb ...
2025-10-01T21:48:33.0318541Z #11 5.407 Unpacking libc6-dev:amd64 (2.36-9+deb12u13) ...
2025-10-01T21:48:33.0319208Z #11 5.549 Selecting previously unselected package libisl23:amd64.
2025-10-01T21:48:33.1326811Z #11 5.551 Preparing to unpack .../21-libisl23_0.25-1.1_amd64.deb ...
2025-10-01T21:48:33.1327460Z #11 5.552 Unpacking libisl23:amd64 (0.25-1.1) ...
2025-10-01T21:48:33.1327986Z #11 5.608 Selecting previously unselected package libmpfr6:amd64.
2025-10-01T21:48:33.1328501Z #11 5.610 Preparing to unpack .../22-libmpfr6_4.2.0-1_amd64.deb ...
2025-10-01T21:48:33.1328843Z #11 5.611 Unpacking libmpfr6:amd64 (4.2.0-1) ...
2025-10-01T21:48:33.1329277Z #11 5.648 Selecting previously unselected package libmpc3:amd64.
2025-10-01T21:48:33.1329678Z #11 5.649 Preparing to unpack .../23-libmpc3_1.3.1-1_amd64.deb ...
2025-10-01T21:48:33.1330100Z #11 5.650 Unpacking libmpc3:amd64 (1.3.1-1) ...
2025-10-01T21:48:33.3010452Z #11 5.666 Selecting previously unselected package cpp-12.
2025-10-01T21:48:33.3011172Z #11 5.667 Preparing to unpack .../24-cpp-12_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:33.3011785Z #11 5.668 Unpacking cpp-12 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:33.6383667Z #11 6.156 Selecting previously unselected package cpp.
2025-10-01T21:48:33.8853831Z #11 6.158 Preparing to unpack .../25-cpp_4%3a12.2.0-3_amd64.deb ...
2025-10-01T21:48:33.8854492Z #11 6.159 Unpacking cpp (4:12.2.0-3) ...
2025-10-01T21:48:33.8855057Z #11 6.174 Selecting previously unselected package libcc1-0:amd64.
2025-10-01T21:48:33.8855644Z #11 6.175 Preparing to unpack .../26-libcc1-0_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:33.8856035Z #11 6.176 Unpacking libcc1-0:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:33.8856637Z #11 6.193 Selecting previously unselected package libgomp1:amd64.
2025-10-01T21:48:33.8857154Z #11 6.194 Preparing to unpack .../27-libgomp1_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:33.8857521Z #11 6.195 Unpacking libgomp1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:33.8858256Z #11 6.216 Selecting previously unselected package libitm1:amd64.
2025-10-01T21:48:33.8858867Z #11 6.217 Preparing to unpack .../28-libitm1_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:33.8859415Z #11 6.218 Unpacking libitm1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:33.8859962Z #11 6.234 Selecting previously unselected package libatomic1:amd64.
2025-10-01T21:48:33.8860637Z #11 6.235 Preparing to unpack .../29-libatomic1_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:33.8861244Z #11 6.236 Unpacking libatomic1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:33.8861807Z #11 6.250 Selecting previously unselected package libasan8:amd64.
2025-10-01T21:48:33.8862459Z #11 6.251 Preparing to unpack .../30-libasan8_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:33.8863062Z #11 6.252 Unpacking libasan8:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:33.8874592Z #11 6.405 Selecting previously unselected package liblsan0:amd64.
2025-10-01T21:48:34.1153551Z #11 6.407 Preparing to unpack .../31-liblsan0_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:34.1154345Z #11 6.408 Unpacking liblsan0:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:34.1154955Z #11 6.481 Selecting previously unselected package libtsan2:amd64.
2025-10-01T21:48:34.1155633Z #11 6.482 Preparing to unpack .../32-libtsan2_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:34.1156212Z #11 6.483 Unpacking libtsan2:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:34.1156881Z #11 6.633 Selecting previously unselected package libubsan1:amd64.
2025-10-01T21:48:34.3614662Z #11 6.635 Preparing to unpack .../33-libubsan1_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:34.3615864Z #11 6.636 Unpacking libubsan1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:34.3617182Z #11 6.703 Selecting previously unselected package libquadmath0:amd64.
2025-10-01T21:48:34.3617770Z #11 6.705 Preparing to unpack .../34-libquadmath0_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:34.3618259Z #11 6.706 Unpacking libquadmath0:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:34.3618660Z #11 6.727 Selecting previously unselected package libgcc-12-dev:amd64.
2025-10-01T21:48:34.3619209Z #11 6.729 Preparing to unpack .../35-libgcc-12-dev_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:34.3619598Z #11 6.730 Unpacking libgcc-12-dev:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:34.3620033Z #11 6.879 Selecting previously unselected package gcc-12.
2025-10-01T21:48:34.5148379Z #11 6.881 Preparing to unpack .../36-gcc-12_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:34.5149267Z #11 6.882 Unpacking gcc-12 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:35.0067487Z #11 7.524 Selecting previously unselected package gcc.
2025-10-01T21:48:35.1800470Z #11 7.526 Preparing to unpack .../37-gcc_4%3a12.2.0-3_amd64.deb ...
2025-10-01T21:48:35.1801194Z #11 7.527 Unpacking gcc (4:12.2.0-3) ...
2025-10-01T21:48:35.1801767Z #11 7.544 Selecting previously unselected package libstdc++-12-dev:amd64.
2025-10-01T21:48:35.1802388Z #11 7.546 Preparing to unpack .../38-libstdc++-12-dev_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:35.1802928Z #11 7.547 Unpacking libstdc++-12-dev:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:35.2263629Z #11 7.744 Selecting previously unselected package g++-12.
2025-10-01T21:48:35.3800737Z #11 7.746 Preparing to unpack .../39-g++-12_12.2.0-14+deb12u1_amd64.deb ...
2025-10-01T21:48:35.3801293Z #11 7.747 Unpacking g++-12 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:35.7391273Z #11 8.257 Selecting previously unselected package g++.
2025-10-01T21:48:35.8512833Z #11 8.258 Preparing to unpack .../40-g++_4%3a12.2.0-3_amd64.deb ...
2025-10-01T21:48:35.8513489Z #11 8.259 Unpacking g++ (4:12.2.0-3) ...
2025-10-01T21:48:35.8514501Z #11 8.272 Selecting previously unselected package make.
2025-10-01T21:48:35.8515123Z #11 8.273 Preparing to unpack .../41-make_4.3-4.1_amd64.deb ...
2025-10-01T21:48:35.8515465Z #11 8.274 Unpacking make (4.3-4.1) ...
2025-10-01T21:48:35.8515823Z #11 8.314 Selecting previously unselected package libdpkg-perl.
2025-10-01T21:48:35.8516741Z #11 8.315 Preparing to unpack .../42-libdpkg-perl_1.21.22_all.deb ...
2025-10-01T21:48:35.8517130Z #11 8.316 Unpacking libdpkg-perl (1.21.22) ...
2025-10-01T21:48:35.8517550Z #11 8.369 Selecting previously unselected package patch.
2025-10-01T21:48:35.9603120Z #11 8.370 Preparing to unpack .../43-patch_2.7.6-7_amd64.deb ...
2025-10-01T21:48:35.9603925Z #11 8.371 Unpacking patch (2.7.6-7) ...
2025-10-01T21:48:35.9604448Z #11 8.392 Selecting previously unselected package dpkg-dev.
2025-10-01T21:48:35.9605046Z #11 8.393 Preparing to unpack .../44-dpkg-dev_1.21.22_all.deb ...
2025-10-01T21:48:35.9605556Z #11 8.394 Unpacking dpkg-dev (1.21.22) ...
2025-10-01T21:48:35.9606072Z #11 8.478 Selecting previously unselected package build-essential.
2025-10-01T21:48:36.0756218Z #11 8.479 Preparing to unpack .../45-build-essential_12.9_amd64.deb ...
2025-10-01T21:48:36.0757028Z #11 8.480 Unpacking build-essential (12.9) ...
2025-10-01T21:48:36.0757586Z #11 8.495 Selecting previously unselected package libbrotli1:amd64.
2025-10-01T21:48:36.0758257Z #11 8.496 Preparing to unpack .../46-libbrotli1_1.0.9-2+b6_amd64.deb ...
2025-10-01T21:48:36.0758816Z #11 8.497 Unpacking libbrotli1:amd64 (1.0.9-2+b6) ...
2025-10-01T21:48:36.0759408Z #11 8.527 Selecting previously unselected package libsasl2-modules-db:amd64.
2025-10-01T21:48:36.0760137Z #11 8.528 Preparing to unpack .../47-libsasl2-modules-db_2.1.28+dfsg-10_amd64.deb ...
2025-10-01T21:48:36.0760815Z #11 8.529 Unpacking libsasl2-modules-db:amd64 (2.1.28+dfsg-10) ...
2025-10-01T21:48:36.0761418Z #11 8.545 Selecting previously unselected package libsasl2-2:amd64.
2025-10-01T21:48:36.0762059Z #11 8.546 Preparing to unpack .../48-libsasl2-2_2.1.28+dfsg-10_amd64.deb ...
2025-10-01T21:48:36.0762627Z #11 8.547 Unpacking libsasl2-2:amd64 (2.1.28+dfsg-10) ...
2025-10-01T21:48:36.0763500Z #11 8.565 Selecting previously unselected package libldap-2.5-0:amd64.
2025-10-01T21:48:36.0764212Z #11 8.566 Preparing to unpack .../49-libldap-2.5-0_2.5.13+dfsg-5_amd64.deb ...
2025-10-01T21:48:36.0764877Z #11 8.567 Unpacking libldap-2.5-0:amd64 (2.5.13+dfsg-5) ...
2025-10-01T21:48:36.0765546Z #11 8.593 Selecting previously unselected package libnghttp2-14:amd64.
2025-10-01T21:48:36.2035768Z #11 8.595 Preparing to unpack .../50-libnghttp2-14_1.52.0-1+deb12u2_amd64.deb ...
2025-10-01T21:48:36.2036708Z #11 8.596 Unpacking libnghttp2-14:amd64 (1.52.0-1+deb12u2) ...
2025-10-01T21:48:36.2037172Z #11 8.615 Selecting previously unselected package libpsl5:amd64.
2025-10-01T21:48:36.2037565Z #11 8.616 Preparing to unpack .../51-libpsl5_0.21.2-1_amd64.deb ...
2025-10-01T21:48:36.2037904Z #11 8.617 Unpacking libpsl5:amd64 (0.21.2-1) ...
2025-10-01T21:48:36.2038236Z #11 8.635 Selecting previously unselected package librtmp1:amd64.
2025-10-01T21:48:36.2050829Z #11 8.636 Preparing to unpack .../52-librtmp1_2.4+20151223.gitfa8646d.1-2+b2_amd64.deb ...
2025-10-01T21:48:36.2051683Z #11 8.637 Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2+b2) ...
2025-10-01T21:48:36.2052330Z #11 8.655 Selecting previously unselected package libssh2-1:amd64.
2025-10-01T21:48:36.2052950Z #11 8.656 Preparing to unpack .../53-libssh2-1_1.10.0-3+b1_amd64.deb ...
2025-10-01T21:48:36.2053513Z #11 8.657 Unpacking libssh2-1:amd64 (1.10.0-3+b1) ...
2025-10-01T21:48:36.2054117Z #11 8.685 Selecting previously unselected package libcurl3-gnutls:amd64.
2025-10-01T21:48:36.2054830Z #11 8.687 Preparing to unpack .../54-libcurl3-gnutls_7.88.1-10+deb12u14_amd64.deb ...
2025-10-01T21:48:36.2055518Z #11 8.688 Unpacking libcurl3-gnutls:amd64 (7.88.1-10+deb12u14) ...
2025-10-01T21:48:36.2056140Z #11 8.721 Selecting previously unselected package libexpat1:amd64.
2025-10-01T21:48:36.3264973Z #11 8.723 Preparing to unpack .../55-libexpat1_2.5.0-1+deb12u2_amd64.deb ...
2025-10-01T21:48:36.3265967Z #11 8.724 Unpacking libexpat1:amd64 (2.5.0-1+deb12u2) ...
2025-10-01T21:48:36.3266854Z #11 8.743 Selecting previously unselected package liberror-perl.
2025-10-01T21:48:36.3267466Z #11 8.744 Preparing to unpack .../56-liberror-perl_0.17029-2_all.deb ...
2025-10-01T21:48:36.3268252Z #11 8.745 Unpacking liberror-perl (0.17029-2) ...
2025-10-01T21:48:36.3268726Z #11 8.761 Selecting previously unselected package git-man.
2025-10-01T21:48:36.3269285Z #11 8.762 Preparing to unpack .../57-git-man_1%3a2.39.5-0+deb12u2_all.deb ...
2025-10-01T21:48:36.3269802Z #11 8.763 Unpacking git-man (1:2.39.5-0+deb12u2) ...
2025-10-01T21:48:36.3270251Z #11 8.844 Selecting previously unselected package git.
2025-10-01T21:48:36.4845864Z #11 8.846 Preparing to unpack .../58-git_1%3a2.39.5-0+deb12u2_amd64.deb ...
2025-10-01T21:48:36.4847027Z #11 8.852 Unpacking git (1:2.39.5-0+deb12u2) ...
2025-10-01T21:48:36.6413734Z #11 9.159 Setting up libexpat1:amd64 (2.5.0-1+deb12u2) ...
2025-10-01T21:48:36.7423127Z #11 9.161 Setting up libpsl5:amd64 (0.21.2-1) ...
2025-10-01T21:48:36.7423748Z #11 9.164 Setting up libbrotli1:amd64 (1.0.9-2+b6) ...
2025-10-01T21:48:36.7424297Z #11 9.166 Setting up binutils-common:amd64 (2.40-2) ...
2025-10-01T21:48:36.7424872Z #11 9.169 Setting up libnghttp2-14:amd64 (1.52.0-1+deb12u2) ...
2025-10-01T21:48:36.7425472Z #11 9.171 Setting up linux-libc-dev:amd64 (6.1.153-1) ...
2025-10-01T21:48:36.7425997Z #11 9.175 Setting up libctf-nobfd0:amd64 (2.40-2) ...
2025-10-01T21:48:36.7426697Z #11 9.177 Setting up libgomp1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7427182Z #11 9.179 Setting up bzip2 (1.0.8-5+b1) ...
2025-10-01T21:48:36.7427616Z #11 9.181 Setting up libjansson4:amd64 (2.14-2) ...
2025-10-01T21:48:36.7428167Z #11 9.184 Setting up libsasl2-modules-db:amd64 (2.1.28+dfsg-10) ...
2025-10-01T21:48:36.7428761Z #11 9.186 Setting up perl-modules-5.36 (5.36.0-7+deb12u3) ...
2025-10-01T21:48:36.7429129Z #11 9.188 Setting up libtirpc-dev:amd64 (1.3.3+ds-1) ...
2025-10-01T21:48:36.7429440Z #11 9.191 Setting up rpcsvc-proto (1.4.3-1) ...
2025-10-01T21:48:36.7430076Z #11 9.193 Setting up make (4.3-4.1) ...
2025-10-01T21:48:36.7430350Z #11 9.195 Setting up libmpfr6:amd64 (4.2.0-1) ...
2025-10-01T21:48:36.7430766Z #11 9.198 Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2+b2) ...
2025-10-01T21:48:36.7431303Z #11 9.200 Setting up xz-utils (5.4.1-1) ...
2025-10-01T21:48:36.7431958Z #11 9.204 update-alternatives: using /usr/bin/xz to provide /usr/bin/lzma (lzma) in auto mode
2025-10-01T21:48:36.7432903Z #11 9.204 update-alternatives: warning: skip creation of /usr/share/man/man1/lzma.1.gz because associated file /usr/share/man/man1/xz.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7434523Z #11 9.205 update-alternatives: warning: skip creation of /usr/share/man/man1/unlzma.1.gz because associated file /usr/share/man/man1/unxz.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7436079Z #11 9.205 update-alternatives: warning: skip creation of /usr/share/man/man1/lzcat.1.gz because associated file /usr/share/man/man1/xzcat.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7437574Z #11 9.205 update-alternatives: warning: skip creation of /usr/share/man/man1/lzmore.1.gz because associated file /usr/share/man/man1/xzmore.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7439124Z #11 9.205 update-alternatives: warning: skip creation of /usr/share/man/man1/lzless.1.gz because associated file /usr/share/man/man1/xzless.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7440469Z #11 9.206 update-alternatives: warning: skip creation of /usr/share/man/man1/lzdiff.1.gz because associated file /usr/share/man/man1/xzdiff.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7442220Z #11 9.206 update-alternatives: warning: skip creation of /usr/share/man/man1/lzcmp.1.gz because associated file /usr/share/man/man1/xzcmp.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7444105Z #11 9.206 update-alternatives: warning: skip creation of /usr/share/man/man1/lzgrep.1.gz because associated file /usr/share/man/man1/xzgrep.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7447287Z #11 9.206 update-alternatives: warning: skip creation of /usr/share/man/man1/lzegrep.1.gz because associated file /usr/share/man/man1/xzegrep.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7449100Z #11 9.206 update-alternatives: warning: skip creation of /usr/share/man/man1/lzfgrep.1.gz because associated file /usr/share/man/man1/xzfgrep.1.gz (of link group lzma) doesn't exist
2025-10-01T21:48:36.7450033Z #11 9.209 Setting up libquadmath0:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7450350Z #11 9.211 Setting up libmpc3:amd64 (1.3.1-1) ...
2025-10-01T21:48:36.7450643Z #11 9.214 Setting up libatomic1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7450930Z #11 9.216 Setting up patch (2.7.6-7) ...
2025-10-01T21:48:36.7451209Z #11 9.218 Setting up libgdbm-compat4:amd64 (1.23-3) ...
2025-10-01T21:48:36.7451509Z #11 9.221 Setting up libsasl2-2:amd64 (2.1.28+dfsg-10) ...
2025-10-01T21:48:36.7452053Z #11 9.223 Setting up libubsan1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7452398Z #11 9.225 Setting up libnsl-dev:amd64 (1.3.0-2) ...
2025-10-01T21:48:36.7452689Z #11 9.227 Setting up libcrypt-dev:amd64 (1:4.4.33-2) ...
2025-10-01T21:48:36.7453102Z #11 9.234 Setting up libasan8:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7453399Z #11 9.237 Setting up git-man (1:2.39.5-0+deb12u2) ...
2025-10-01T21:48:36.7453782Z #11 9.240 Setting up libssh2-1:amd64 (1.10.0-3+b1) ...
2025-10-01T21:48:36.7454170Z #11 9.242 Setting up libtsan2:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7454460Z #11 9.244 Setting up libbinutils:amd64 (2.40-2) ...
2025-10-01T21:48:36.7454725Z #11 9.246 Setting up libisl23:amd64 (0.25-1.1) ...
2025-10-01T21:48:36.7455005Z #11 9.249 Setting up libc-dev-bin (2.36-9+deb12u13) ...
2025-10-01T21:48:36.7455390Z #11 9.251 Setting up libcc1-0:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7455696Z #11 9.253 Setting up libperl5.36:amd64 (5.36.0-7+deb12u3) ...
2025-10-01T21:48:36.7456609Z #11 9.255 Setting up liblsan0:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7456914Z #11 9.258 Setting up libitm1:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.7457194Z #11 9.260 Setting up libctf0:amd64 (2.40-2) ...
2025-10-01T21:48:36.9679088Z #11 9.263 Setting up cpp-12 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.9679674Z #11 9.265 Setting up libldap-2.5-0:amd64 (2.5.13+dfsg-5) ...
2025-10-01T21:48:36.9680201Z #11 9.267 Setting up perl (5.36.0-7+deb12u3) ...
2025-10-01T21:48:36.9680567Z #11 9.276 Setting up libgprofng0:amd64 (2.40-2) ...
2025-10-01T21:48:36.9680938Z #11 9.278 Setting up libgcc-12-dev:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.9681293Z #11 9.280 Setting up libdpkg-perl (1.21.22) ...
2025-10-01T21:48:36.9681593Z #11 9.283 Setting up cpp (4:12.2.0-3) ...
2025-10-01T21:48:36.9681906Z #11 9.288 Setting up libc6-dev:amd64 (2.36-9+deb12u13) ...
2025-10-01T21:48:36.9682263Z #11 9.290 Setting up binutils-x86-64-linux-gnu (2.40-2) ...
2025-10-01T21:48:36.9682649Z #11 9.292 Setting up libstdc++-12-dev:amd64 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.9683052Z #11 9.295 Setting up libcurl3-gnutls:amd64 (7.88.1-10+deb12u14) ...
2025-10-01T21:48:36.9683395Z #11 9.297 Setting up binutils (2.40-2) ...
2025-10-01T21:48:36.9683674Z #11 9.300 Setting up dpkg-dev (1.21.22) ...
2025-10-01T21:48:36.9683979Z #11 9.303 Setting up liberror-perl (0.17029-2) ...
2025-10-01T21:48:36.9684295Z #11 9.306 Setting up gcc-12 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.9684592Z #11 9.308 Setting up git (1:2.39.5-0+deb12u2) ...
2025-10-01T21:48:36.9684898Z #11 9.315 Setting up g++-12 (12.2.0-14+deb12u1) ...
2025-10-01T21:48:36.9685178Z #11 9.318 Setting up gcc (4:12.2.0-3) ...
2025-10-01T21:48:36.9685441Z #11 9.326 Setting up g++ (4:12.2.0-3) ...
2025-10-01T21:48:36.9685859Z #11 9.329 update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
2025-10-01T21:48:36.9686539Z #11 9.332 Setting up build-essential (12.9) ...
2025-10-01T21:48:36.9687051Z #11 9.335 Processing triggers for libc-bin (2.36-9+deb12u13) ...
2025-10-01T21:48:37.4263114Z #11 DONE 9.9s
2025-10-01T21:48:37.6310095Z 
2025-10-01T21:48:37.6310583Z #12 [builder 2/3] COPY requirements.txt /app/requirements.txt
2025-10-01T21:48:37.6311691Z #12 DONE 0.1s
2025-10-01T21:48:37.6311885Z 
2025-10-01T21:48:37.6312555Z #13 [builder 3/3] RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
2025-10-01T21:48:38.7583201Z #13 1.278 Collecting click==8.1.7 (from -r requirements.txt (line 2))
2025-10-01T21:48:38.8716974Z #13 1.334   Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
2025-10-01T21:48:38.8717836Z #13 1.391 Collecting pyyaml==6.0.2 (from -r requirements.txt (line 3))
2025-10-01T21:48:38.9805529Z #13 1.426   Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
2025-10-01T21:48:38.9806883Z #13 1.489 Collecting pytest>=8.0.0 (from -r requirements.txt (line 6))
2025-10-01T21:48:38.9807646Z #13 1.500   Downloading pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
2025-10-01T21:48:39.1663721Z #13 1.686 Collecting setuptools>=78.1.1 (from -r requirements.txt (line 9))
2025-10-01T21:48:39.2881152Z #13 1.698   Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
2025-10-01T21:48:39.2882105Z #13 1.729 Collecting iniconfig>=1 (from pytest>=8.0.0->-r requirements.txt (line 6))
2025-10-01T21:48:39.2882999Z #13 1.740   Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
2025-10-01T21:48:39.2883862Z #13 1.770 Collecting packaging>=20 (from pytest>=8.0.0->-r requirements.txt (line 6))
2025-10-01T21:48:39.2884745Z #13 1.782   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-10-01T21:48:39.2885421Z #13 1.808 Collecting pluggy<2,>=1.5 (from pytest>=8.0.0->-r requirements.txt (line 6))
2025-10-01T21:48:39.4099492Z #13 1.819   Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
2025-10-01T21:48:39.4100889Z #13 1.852 Collecting pygments>=2.7.2 (from pytest>=8.0.0->-r requirements.txt (line 6))
2025-10-01T21:48:39.4101884Z #13 1.863   Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
2025-10-01T21:48:39.4103066Z #13 1.930 Downloading click-8.1.7-py3-none-any.whl (97 kB)
2025-10-01T21:48:39.5198560Z #13 1.944    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 7.2 MB/s eta 0:00:00
2025-10-01T21:48:39.5199453Z #13 1.956 Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (762 kB)
2025-10-01T21:48:39.5200465Z #13 1.978    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 763.0/763.0 kB 37.3 MB/s eta 0:00:00
2025-10-01T21:48:39.5201082Z #13 1.989 Downloading pytest-8.4.2-py3-none-any.whl (365 kB)
2025-10-01T21:48:39.5201834Z #13 1.992    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 365.8/365.8 kB 294.8 MB/s eta 0:00:00
2025-10-01T21:48:39.5202390Z #13 2.004 Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)
2025-10-01T21:48:39.5203121Z #13 2.017    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 110.2 MB/s eta 0:00:00
2025-10-01T21:48:39.5203704Z #13 2.028 Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
2025-10-01T21:48:39.5204347Z #13 2.039 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-10-01T21:48:39.6433319Z #13 2.042    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 kB 152.2 MB/s eta 0:00:00
2025-10-01T21:48:39.6436926Z #13 2.053 Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
2025-10-01T21:48:39.6437626Z #13 2.066 Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
2025-10-01T21:48:39.6438382Z #13 2.072    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 263.3 MB/s eta 0:00:00
2025-10-01T21:48:39.6439091Z #13 2.163 Installing collected packages: setuptools, pyyaml, pygments, pluggy, packaging, iniconfig, click, pytest
2025-10-01T21:48:39.8809663Z #13 2.163   Attempting uninstall: setuptools
2025-10-01T21:48:39.8810236Z #13 2.166     Found existing installation: setuptools 65.5.1
2025-10-01T21:48:39.8810801Z #13 2.183     Uninstalling setuptools-65.5.1:
2025-10-01T21:48:39.8811330Z #13 2.250       Successfully uninstalled setuptools-65.5.1
2025-10-01T21:48:41.2129623Z #13 3.732 Successfully installed click-8.1.7 iniconfig-2.1.0 packaging-25.0 pluggy-1.6.0 pygments-2.19.2 pytest-8.4.2 pyyaml-6.0.2 setuptools-80.9.0
2025-10-01T21:48:41.3470004Z #13 3.732 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
2025-10-01T21:48:41.3471974Z #13 3.867 
2025-10-01T21:48:41.3472505Z #13 3.867 [notice] A new release of pip is available: 24.0 -> 25.2
2025-10-01T21:48:41.3473238Z #13 3.867 [notice] To update, run: pip install --upgrade pip
2025-10-01T21:48:41.4607540Z #13 DONE 4.0s
2025-10-01T21:48:41.7754202Z 
2025-10-01T21:48:41.7754730Z #14 [runtime 1/9] COPY --from=builder /install /usr/local
2025-10-01T21:48:42.0488116Z #14 DONE 0.3s
2025-10-01T21:48:42.1553252Z 
2025-10-01T21:48:42.1553657Z #15 [runtime 2/9] COPY src /app/src
2025-10-01T21:48:42.1554076Z #15 DONE 0.0s
2025-10-01T21:48:42.1554255Z 
2025-10-01T21:48:42.1554454Z #16 [runtime 3/9] COPY scripts /app/scripts
2025-10-01T21:48:42.1554806Z #16 DONE 0.0s
2025-10-01T21:48:42.1554913Z 
2025-10-01T21:48:42.1555069Z #17 [runtime 4/9] COPY docker/start.sh /app/scripts/start.sh
2025-10-01T21:48:42.1555540Z #17 DONE 0.0s
2025-10-01T21:48:42.1555861Z 
2025-10-01T21:48:42.1556177Z #18 [runtime 5/9] COPY scripts/healthcheck.py /app/scripts/healthcheck.py
2025-10-01T21:48:42.1558267Z #18 DONE 0.0s
2025-10-01T21:48:42.1558469Z 
2025-10-01T21:48:42.1558673Z #19 [runtime 6/9] RUN chmod +x /app/scripts/start.sh
2025-10-01T21:48:42.1559125Z #19 DONE 0.0s
2025-10-01T21:48:42.2704211Z 
2025-10-01T21:48:42.2704918Z #20 [runtime 7/9] RUN chmod +x /app/scripts/healthcheck.py
2025-10-01T21:48:42.2705509Z #20 DONE 0.0s
2025-10-01T21:48:42.2705691Z 
2025-10-01T21:48:42.2706171Z #21 [runtime 8/9] RUN groupadd --system appuser && useradd --system --gid appuser --create-home appuser
2025-10-01T21:48:42.2707107Z #21 DONE 0.1s
2025-10-01T21:48:42.4817381Z 
2025-10-01T21:48:42.4817842Z #22 [runtime 9/9] RUN chown -R appuser:appuser /app
2025-10-01T21:48:42.4818661Z #22 DONE 0.1s
2025-10-01T21:48:42.4818932Z 
2025-10-01T21:48:42.4819291Z #23 exporting to docker image format
2025-10-01T21:48:42.4819685Z #23 exporting layers
2025-10-01T21:48:43.2528470Z #23 exporting layers 0.9s done
2025-10-01T21:48:43.4100914Z #23 exporting manifest sha256:c83a96e5f264ee07dddc81ba7f4d6648460754bd2c817ecb4a28b3327465f043 done
2025-10-01T21:48:43.4102244Z #23 exporting config sha256:5bd69d849c130281d4cff85531fe696f489d6ba8a99181a856f10714347f2141 done
2025-10-01T21:48:43.4110653Z #23 sending tarball
2025-10-01T21:48:46.1688540Z #23 sending tarball 2.9s done
2025-10-01T21:48:46.1689007Z #23 DONE 3.8s
2025-10-01T21:48:46.1689190Z 
2025-10-01T21:48:46.1689335Z #24 importing to docker
2025-10-01T21:48:46.1689788Z #24 loading layer aca836066730 28.23MB / 28.23MB 2.6s done
2025-10-01T21:48:46.1690375Z #24 loading layer b3a19b5ba963 3.52MB / 3.52MB 1.6s done
2025-10-01T21:48:46.1690930Z #24 loading layer 933d50692269 16.21MB / 16.21MB 1.4s done
2025-10-01T21:48:46.1691470Z #24 loading layer ac1568d6117b 248B / 248B 0.7s done
2025-10-01T21:48:46.1691834Z #24 loading layer 02492764898a 93B / 93B 0.7s done
2025-10-01T21:48:46.1692382Z #24 loading layer 51810e28921c 7.97MB / 7.97MB 0.7s done
2025-10-01T21:48:46.1692775Z #24 loading layer 77377fe9e8fb 189B / 189B 0.1s done
2025-10-01T21:48:46.1693167Z #24 loading layer 8b8c0e688d0b 8.15kB / 8.15kB 0.1s done
2025-10-01T21:48:46.1693677Z #24 loading layer da114cc3e5e5 209B / 209B 0.1s done
2025-10-01T21:48:46.1694192Z #24 loading layer 5f70bf18a086 32B / 32B 0.1s done
2025-10-01T21:48:46.1694491Z #24 loading layer 83f610bb422a 205B / 205B 0.0s done
2025-10-01T21:48:46.1694771Z #24 loading layer 2c907a77ddd7 319B / 319B 0.0s done
2025-10-01T21:48:46.1695247Z #24 loading layer b749a2a9aed1 3.22kB / 3.22kB 0.0s done
2025-10-01T21:48:46.1695764Z #24 loading layer 8133fdb4dfc0 8.32kB / 8.32kB 0.0s done
2025-10-01T21:48:46.1696169Z #24 DONE 2.6s
2025-10-01T21:48:46.1696554Z 
2025-10-01T21:48:46.1696744Z #25 resolving provenance for metadata file
2025-10-01T21:48:46.1697156Z #25 DONE 0.0s
2025-10-01T21:48:46.1765102Z ##[group]ImageID
2025-10-01T21:48:46.1765741Z sha256:5bd69d849c130281d4cff85531fe696f489d6ba8a99181a856f10714347f2141
2025-10-01T21:48:46.1767485Z ##[endgroup]
2025-10-01T21:48:46.1768041Z ##[group]Digest
2025-10-01T21:48:46.1768576Z sha256:c83a96e5f264ee07dddc81ba7f4d6648460754bd2c817ecb4a28b3327465f043
2025-10-01T21:48:46.1769454Z ##[endgroup]
2025-10-01T21:48:46.1769978Z ##[group]Metadata
2025-10-01T21:48:46.1770452Z {
2025-10-01T21:48:46.1770795Z   "buildx.build.provenance": {
2025-10-01T21:48:46.1771169Z     "builder": {
2025-10-01T21:48:46.1771449Z       "id": ""
2025-10-01T21:48:46.1771684Z     },
2025-10-01T21:48:46.1772062Z     "buildType": "https://mobyproject.org/buildkit@v1",
2025-10-01T21:48:46.1772542Z     "materials": [
2025-10-01T21:48:46.1772823Z       {
2025-10-01T21:48:46.1773115Z         "uri": "pkg:docker/docker/dockerfile@1.5",
2025-10-01T21:48:46.1773529Z         "digest": {
2025-10-01T21:48:46.1774039Z           "sha256": "39b85bbfa7536a5feceb7372a0817649ecb2724562a38360f4d6a7782a409b14"
2025-10-01T21:48:46.1774627Z         }
2025-10-01T21:48:46.1774877Z       },
2025-10-01T21:48:46.1775097Z       {
2025-10-01T21:48:46.1775374Z         "uri": "pkg:docker/python@3.11-slim-bookworm?platform=linux%2Famd64",
2025-10-01T21:48:46.1775703Z         "digest": {
2025-10-01T21:48:46.1776009Z           "sha256": "86adf8dbadc3d6e82ee5dd2c74bec2e1c2467cdad47886280501df722372d2e1"
2025-10-01T21:48:46.1776663Z         }
2025-10-01T21:48:46.1776819Z       }
2025-10-01T21:48:46.1776956Z     ],
2025-10-01T21:48:46.1777112Z     "invocation": {
2025-10-01T21:48:46.1777289Z       "configSource": {},
2025-10-01T21:48:46.1777491Z       "parameters": {
2025-10-01T21:48:46.1777688Z         "frontend": "gateway.v0",
2025-10-01T21:48:46.1777889Z         "args": {
2025-10-01T21:48:46.1778082Z           "cmdline": "docker/dockerfile:1.5",
2025-10-01T21:48:46.1778331Z           "source": "docker/dockerfile:1.5"
2025-10-01T21:48:46.1778807Z         },
2025-10-01T21:48:46.1778952Z         "locals": [
2025-10-01T21:48:46.1779114Z           {
2025-10-01T21:48:46.1779266Z             "name": "context"
2025-10-01T21:48:46.1779458Z           },
2025-10-01T21:48:46.1779608Z           {
2025-10-01T21:48:46.1779767Z             "name": "dockerfile"
2025-10-01T21:48:46.1779958Z           }
2025-10-01T21:48:46.1780101Z         ]
2025-10-01T21:48:46.1780246Z       },
2025-10-01T21:48:46.1780396Z       "environment": {
2025-10-01T21:48:46.1780590Z         "platform": "linux/amd64"
2025-10-01T21:48:46.1780789Z       }
2025-10-01T21:48:46.1780934Z     }
2025-10-01T21:48:46.1781069Z   },
2025-10-01T21:48:46.1781566Z   "buildx.build.ref": "builder-54d1668b-0a40-40ea-89c4-8b5572363844/builder-54d1668b-0a40-40ea-89c4-8b55723638440/kc7npxi8b0yb16tq70wamxril",
2025-10-01T21:48:46.1782340Z   "containerimage.config.digest": "sha256:5bd69d849c130281d4cff85531fe696f489d6ba8a99181a856f10714347f2141",
2025-10-01T21:48:46.1782800Z   "containerimage.descriptor": {
2025-10-01T21:48:46.1783147Z     "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
2025-10-01T21:48:46.1783625Z     "digest": "sha256:c83a96e5f264ee07dddc81ba7f4d6648460754bd2c817ecb4a28b3327465f043",
2025-10-01T21:48:46.1783988Z     "size": 3040,
2025-10-01T21:48:46.1784154Z     "annotations": {
2025-10-01T21:48:46.1784404Z       "org.opencontainers.image.created": "2025-10-01T21:48:43Z"
2025-10-01T21:48:46.1784677Z     },
2025-10-01T21:48:46.1784831Z     "platform": {
2025-10-01T21:48:46.1785006Z       "architecture": "amd64",
2025-10-01T21:48:46.1785200Z       "os": "linux"
2025-10-01T21:48:46.1785353Z     }
2025-10-01T21:48:46.1785491Z   },
2025-10-01T21:48:46.1785838Z   "containerimage.digest": "sha256:c83a96e5f264ee07dddc81ba7f4d6648460754bd2c817ecb4a28b3327465f043",
2025-10-01T21:48:46.1786473Z   "image.name": "ghcr.io/example/phase0:latest"
2025-10-01T21:48:46.1786897Z }
2025-10-01T21:48:46.1787481Z ##[endgroup]
2025-10-01T21:48:46.1876485Z ##[group]Run anchore/sbom-action@v0
2025-10-01T21:48:46.1876920Z with:
2025-10-01T21:48:46.1877192Z   image: ghcr.io/example/phase0:latest
2025-10-01T21:48:46.1877449Z   format: cyclonedx-json
2025-10-01T21:48:46.1877661Z   output-file: sbom-phase0.json
2025-10-01T21:48:46.1877876Z   path: .
2025-10-01T21:48:46.1878187Z   github-token: ***
2025-10-01T21:48:46.1878394Z   dependency-snapshot: false
2025-10-01T21:48:46.1878617Z   upload-artifact: true
2025-10-01T21:48:46.1878825Z   upload-artifact-retention: 0
2025-10-01T21:48:46.1879053Z   upload-release-assets: true
2025-10-01T21:48:46.1879257Z ##[endgroup]
2025-10-01T21:48:46.3937111Z ------------------------------ Running SBOM Action -----------------------------
2025-10-01T21:48:46.4790185Z [command]/usr/bin/sh /home/runner/work/_temp/d8638ef0-1807-4e4b-9958-26a56191623d -d -b /home/runner/work/_temp/d8638ef0-1807-4e4b-9958-26a56191623d_syft v1.33.0
2025-10-01T21:48:46.4839143Z [info] checking github for release tag='v1.33.0' 
2025-10-01T21:48:46.4878077Z [debug] http_download(url=https://github.com/anchore/syft/releases/v1.33.0) 
2025-10-01T21:48:46.7602749Z [info] fetching release script for tag='v1.33.0' 
2025-10-01T21:48:46.7628018Z [debug] http_download(url=https://get.anchore.io/syft/v1.33.0/install.sh) 
2025-10-01T21:48:47.2010330Z [info] checking github for release tag='v1.33.0' 
2025-10-01T21:48:47.2046703Z [debug] http_download(url=https://github.com/anchore/syft/releases/v1.33.0) 
2025-10-01T21:48:47.3115772Z [info] using release tag='v1.33.0' version='1.33.0' os='linux' arch='amd64' 
2025-10-01T21:48:47.3138258Z [debug] downloading files into /tmp/tmp.9veCyxJz52 
2025-10-01T21:48:47.3176569Z [debug] http_download(url=https://github.com/anchore/syft/releases/download/v1.33.0/syft_1.33.0_checksums.txt) 
2025-10-01T21:48:47.4759688Z [debug] http_download(url=https://github.com/anchore/syft/releases/download/v1.33.0/syft_1.33.0_linux_amd64.tar.gz) 
2025-10-01T21:48:48.3472019Z [info] installed /home/runner/work/_temp/d8638ef0-1807-4e4b-9958-26a56191623d_syft/syft 
2025-10-01T21:48:48.4217638Z [command]/opt/hostedtoolcache/syft/1.33.0/x64/syft scan ghcr.io/example/phase0:latest -o cyclonedx-json
2025-10-01T21:48:48.4219136Z ##[group]Executing Syft...
2025-10-01T21:48:51.7610301Z ##[endgroup]
2025-10-01T21:48:51.7610623Z SBOM scan completed in: 5.365s
2025-10-01T21:48:51.7732283Z ------------------------- Uploading workflow artifacts -------------------------
2025-10-01T21:48:51.7733073Z /tmp/sbom-action-mp2uIz/example-phase0_latest.cyclonedx.json
2025-10-01T21:48:52.5319375Z ##[group]Run aquasecurity/trivy-action@0.24.0
2025-10-01T21:48:52.5319667Z with:
2025-10-01T21:48:52.5319873Z   image-ref: ghcr.io/example/phase0:latest
2025-10-01T21:48:52.5320143Z   severity: HIGH,CRITICAL
2025-10-01T21:48:52.5320364Z   exit-code: 1
2025-10-01T21:48:52.5320543Z   scan-type: image
2025-10-01T21:48:52.5320719Z   format: json
2025-10-01T21:48:52.5320905Z   output: trivy-report.json
2025-10-01T21:48:52.5321115Z   scan-ref: .
2025-10-01T21:48:52.5321289Z   ignore-unfixed: false
2025-10-01T21:48:52.5321503Z   vuln-type: os,library
2025-10-01T21:48:52.5321704Z   list-all-pkgs: false
2025-10-01T21:48:52.5321888Z env:
2025-10-01T21:48:52.5322165Z   ANCHORE_SBOM_ACTION_PRIOR_ARTIFACT: example-phase0_latest.cyclonedx.json
2025-10-01T21:48:52.5322514Z ##[endgroup]
2025-10-01T21:48:52.5455701Z ##[command]/usr/bin/docker run --name b2e41d9d5bea7102e54c1cb0feb61344069cd4_358dce --label b2e41d --workdir /github/workspace --rm -e "ANCHORE_SBOM_ACTION_PRIOR_ARTIFACT" -e "INPUT_IMAGE-REF" -e "INPUT_SEVERITY" -e "INPUT_EXIT-CODE" -e "INPUT_SCAN-TYPE" -e "INPUT_FORMAT" -e "INPUT_OUTPUT" -e "INPUT_INPUT" -e "INPUT_SCAN-REF" -e "INPUT_IGNORE-UNFIXED" -e "INPUT_VULN-TYPE" -e "INPUT_TEMPLATE" -e "INPUT_SKIP-DIRS" -e "INPUT_SKIP-FILES" -e "INPUT_CACHE-DIR" -e "INPUT_TIMEOUT" -e "INPUT_IGNORE-POLICY" -e "INPUT_HIDE-PROGRESS" -e "INPUT_LIST-ALL-PKGS" -e "INPUT_SCANNERS" -e "INPUT_TRIVYIGNORES" -e "INPUT_ARTIFACT-TYPE" -e "INPUT_GITHUB-PAT" -e "INPUT_TRIVY-CONFIG" -e "INPUT_TF-VARS" -e "INPUT_LIMIT-SEVERITIES-FOR-SARIF" -e "INPUT_DOCKER-HOST" -e "HOME" -e "GITHUB_JOB" -e "GITHUB_REF" -e "GITHUB_SHA" -e "GITHUB_REPOSITORY" -e "GITHUB_REPOSITORY_OWNER" -e "GITHUB_REPOSITORY_OWNER_ID" -e "GITHUB_RUN_ID" -e "GITHUB_RUN_NUMBER" -e "GITHUB_RETENTION_DAYS" -e "GITHUB_RUN_ATTEMPT" -e "GITHUB_ACTOR_ID" -e "GITHUB_ACTOR" -e "GITHUB_WORKFLOW" -e "GITHUB_HEAD_REF" -e "GITHUB_BASE_REF" -e "GITHUB_EVENT_NAME" -e "GITHUB_SERVER_URL" -e "GITHUB_API_URL" -e "GITHUB_GRAPHQL_URL" -e "GITHUB_REF_NAME" -e "GITHUB_REF_PROTECTED" -e "GITHUB_REF_TYPE" -e "GITHUB_WORKFLOW_REF" -e "GITHUB_WORKFLOW_SHA" -e "GITHUB_REPOSITORY_ID" -e "GITHUB_TRIGGERING_ACTOR" -e "GITHUB_WORKSPACE" -e "GITHUB_ACTION" -e "GITHUB_EVENT_PATH" -e "GITHUB_ACTION_REPOSITORY" -e "GITHUB_ACTION_REF" -e "GITHUB_PATH" -e "GITHUB_ENV" -e "GITHUB_STEP_SUMMARY" -e "GITHUB_STATE" -e "GITHUB_OUTPUT" -e "RUNNER_OS" -e "RUNNER_ARCH" -e "RUNNER_NAME" -e "RUNNER_ENVIRONMENT" -e "RUNNER_TOOL_CACHE" -e "RUNNER_TEMP" -e "RUNNER_WORKSPACE" -e "ACTIONS_RUNTIME_URL" -e "ACTIONS_RUNTIME_TOKEN" -e "ACTIONS_CACHE_URL" -e "ACTIONS_RESULTS_URL" -e GITHUB_ACTIONS=true -e CI=true -v "/var/run/docker.sock":"/var/run/docker.sock" -v "/home/runner/work/_temp/_github_home":"/github/home" -v "/home/runner/work/_temp/_github_workflow":"/github/workflow" -v "/home/runner/work/_temp/_runner_file_commands":"/github/file_commands" -v "/home/runner/work/N_grade/N_grade":"/github/workspace" b2e41d:9d5bea7102e54c1cb0feb61344069cd4  "-a image" "-b json" "-c " "-d 1" "-e false" "-f os,library" "-g HIGH,CRITICAL" "-h trivy-report.json" "-i ghcr.io/example/phase0:latest" "-j ." "-k " "-l " "-m " "-n " "-o " "-p " "-q " "-r false" "-s " "-t " "-u " "-v " "-x " "-z " "-y "
2025-10-01T21:48:52.6874072Z Running trivy with options: trivy image  --format json --exit-code  1 --vuln-type  os,library --severity  HIGH,CRITICAL --output  trivy-report.json  ghcr.io/example/phase0:latest
2025-10-01T21:48:52.6874790Z Global options:  
2025-10-01T21:48:53.1240255Z 2025-10-01T21:48:53Z	INFO	Need to update DB
2025-10-01T21:48:53.1241593Z 2025-10-01T21:48:53Z	INFO	Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
2025-10-01T21:48:55.9829016Z 24.05 MiB / 71.77 MiB [-------------------->________________________________________] 33.51% ? p/s ?58.89 MiB / 71.77 MiB [-------------------------------------------------->__________] 82.05% ? p/s ?71.77 MiB / 71.77 MiB [----------------------------------------------------------->] 100.00% ? p/s ?71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 79.52 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 79.52 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 79.52 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 74.39 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 74.39 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 74.39 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 69.59 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 69.59 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [---------------------------------------------->] 100.00% 69.59 MiB p/s ETA 0s71.77 MiB / 71.77 MiB [-------------------------------------------------] 100.00% 30.68 MiB p/s 2.5s2025-10-01T21:48:55Z	INFO	Vulnerability scanning is enabled
2025-10-01T21:48:55.9832954Z 2025-10-01T21:48:55Z	INFO	Secret scanning is enabled
2025-10-01T21:48:55.9833786Z 2025-10-01T21:48:55Z	INFO	If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-10-01T21:48:55.9834847Z 2025-10-01T21:48:55Z	INFO	Please see also https://aquasecurity.github.io/trivy/v0.53/docs/scanner/secret#recommendation for faster secret detection
2025-10-01T21:48:59.2365783Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="pip" version="24.0"
2025-10-01T21:48:59.2394857Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="PyYAML" version="6.0.2"
2025-10-01T21:48:59.2396532Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="click" version="8.1.7"
2025-10-01T21:48:59.2398040Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="pluggy" version="1.6.0"
2025-10-01T21:48:59.2399548Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="Pygments" version="2.19.2"
2025-10-01T21:48:59.2401015Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="pytest" version="8.4.2"
2025-10-01T21:48:59.2402480Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="autocommand" version="2.2.2"
2025-10-01T21:48:59.2429867Z 2025-10-01T21:48:59Z	INFO	[python] License acquired from METADATA classifiers may be subject to additional terms	name="typeguard" version="4.3.0"
2025-10-01T21:48:59.3128140Z 2025-10-01T21:48:59Z	INFO	Detected OS	family="debian" version="12.12"
2025-10-01T21:48:59.3128695Z 2025-10-01T21:48:59Z	INFO	[debian] Detecting vulnerabilities...	os_version="12" pkg_num=105
2025-10-01T21:48:59.3228902Z 2025-10-01T21:48:59Z	INFO	Number of language-specific files	num=1
2025-10-01T21:48:59.3229534Z 2025-10-01T21:48:59Z	INFO	[python-pkg] Detecting vulnerabilities...
2025-10-01T21:48:59.3240533Z 2025-10-01T21:48:59Z	WARN	Using severities from other vendors for some vulnerabilities. Read https://aquasecurity.github.io/trivy/v0.53/docs/scanner/vulnerability#severity-selection for details.
2025-10-01T21:48:59.4330968Z ##[group]Run actions/upload-artifact@v4
2025-10-01T21:48:59.4331247Z with:
2025-10-01T21:48:59.4331424Z   name: security-scan-report
2025-10-01T21:48:59.4331789Z   path: trivy-report.json
sbom-phase0.json

2025-10-01T21:48:59.4332311Z   if-no-files-found: warn
2025-10-01T21:48:59.4332609Z   compression-level: 6
2025-10-01T21:48:59.4332972Z   overwrite: false
2025-10-01T21:48:59.4333302Z   include-hidden-files: false
2025-10-01T21:48:59.4333570Z env:
2025-10-01T21:48:59.4333990Z   ANCHORE_SBOM_ACTION_PRIOR_ARTIFACT: example-phase0_latest.cyclonedx.json
2025-10-01T21:48:59.4334409Z ##[endgroup]
2025-10-01T21:48:59.6471109Z Multiple search paths detected. Calculating the least common ancestor of all paths
2025-10-01T21:48:59.6497581Z The least common ancestor is /home/runner/work/N_grade/N_grade. This will be the root directory of the artifact
2025-10-01T21:48:59.6498531Z With the provided path, there will be 2 files uploaded
2025-10-01T21:48:59.6499315Z Artifact name is valid!
2025-10-01T21:48:59.6499784Z Root directory input is valid!
2025-10-01T21:48:59.8029120Z Beginning upload of artifact content to blob storage
2025-10-01T21:49:00.1355040Z Uploaded bytes 303420
2025-10-01T21:49:00.1783949Z Finished uploading artifact content to blob storage!
2025-10-01T21:49:00.1787636Z SHA256 digest of uploaded artifact zip is 415271ac6c995da3da3348787ca71cb14404f80771867dc5e20641210263aa76
2025-10-01T21:49:00.1790230Z Finalizing artifact upload
2025-10-01T21:49:00.2766708Z Artifact security-scan-report.zip successfully finalized. Artifact ID 4159484344
2025-10-01T21:49:00.2768002Z Artifact security-scan-report has been successfully uploaded! Final size is 303420 bytes. Artifact ID is 4159484344
2025-10-01T21:49:00.2774743Z Artifact download URL: https://github.com/Baragji/N_grade/actions/runs/18176579945/artifacts/4159484344
2025-10-01T21:49:00.2893830Z Post job cleanup.
2025-10-01T21:49:00.5032225Z ##[group]Removing temp folder /home/runner/work/_temp/docker-actions-toolkit-qmXfnc
2025-10-01T21:49:00.5045018Z ##[endgroup]
2025-10-01T21:49:00.5045829Z ##[group]Post cache
2025-10-01T21:49:00.5048187Z State not set
2025-10-01T21:49:00.5048756Z ##[endgroup]
2025-10-01T21:49:00.5165992Z Post job cleanup.
2025-10-01T21:49:00.8124760Z [command]/usr/bin/docker logout ghcr.io
2025-10-01T21:49:00.8255347Z Removing login credentials for ghcr.io
2025-10-01T21:49:00.8288416Z ##[group]Post cache
2025-10-01T21:49:00.8290155Z State not set
2025-10-01T21:49:00.8291513Z ##[endgroup]
2025-10-01T21:49:00.8417302Z Post job cleanup.
2025-10-01T21:49:01.1141465Z ##[group]Removing builder
2025-10-01T21:49:01.2255583Z [command]/usr/bin/docker buildx rm builder-54d1668b-0a40-40ea-89c4-8b5572363844
2025-10-01T21:49:01.8620494Z builder-54d1668b-0a40-40ea-89c4-8b5572363844 removed
2025-10-01T21:49:01.8659041Z ##[endgroup]
2025-10-01T21:49:01.8664530Z ##[group]Cleaning up certificates
2025-10-01T21:49:01.8668660Z ##[endgroup]
2025-10-01T21:49:01.8669313Z ##[group]Post cache
2025-10-01T21:49:01.8671641Z State not set
2025-10-01T21:49:01.8672292Z ##[endgroup]
2025-10-01T21:49:01.8820407Z Post job cleanup.
2025-10-01T21:49:01.9750435Z [command]/usr/bin/git version
2025-10-01T21:49:01.9786796Z git version 2.51.0
2025-10-01T21:49:01.9829831Z Temporarily overriding HOME='/home/runner/work/_temp/05751637-bf6d-4c46-8a0e-063e81aa14d7' before making global git config changes
2025-10-01T21:49:01.9831112Z Adding repository directory to the temporary git global config as a safe directory
2025-10-01T21:49:01.9844146Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/N_grade/N_grade
2025-10-01T21:49:01.9877571Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2025-10-01T21:49:01.9908945Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2025-10-01T21:49:02.0130384Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2025-10-01T21:49:02.0150620Z http.https://github.com/.extraheader
2025-10-01T21:49:02.0162580Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2025-10-01T21:49:02.0193655Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2025-10-01T21:49:02.0508307Z Cleaning up orphan processes