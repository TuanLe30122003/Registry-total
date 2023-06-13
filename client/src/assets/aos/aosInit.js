import AOS from 'aos';
import 'aos/dist/aos.css';

const aosInit = () => {
    AOS.init(); // Khởi tạo thư viện AoS

    // Tùy chọn: Thiết lập các tuỳ chọn mặc định của AoS
    // Bạn có thể tùy chỉnh các tuỳ chọn này theo ý muốn
    AOS.init({
        duration: 1000, // Thời gian diễn ra hiệu ứng (ms)
        offset: 200, // Khoảng cách từ khi cuộn đến phần tử để kích hoạt hiệu ứng (px)
        easing: 'ease-in-out', // Kiểu easing sử dụng cho hiệu ứng
        delay: 200, // Độ trễ trước khi bắt đầu hiệu ứng (ms)
        once: true, // Hiệu ứng chỉ được kích hoạt một lần duy nhất
    });

    // Tùy chỉnh các tuỳ chọn theo component hoặc trang riêng
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        // more custom options here...
    });

    // Đảm bảo rằng bạn gọi hàm này để xóa hiệu ứng khi component unmounts
    return () => {
        AOS.refresh(); // Xóa tất cả các hiệu ứng AoS đã khởi tạo
    };
};

export default aosInit;