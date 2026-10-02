from file_manager import FileManager

file_manager = FileManager()

while True:
    print("miditへようこそ！\n機能を選択してください\n1. ファイルを作成\n2. ファイルを読み込む\n3. ファイルを削除\n4. 終了")
    input_choice = input("選択肢を入力してください (1-4): ")

    if input_choice == "1":
        file_name = input("作成するファイル名を入力してください: ")
        content = input("ファイルに書き込む内容を入力してください: ")
        file_manager.create_file(file_name, content)
        print(f"{file_name} が作成されました。")
    elif input_choice == "2":
        file_name = input("読み込むファイル名を入力してください: ")
        content = file_manager.read_file(file_name)
        if content is not None:
            print(f"{file_name} の内容:\n{content}")
        else:
            print(f"{file_name} は存在しません。")
    elif input_choice == "3":
        file_name = input("削除するファイル名を入力してください: ")
        if file_manager.delete_file(file_name):
            print(f"{file_name} が削除されました。")
        else:
            print(f"{file_name} は存在しません。")
    elif input_choice == "4":
        print("miditを終了します。")
        break
    else:
        print("無効な選択肢です。")