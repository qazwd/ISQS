# ISQS

信息统计与查询系统

ISQS/          # 项目根目录
├── backend/           # FastAPI 后端目录
│   ├── app/           # 后端核心代码
│   │   ├── api/       # API 路由（分模块）
│   │   │   ├── v1/    # API 版本控制（可选，推荐）
│   │   │   │   ├── endpoints/  # 具体接口实现
│   │   │   │   │   ├── users.py
│   │   │   │   │   ├── items.py
│   │   │   │   │   └── __init__.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── core/      # 核心配置（全局常量、安全、设置）
│   │   │   ├── config.py       # 配置文件（数据库、端口、密钥等）
│   │   │   ├── security.py     # 认证授权（JWT、密码加密等）
│   │   │   └── __init__.py
│   │   ├── crud/      # 数据库操作（增删改查）
│   │   │   ├── base.py         # 通用CRUD基类
│   │   │   ├── crud_user.py
│   │   │   ├── crud_item.py
│   │   │   └── __init__.py
│   │   ├── db/        # 数据库相关
│   │   │   ├── base.py         # 数据库连接基类
│   │   │   ├── session.py      # 数据库会话（连接）
│   │   │   └── __init__.py
│   │   ├── models/    # 数据库模型（ORM）
│   │   │   ├── user.py
│   │   │   ├── item.py
│   │   │   └── __init__.py
│   │   ├── schemas/   # Pydantic 数据校验模型（请求/响应体）
│   │   │   ├── user.py
│   │   │   ├── item.py
│   │   │   └── __init__.py
│   │   ├── utils/     # 工具函数（通用方法）
│   │   │   ├── common.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── tests/         # 后端测试用例
│   │   ├── test_users.py
│   │   ├── test_items.py
│   │   └── __init__.py
│   ├── .env           # 环境变量（数据库地址、密钥等，不上传仓库）
│   ├── .env.example   # 环境变量示例（上传仓库，供参考）
│   ├── requirements.txt  # 后端依赖
│   ├── main.py        # 后端入口文件
│   └── README.md      # 后端说明文档
│
├── frontend/          # React 前端目录（Create React App 生成）
│   ├── public/        # 静态资源（不经过webpack处理）
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── manifest.json
│   ├── src/           # 前端核心代码
│   │   ├── api/       # API 请求封装（对接后端接口）
│   │   │   ├── axiosInstance.js  # axios 实例（统一配置）
│   │   │   ├── userApi.js
│   │   │   └── itemApi.js
│   │   ├── assets/    # 静态资源（图片、样式、字体等）
│   │   │   ├── images/
│   │   │   └── styles/
│   │   ├── components/ # 通用组件（按钮、表单、弹窗等）
│   │   │   ├── Button/
│   │   │   ├── Form/
│   │   │   └── Layout/
│   │   ├── pages/     # 页面组件（按业务模块划分）
│   │   │   ├── Home/
│   │   │   ├── User/
│   │   │   └── Item/
│   │   ├── hooks/     # 自定义Hooks
│   │   │   ├── useAuth.js
│   │   │   └── useRequest.js
│   │   ├── context/   # React Context（状态管理，小型项目）
│   │   ├── store/     # Redux/Zustand 状态管理（中大型项目）
│   │   ├── utils/     # 工具函数（格式化、验证等）
│   │   ├── routes/    # 路由配置
│   │   ├── App.js     # 根组件
│   │   ├── index.js   # 入口文件
│   │   └── setupProxy.js  # 跨域代理配置（开发环境）
│   ├── package.json   # 前端依赖
│   ├── .env           # 前端环境变量
│   └── README.md      # 前端说明文档
│
└── README.md          # 项目整体说明文档

构建前端:
npm create vite@latest . -- --template react
npm install
npm install axios react-router-dom
