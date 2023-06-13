import Button from "../component/button/button";
import aosInit from "../assets/aos/aosInit";
import React, { useEffect } from 'react';

const Layout1 = () => {

    useEffect(aosInit, []);

    return (
        <>
            <div className="landingPage__content">
                <div className="landingPage__content__left" data-aos="fade-right">
                    <h1>Registry Total</h1>
                    <p>Hệ thống hỗ trợ quản lý đăng kiểm</p>
                    <br></br>
                    <div className="landingPage__content__left-button">
                        <Button title="Đăng nhập" />
                        <a href="">Tìm hiểu thêm ?</a>
                    </div>
                </div>

                <div className="landingPage__content__right">

                </div>
            </div>
        </>
    );
};

export default Layout1;