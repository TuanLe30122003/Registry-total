import { BrowserRouter as Router, Routes, Switch, Route, Link, BrowserRouter } from "react-router-dom";
import Layout1 from "./layout1";
import Layout2 from "./layout2";
import Layout3 from "./layout3";
import Layout4 from "./layout4";
import Login from "./login";
import Navigation from "../component/navigation/Navigation";

import { useEffect } from 'react';

const LayoutRouter = () => {

    return (

        <>
            <Routes>
                <Route exact path="/dang-nhap" element={<Login />} />
                <Route exact path="/" element={<Layout1 />} />
                <Route exact path="/dang-ki-tk-cho-ttdk" element={<Layout2 />} />
                <Route exact path="/theo-doi-so-luong" element={<Layout3 />} />
                <Route exact path="/du-lieu" element={<Layout4 />} />
                <Route exact path="/chuc-nang-khac" element={<Layout2 />} />
            </Routes>
        </>
    );
};

export default LayoutRouter;