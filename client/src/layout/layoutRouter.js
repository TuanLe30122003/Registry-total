import { BrowserRouter as Router, Routes, Switch, Route, Link, BrowserRouter } from "react-router-dom";
import Layout1 from "./layout1";
import Layout2 from "./layout2";
import Layout3 from "./layout3";

const LayoutRouter = () => {
    return (
        <Routes>
            <Route exact path="/" element={<Layout1 />} />
            <Route exact path="/dang-ki-tk-cho-ttdk" element={<Layout2 />} />
            <Route exact path="/theo-doi-so-luong" element={<Layout3 />} />
            <Route exact path="/du-lieu" element={<Layout3 />} />
            <Route exact path="/chuc-nang-khac" element={<Layout2 />} />
        </Routes>
    );
};

export default LayoutRouter;