# Sparta-bucketlist

나만의 버킷리스트를 업로드하고 좋아요 기능을 구현해본 간단한 1인 토이 프로젝트 입니다.

### Main Page
![image](https://user-images.githubusercontent.com/70055619/155463483-48ae4255-c9db-4b72-8f78-8c1a3270cf8d.png)



### Main Page (카테고리별 분류)
![image](https://user-images.githubusercontent.com/70055619/155464396-4ee8defa-5577-41fa-9f7c-52e11dacb991.png)



### Main Page (좋아요순 정렬)
![image](https://user-images.githubusercontent.com/70055619/155464505-0a136663-50ee-48ea-a0ac-b1641643a9d8.png)



### SignUp page
![image](https://user-images.githubusercontent.com/70055619/155464791-f93793ca-3b32-4ecc-af2b-dcdfe3d850e8.png)



### Login page
![image](https://user-images.githubusercontent.com/70055619/155465135-07c36387-2377-4e20-beb4-705f8e6a835b.png)



### FindPw page
![image](https://user-images.githubusercontent.com/70055619/155465300-e1993041-2a9e-4957-9d3e-ca44a5ba4cfb.png)
![image](https://user-images.githubusercontent.com/70055619/155465547-05fd9bc5-21e6-44f1-83b3-68427514ab64.png)



### FindId page
![image](https://user-images.githubusercontent.com/70055619/155465622-8408b896-54f8-4e8b-aa87-560c95693381.png)



### Upload page
![image](https://user-images.githubusercontent.com/70055619/155465938-06c36691-59cc-4846-b5de-6d8f7cef4e93.png)



## API 설계

| 기능          | URL             | Method    |Request      |Response|
| ----------- | --------------- | --------- | ----------- | ------ |
| 버킷리스트 전체 조회     | /api/list          | GET      | {}      | {'lists': [{'title': "스카이 다이빙", "category": "스포츠", "description":"스카이 다이빙 해야지!", "image": "", "like": 12}, ....]} |
| 버킷리스트 업로드       | /api/enrollment | POST | {title_give: title, description_give: description, image_give: image, category_give: category} | {'msg': '등록되었습니다!'} |
| 좋아요  | /api/heart | POST| {image_give: image}       | {'result': True} |{}  |
| 회원가입      | /api/member  | POST | {id_give: id, pw_give: pw, nickname_give: nickname}  |  {'msg': '등록되었습니다!'} |
| 로그인체크      | /api/check  | POST | {id_give: id_check, pw_give: pw_check}  |  {'result': True} or {'msg': '아이디 및 비밀번호가 틀렸습니다!', 'result': False} |
| 회원가입 중복 체크     | /api/sign_up_check  | POST | {id_give: id}  |  {'result': False} or {'result': True} |
| 업로드 중복 체크     | /api/upload_check  | POST | {image_give: image}  |  {'result': False} or {'result': True} |
| 비밀번호찾기     | /api/find_password_check  | POST | {id_give: id}  |  {'result': False} or {'result': True} |
| 메인페이지 카테고리별 분류     | /api/category  | POST | {category_give:category}  |  {'lists': [{'title': "스카이 다이빙", "category": "스포츠", "description":"스카이 다이빙 해야지!", "image": "", "like": 12}, ....]} |
| 메인페이지 좋아요순 정렬     | /api/like  | GET | {}  |  {'lists': [{'title': "스카이 다이빙", "category": "스포츠", "description":"스카이 다이빙 해야지!", "image": "", "like": 12}, ....]} |
| 비밀번호 변경     | /api/modify_password  | POST | {id_give: id_input, pw_give: pw_input}  |  {'msg': '변경완료!'} |
| 아이디 찾기시 이름 존재 여부 체크     | /api/name_check  | POST | {name_give: name}  |  {'result': False} or {'result': True} |
| 아이디 찾기시 해당 이름 아이디 호출     | /api/check_id  | POST | {name_give: decode_name}  |  {'lists': [{'id1': "qweewq", "pw": "q%31d%", "name:"반원재"}, ....]} |







