import { Link } from "react-router-dom"


export function Navegations() {
    return (
        <div>
            <Link to="/tasks">
                <h1>
                    Tasks app
                </h1>
            </Link>
            <Link to="/tasks-create">Create tasks</Link>
        </div>
    )
}
