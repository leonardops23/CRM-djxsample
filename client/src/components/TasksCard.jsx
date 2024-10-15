import { useNavigate } from "react-router-dom"


export function TasksCard({ task }) {
    const navegate = useNavigate()

    return (
        <div onClick={() => {
            navegate(`/tasks/${task.id}`)
        }}>
            <h1>{task.title}</h1>
            <p>{task.description}</p>
        </div>
    )
}
