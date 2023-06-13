import "../../assets/cssFiles/input.css"

const Input = (props) => {

    return (
        <>
            <label>
                <h3>{props.name || "Tên trường"} : </h3>
                <input placeholder={props.placeholder || "Nhập tại đây"} type={props.type || "text"} class="input" required={props.required} />
            </label>

            <span></span>
        </>
    );
};

export default Input;
