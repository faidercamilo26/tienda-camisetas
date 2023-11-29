import Layout from "../../hocs/Layout"
import {useState, useEffect} from 'react'
import {connect} from 'react-redux'
import { signup } from "../../redux/actions/auth"


function Signup({
    signup
}) {


    useEffect(() => {
        window.scrollTo(0,0)
    }, [])

    const [accountCreated, setAccountCreated] = useState(false);

    const [formData, setFormData] = useState({
        email: '',
        tipo_documento: '',
        numero_documento: '',
        tipo_persona: '',
        nombre: '',
        apellido: '',
        numeroCelular: '',
        direccion: '',
        username: '',
        password: '',
        re_password: '',
    })

    const {
        email,
        tipo_documento,
        numero_documento,
        tipo_persona,
        nombre,
        apellido,
        numeroCelular,
        direccion,
        username,
        password,
        re_password
    } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();
        console.log(formData);
        signup(
            email,
            tipo_documento,
            numero_documento,
            tipo_persona,
            nombre,
            apellido,
            numeroCelular,
            direccion,
            username,
            password,
            re_password
            )
            setAccountCreated(true);
            window.scrollTo(0,0)
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
            <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Registrarte</h2>
          </div>
  
          <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
              <form onSubmit = {e=>onSubmit(e)} className="space-y-6">

              <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                    Correo electrónico
                  </label>
                  <div className="mt-1">
                    <input
                      name="email"
                      value={email}
                      onChange={e=>onChange(e)}
                      type="email"
                      autoComplete="email"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                    <label htmlFor="tipo_documento" className="block text-sm font-medium text-gray-700">
                        Tipo Documento
                    </label>
                    <div className="mt-1">
                        <select
                        name="tipo_documento"
                        value={tipo_documento}
                        onChange={e=>onChange(e)}
                        className="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        required
                        >
                        <option value="" disabled selected>Selecciona un tipo de documento</option>
                        <option value="CC">Cedula de ciudadania</option>
                        <option value="CE">Cedula de extranjeria</option>
                        <option value="TI">Tarjeta de identidad</option>
                        </select>
                    </div>
                </div>

                <div>
                  <label htmlFor="numero_documento" className="block text-sm font-medium text-gray-700">
                    Numero de documento
                  </label>
                  <div className="mt-1">
                    <input
                      name="numero_documento"
                      value={numero_documento}
                      onChange={e=>onChange(e)}
                      type="Integer"
                      autoComplete="Integer"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                    <label htmlFor="tipo_persona" className="block text-sm font-medium text-gray-700">
                        Tipo de persona
                    </label>
                    <div className="mt-1">
                        <select
                        name="tipo_persona"
                        value={tipo_persona}
                        onChange={e=>onChange(e)}
                        className="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        required
                        >
                        <option value="" disabled selected>Tipo de persona</option>
                        <option value="2">Artista</option>
                        <option value="1">Cliente</option>
                        </select>
                    </div>
                </div>

                <div>
                  <label htmlFor="nombre" className="block text-sm font-medium text-gray-700">
                    Nombre
                  </label>
                  <div className="mt-1">
                    <input
                      name="nombre"
                      value={nombre}
                      onChange={e=>onChange(e)}
                      type="text"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                  <label htmlFor="apellido" className="block text-sm font-medium text-gray-700">
                    Apellido
                  </label>
                  <div className="mt-1">
                    <input
                      name="apellido"
                      value={apellido}
                      onChange={e=>onChange(e)}
                      type="text"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                  <label htmlFor="numeroCelular" className="block text-sm font-medium text-gray-700">
                    Número de celular
                  </label>
                  <div className="mt-1">
                    <input
                      name="numeroCelular"
                      value={numeroCelular}
                      onChange={e=>onChange(e)}
                      type="text"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                  <label htmlFor="direccion" className="block text-sm font-medium text-gray-700">
                    Dirección
                  </label>
                  <div className="mt-1">
                    <input
                      name="direccion"
                      value={direccion}
                      onChange={e=>onChange(e)}
                      type="text"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

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
                  <label htmlFor="re_password" className="block text-sm font-medium text-gray-700">
                    Repite la contraseña
                  </label>
                  <div className="mt-1">
                    <input
                      name="re_password"
                      value={re_password}
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
                    Registrarte
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
    signup
  }) (Signup)