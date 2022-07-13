GIT - это распределенная система контроля версии
Это система для отслежиания и введения истории изменений ваших файлов и проектов.
Репазиторий - это хранилище ваших файлов которые отслеживаются при помощи гита, и их изменений.
Команды Git:
1.git init -  команда создает новый гит репозиторий локально на вашем пк, сохдаст она в той дериктории где вы запускаете эту команду.

2. git add - когда мы создаем и изменчем файлы то при помощи жтой команды мы загркжаем все изменения в промежуточное место хранение 
git add <file_name>
git add. -> Все в текущей дериктории 

3. git commit - как только мы достигаем определенного момента разработки то мы тогда сохраняем и комментируем все нащи изменения в репозиторий. (Фиксация изменений в репозиторий)
git commit -m '<comment>'

4. git remote add - это команда для того чтобы связать ваш локальный репозиторий с удаленным репозиторием (репо в гитхабе)
 git remote add <название подключения> <ссылка на репозиторий>

git remote add origin <url>

5. git push - после коммита изменений при помощи этой команды мы отправляем наши изменения в файлах на удаленный репозиторий.

git push <origin> <название ветки (main)>

git push origin main





