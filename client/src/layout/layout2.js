import Input from "../component/input/input";
import aosInit from "../assets/aos/aosInit";
import React, { useEffect } from 'react';

const Layout2 = () => {

    useEffect(aosInit, []);

    return (
        <>
            <container className="layout2__cover">
                <div className="layout2__coverinside" data-aos="fade-up">
                    <div className="layout2__intro">
                        <h1>Tạo hồ sơ cho trung tâm đăng kiểm mới</h1>
                        <p>Tài khoản cho trung tâm đăng kiểm giúp cá nhân, tổ chức thuận tiện hơn trong việc quản lý phương tiện</p>
                    </div>

                    <form className="layout2__info">
                        <div className="layout2__info__car layout2__info__block">
                            <h3>Thông tin xe</h3>
                            <span>Các thông tin cơ bản của phương tiện</span>
                            <Input name="Biển kiếm soát" />
                            <Input name='Mã số đăng kiểm' />
                            <Input placeholder="" name="Mục đích sử dụng" type="text" />
                        </div>

                        <div className="layout2__info__car layout2__info__block">
                            <h3>Thông tin chủ xe</h3>
                            <span>Các thông tin cơ bản của chủ sở hữu phương tiện</span>
                            <Input name='Tên' />
                            <Input name='Nơi đăng kí thường trú' />
                            <Input name='Quê quán' />
                        </div>
                    </form>
                </div>


            </container>
        </>
    );
};

export default Layout2;