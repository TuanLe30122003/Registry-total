import logo from '../../assets/images/logoWithCap.png';
import Button from '../button/button';
import '../../assets/cssFiles/navigation.css'
import { BrowserRouter as Router, Routes, Switch, Route, Link, BrowserRouter } from "react-router-dom";

const Navigation = () => {
    return (
        <nav className="navigation">
            <div className="navigation__logo">
                <img src={logo}></img>
                <h2><Link to='/'>Registry total</Link></h2>
            </div>

            <div className="navigation__menu">
                <ul>
                    <li>
                        <Link to='/dang-ki-tk-cho-ttdk'>Cấp TK cho TTDK</Link>
                    </li>
                    <li><Link to='/theo-doi-so-luong'>Theo dõi số lượng</Link></li>
                    <li><Link to='/du-lieu'>Lấy dữ liệu ĐK</Link></li>
                    <li><Link to='/chuc-nang-khac'>Khác</Link></li>
                </ul>
            </div>

            <div className="navigation__auth">
                <Button title="Đăng nhập" />
            </div>
        </nav>
    );
};

export default Navigation;