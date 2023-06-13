import Navigation from "../component/navigation/Navigation";
import '../assets/cssFiles/landingPage.css';
import Button from "../component/button/button";
import LayoutRouter from "../layout/layoutRouter";
import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, useLocation } from "react-router-dom";
// import ScrollToTop from "../assets/scrollToTop/scrollToTop";

const LandingPage = () => {

    const ScrollToTop = () => {
        const { pathname } = useLocation();

        useEffect(() => {
            window.scrollTo(0, 0);
        }, [pathname]);

        return null;
    }

    return (
        <div className="landingPage__cover" onLoad={
            () => ScrollToTop()
        }>
            <Navigation />

            <LayoutRouter />
        </div>
    );
};

export default LandingPage;