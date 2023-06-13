import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    // console.log(username + password);

    const CUCDANGKIEM = {
        username: "cucdangkiemHN",
        password: "123456"
    }

    return (

        <form class="form">
            <p class="form-title">Sign in to your account</p>
            <div class="input-container">
                <input placeholder="Enter email" type="text" className="username"
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                />
                <span>
                    <svg stroke="currentColor" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path>
                    </svg>
                </span>
            </div>
            <div class="input-container">
                <input placeholder="Enter password" type="password" className="password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />

                <span>
                    <svg stroke="currentColor" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path>
                        <path d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path>
                    </svg>
                </span>
            </div>
            <button class="submit" type="submit" onClick={
                (e) => {
                    e.preventDefault();
                    if (username === CUCDANGKIEM.username && password === CUCDANGKIEM.password) {
                        console.log("Đăng nhập thành công");
                        navigate('/');
                    } else {
                        console.log("Đăng nhập thất bại");
                        setUsername('');
                        setPassword('');
                    }
                }
            }>
                Sign in
            </button>
        </form>

    );
}

export default Login;
