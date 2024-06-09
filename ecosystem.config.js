module.exports = {
    apps: [
        {
            name: "flask_api",
            script: "./app.py",
            interpreter: "python3",
            env: {
                FLASK_ENV: "production",
                TZ: "Asia/Seoul"  // 타임존 설정
            },
            env_production: {
                FLASK_ENV: "production",
                TZ: "Asia/Seoul"  // 타임존 설정
            },
            log_date_format: "YYYY-MM-DD HH:mm:ss Z"  // 로그 시간 포맷 설정
        },
    ],
};