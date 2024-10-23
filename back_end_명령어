node js 설치
```
npm install
npm install express
npm install cors
```

**수정된 package.json 예시 (유효한 JSON)**
{
  "name": "your-project-name",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1"
  },
  "scripts": {
    "start": "node index.js"
  }
}

npm start

index.js내용

```
const express = require("express")
const app = express()
const cors = require("cors")

app.use(
  cors({
    origin: "http://121.134.18.63:8080",
    methods: ["GET", "POST", "PUT", "DELETE"],
    allowedHeaders: ["Content-Type"],
    credentials: true,
  })
)

// Server code

app.listen(7860)
```


iisreset /start
iisreset /stop
iisreset /restart



---
$ npm init
$ ls
$ npm i express cors http-proxy-middleware
$ npm i nodemon



const express = require('express');
const fs = require('fs');
const https = require('https');
const cors = require('cors');
const { createProxyMiddleware } = require('http-proxy-middleware');

// SSL 인증서 경로 설정


const options = {
    key: fs.readFileSync('C:/inetpub/wwwroot/pem/key.pem'),  // 개인 키 파일
    cert: fs.readFileSync('C:/inetpub/wwwroot/pem/cert.pem'),  // 인증서 파일
};


const app = express();

// 본문 크기 제한을 50MB로 설정 (필요에 따라 값을 조정 가능)
app.use(express.json({ limit: '50mb' }));  
app.use(express.urlencoded({ limit: '50mb', extended: true }));

app.use(cors({
    origin: "*",
    methods: "GET, POST",
    credentials: true,
}));

// 프록시 설정
app.use('/', createProxyMiddleware({
    target: 'http://192.168.50.7:7860',  // Stable Diffusion API 주소
    changeOrigin: true,
    pathRewrite: {
        '^/': '/',  // 경로를 수정하지 않음
    },
}));

// HTTPS 서버 시작
https.createServer(options, app).listen(4005, '192.168.50.7', () => {
    console.log('HTTPS server is running on https://192.168.50.7:4005');
});
