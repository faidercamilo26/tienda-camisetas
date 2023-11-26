import Layout from "../../hocs/Layout"
import {useState, useEffect} from 'react'
import {connect} from 'react-redux'
import { login } from "../../redux/actions/auth"
import {TailSpin as Loader} from 'react-loader-spinner'

function Login({
    login
}) {


    useEffect(() => {
        window.scrollTo(0,0)
    }, [])


    const [formData, setFormData] = useState({
        username: '',
        password: '',
    })

    const {
        username,
        password,
    } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();
        login(
            username,
            password,
            )
    }

    return (
      <Layout>
       
        <div className="min-h-full flex flex-col justify-center py-12 sm:px-6 lg:px-8">
          <div className="sm:mx-auto sm:w-full sm:max-w-md">
            <img
              className="mx-auto h-12 w-auto"
              src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
              alt="Workflow"
            />
            <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Iniciar sesión</h2>
          </div>
  
          <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
              <form onSubmit = {e=>onSubmit(e)} className="space-y-6">


                <div>
                  <label htmlFor="username" className="block text-sm font-medium text-gray-700">
                    Username
                  </label>
                  <div className="mt-1">
                    <input
                      name="username"
                      value={username}
                      onChange={e=>onChange(e)}
                      type="username"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

  
                <div>
                  <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                    Contraseña
                  </label>
                  <div className="mt-1">
                    <input
                      name="password"
                      value={password}
                      onChange={e=>onChange(e)}
                      type="password"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

  
                <div>
                  <button
                    type="submit"
                    className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Iniciar sesión
                  </button>
                </div>
              </form>
  
              
            </div>
          </div>
        </div>
      </Layout>
    )
  }
  const mapStateToProps = state => ({

  }) 
  export default connect(mapStateToProps, {
    login
  }) (Login)