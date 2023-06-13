import "../../assets/cssFiles/button.css";

const Button = (props) => {
    return (
        <button class="cssbuttons-io">
            <span>{props.title}</span>
        </button>
    );
};

export default Button;