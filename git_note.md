## 第一次建立及上傳 git ##

# 1. 進入你的專案資料夾（如果還沒cd進去）
cd 你的專案路徑

# 2. 初始化 Git 倉庫
git init

# 3. 加入所有檔案
git add .

# 4. 第一次 commit, github是載下來改的不用這段
git commit -m "Initial commit"

# 5. 將當前分支改名為 main
git branch -m master main

# 6. （選擇性）確認分支改名成功
git branch

# 7. 新增遠端倉庫，換成你的 GitHub repo URL
git remote add origin https://github.com/xerion73741/Flask_LongTermCare_Projec.git

# 8. 推送 main 分支到遠端，並設定 upstream（追蹤遠端分支）
git push -u origin main

----------------------------------------------------------------------------

#### 之後上傳流程 ####

# 1. 將修改過的檔案放進暫存
git add .

# 2. 提交 commit，填上這次修改的說明
git commit -m "你的這次修改內容說明"

# 3. 推送到遠端 GitHub main 分支
git push

---------------------------------------
Git + GitHub 常用操作流程筆記
# 1. 查看狀態與版本紀錄
查看當前工作區狀態（有哪些修改、哪些檔案被追蹤）
git status                      # 查看當前狀態
git log --oneline --graph --all # 簡潔版歷史紀錄
git branch                      # 查看分支

查看簡潔歷史 commit 紀錄（含分支關係圖）
git log --oneline --graph --all

查看所有本地分支
git branch <branch-name>  # 新建分支
git checkout <branch-name> # 切換分支
git branch -d <branch-name> # 刪除分支

# 2. 本地操作：編輯、分支管理
新建分支（但還沒切換）
git branch <branch-name>

切換分支
git checkout <branch-name>

刪除本地分支（確認不需要後）
git branch -d <branch-name>

# 3. 修改管理
取消暫存（把 staged 狀態還原為未暫存）
git restore --staged <file>

放棄工作區的所有未提交改動（注意會直接覆蓋，務必確定不要重要修改）
git reset --hard

# 4. 提交紀錄
修改最新 commit（適用修改 commit 訊息或補充檔案）
git commit --amend
（進入編輯後，按 Esc 輸入 :wq 並 Enter）

# 5. 遠端倉庫操作（GitHub）
將本地 commit 推送到遠端倉庫（上傳）
git push                          # 推送到遠端
git clone <url>                   # 抓整包專案
git pull                          # 從遠端拉取並合併（下載＋合併，若有衝突需手動處理）
git rm --cached -r <name>         # 停止追蹤檔案（刪除暫存區中的檔案，但保留本地檔案）

git rm <file>                     # 在本機工作目錄刪除檔案
git rm -r --cached <file>
git commit -m "刪除 git.txt 檔案"  # commit 這次刪除
git push                          # 到遠端同步刪除

# 6. 進階：重寫 commit 歷史
git rebase               # 開始重組 Commit
git rebase --continue    # 繼續 Rebase
git rebase --abort       # 放棄 Rebase

----------------------------------
# 7. 還原
git log --oneline 查看 commit 版本紀錄
git checkout ID --<file>
git status
git add .
git commit -m "還原 login.html"
git push

--------------------------------------
# 8. 衝突版本
git pull --rebase origin main 手動比較檔案
