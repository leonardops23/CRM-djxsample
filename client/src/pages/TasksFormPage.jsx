import { useForm } from 'react-hook-form'
import { createTasks, deleteTasks, updateTasks, getTask } from '../api/tasks.api'
import { useNavigate, useParams } from 'react-router-dom'
import { useEffect } from 'react';

function TasksFormPage() {
    const {
        register, 
        handleSubmit,
        formState: { errors },
        setValue
        } = useForm();

    const Navegate = useNavigate()
    const params = useParams()

    const onSubmit = handleSubmit(async (data) => {
        if (params.id) {
            await updateTasks(params.id, data)
        } else {
            await createTasks(data);
        }
        Navegate('/tasks')
    })

    useEffect(() => {
        async function loadTask() {
            const {data: {title, description}} = await getTask(params.id)
            setValue('title', title)
            setValue('description', description)
        }
        loadTask()  
    }, [])

    return (
        <div>
            <form onSubmit={onSubmit}>
                <input
                    type="text"
                    placeholder="title"
                    {...register("title", { required: true })}
                />
                {errors.title && <span>Title is required</span>}
                <textarea
                    rows="3"
                    placeholder='Description'
                    {...register('description', { required: true })}
                ></textarea>
                {errors.description && <span>Description is required</span>}

                <button>Save</button>
            </form>
            {params.id && (
                <button onClick={async () => {
                    const accepted = window.confirm("are you sure")
                    if (accepted) {
                        await deleteTasks(params.id)
                        Navegate('/tasks');
                    }
                }}>
                    Delete
                </button>
            )}
        </div>
    )
}

export default TasksFormPage
