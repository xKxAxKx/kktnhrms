## これは何か
*  kktnhrms a.k.a xKxAxKx のウェブサイトのやつです

## 環境
* Python >= 3.6.0
* Django >= 2.0
* node >=

## サイトの目的
- SNSアカウントとか色々ありすぎて自分でもワケワカンなくなっているので、それをまとめたりするなど
- サーバサイドはDjango
- フロントエンドはVue.js

## ローカルでの起動
- vue
```
$ npm run dev
```

- django
```
$ python manage.py runserver --settings=django_app.settings.local
```

## Build
```
$ npm run build
```
/dist以下はgitignoreしているので、サーバ上でgit pullした後にも実行する
