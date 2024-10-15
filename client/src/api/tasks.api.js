import axios from 'axios'

const tasksApi = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/tasks/'
})

export const getAllTasks = () => tasksApi.get('/')
export const createTasks = (task) => tasksApi.post('/', task)
export const deleteTasks = (id) => tasksApi.delete(`${id}/`) 
export const updateTasks = (id, task) => tasksApi.put(`${id}/`, task)
export const getTask = (id) => tasksApi.get(`${id}/`)
