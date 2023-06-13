import React, { useState, useEffect } from 'react';
import { json } from 'react-router-dom';
import '../assets/table/table.css';

const Layout3 = () => {

    const [dataCenter, setDataCenter] = useState([]);

    const [dataInspection, setDataInspection] = useState([]);


    useEffect(() => {
        fetchDataCenter();
        fetchDataInspection();
    }, []);

    const fetchDataCenter = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/centers/');
            const jsonData = await response.json();
            setDataCenter(jsonData);
            // console.log(jsonData)
        } catch (error) {
            console.log('Error fetching data:', error);
        }

    }

    const fetchDataInspection = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/inspections/');
            const jsonData = await response.json();
            setDataInspection(jsonData);
            // console.log(jsonData[0])
        } catch (error) {
            console.log('Error fetching data:', error);
        }
    }
    // console.log(data[0]);

    const [selectedCenter, setSelectedCenter] = useState('N/A');

    console.log(selectedCenter);
    console.log(dataInspection[0]);

    const getValidInspection = () => {
        const validInspection = dataInspection.filter(item => item.center_id_id === parseInt(selectedCenter));
        console.log(validInspection);
        return validInspection;
    }

    const getCarNumber = async (center_id_id, req_id_id) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/get_plate_status/?key1=${center_id_id}&key2=${req_id_id}`);
            const jsonData = await response.json();
            console.log(jsonData);
        } catch (error) {
            console.log('Error fetching data:', error);
        }

    }

    getCarNumber(359309, 656484)

    return (
        <div className='cover'>
            <h1>Tra cứu thông tin đăng kiểm của các trung tâm</h1>

            <div className='chooseCenter'>
                <label>Chọn trung tâm đăng kiểm cần tra cứu: </label>
                <select name='Trung tâm'
                    value={selectedCenter}
                    onChange={e => setSelectedCenter(e.target.value)}
                >
                    {dataCenter.map((item, index) => {
                        return <option value={item.id}>{item.name}</option>
                    })}
                </select>
            </div>

            <div className=''>
                <h2>Thông tin đăng kiểm của các phương tiện tại trung tâm:</h2>
                <div className='tableContainer'>
                    <table>
                        <thead>
                            <tr>
                                <th>STT</th>
                                <th>Biển số xe</th>
                                <th>Ngày đăng kiểm</th>
                                <th>Ngày hết hạn</th>
                                <th>Trạng thái</th>
                            </tr>
                        </thead>
                        <tbody>
                            {getValidInspection().map((item, index) => {
                                return (
                                    <tr>
                                        <td>{index + 1}</td>
                                        <td>99999</td>
                                        <td>{item.insp_date}</td>
                                        <td>{item.exp_date}</td>
                                        <td>{item.status || "Chưa hết hạn"}</td>
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>
                </div>
            </div>
        </div >
    );
};
export default Layout3;