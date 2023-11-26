import {
    SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    ACTIVATION_SUCCESS,
    ACTIVATION_FAIL,
    SET_AUTH_LOADING,
    REMOVE_AUTH_LOADING,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,
    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    REFRESH_SUCCESS,
    REFRESH_FAIL,
    LOGOUT,
} from './types'

import axios from 'axios'
import { setAlert } from './alert';

export const check_authenticated = () => async dispatch => {
    if(localStorage.getItem('access')){
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        };

        const body = JSON.stringify({
            token: localStorage.getItem('access')
        });

        try {
            const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/jwt/verify/`, body, config);

            if (res.status === 200) {
                dispatch({
                    type: AUTHENTICATED_SUCCESS
                });
            } else {
                dispatch({
                    type: AUTHENTICATED_FAIL
                });
            }
        } catch(err){
            dispatch({
                type: AUTHENTICATED_FAIL
            });
        }
    } else {
        dispatch({
            type: AUTHENTICATED_FAIL
        });
    }
}

export const signup = (email, tipo_documento, numero_documento, tipo_persona, nombre, apellido, numeroCelular, direccion, username,     
    password, re_password) =>
async dispatch => {

    dispatch({
        type: SET_AUTH_LOADING
    });


    if (password.length < 8) {
        dispatch(setAlert('La contraseña debe tener al menos 8 caracteres', 'red'));
        dispatch({
            type: REMOVE_AUTH_LOADING,
        });
        return;
    }

    if (password !== re_password) {
        dispatch(setAlert('Las contraseñas no coinciden', 'red'));
        dispatch({
            type: REMOVE_AUTH_LOADING,
        });
        return; 
    }

    
    const passwordRegex = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{8,}$/;

    if (!passwordRegex.test(password)) {
        dispatch(setAlert('La contraseña debe tener al menos una mayúscula, un número y un carácter especial', 'red'));
        dispatch({
            type: REMOVE_AUTH_LOADING,
        });
        return;
    }

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    }

    const body = JSON.stringify({
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
    });

    try{
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/`,body, config);

        if(res.status === 201){
            dispatch({
                type: SIGNUP_SUCCESS,
                payload: res.data
            })
            dispatch(setAlert('Te enviamos un correo, por favor activa tu cuenta.', 'green'))
        }else{
            dispatch({
                type: SIGNUP_FAIL
            });
            dispatch(setAlert('Error al crear la cuenta, por favor revisa los datos', 'red'))
        }

        dispatch({
            type: REMOVE_AUTH_LOADING
        });

    }
    catch(err){
        dispatch({
            type: SIGNUP_FAIL
        });
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
        dispatch(setAlert('Error al conectar con el servidor, intentalo mas tarde', 'red'))
    }
};

export const load_user = () => async dispatch => {
    if(localStorage.getItem('access')){
        const config = {
            headers: {
                'Authorization': `JWT ${localStorage.getItem('access')}`,
                'Accept': 'application/json'
            }
        };
        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/users/me/`, config);
        
            if (res.status === 200) {
                dispatch({
                    type: USER_LOADED_SUCCESS,
                    payload: res.data
                });
            } else {
                dispatch({
                    type: USER_LOADED_FAIL
                });
            }
        }
        catch(err){
            dispatch({
                type: USER_LOADED_FAIL
            });
        }
    } else {
        dispatch({
            type: USER_LOADED_FAIL
        });
    }
}

export const login = (username, password) => async dispatch => {
    dispatch({
        type: SET_AUTH_LOADING
    });

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({
        username,
        password
    });

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/jwt/create/`, body, config);
    
        if (res.status === 200) {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            });
            dispatch(load_user);
            dispatch({
                type: REMOVE_AUTH_LOADING
            });
            dispatch(setAlert('Inicio de sesión con éxito', 'green'));
        } else {
            dispatch({
                type: LOGIN_FAIL
            });
            dispatch({
                type: REMOVE_AUTH_LOADING
            });
            dispatch(setAlert('Error al iniciar sesion.', 'red'));
        }
    }
    catch(err){
        dispatch({
            type: LOGIN_FAIL
        });
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
        dispatch(setAlert('Error al iniciar sesion. Intenta mas tarde', 'red'));
    }
}


export const activate = (uid, token) => async dispatch => {
    dispatch({
        type: SET_AUTH_LOADING
    });
    dispatch({
        type: SET_AUTH_LOADING
    });

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({
        uid,
        token
    });

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/activation/`, body, config);
    
        if (res.status === 204) {
            dispatch({
                type: ACTIVATION_SUCCESS
            });
            dispatch(setAlert('Cuenta activada correctamente', 'green'))
        } else {
            dispatch({
                type: ACTIVATION_FAIL
            });
            dispatch(setAlert('Error al activar la cuenta', 'red'))
        }
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
    }
    catch(err){
        dispatch({
            type: ACTIVATION_FAIL
        });
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
        dispatch(setAlert('Error al conectar con el servidor, intentalo mas tarde', 'red'))
    }
};

export const refresh = () => async dispatch => {
    if (localStorage.getItem('refresh')) {
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        };

        const body = JSON.stringify({
            refresh: localStorage.getItem('refresh')
        });

        try {
            const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/jwt/refresh/`, body, config);
            
            if (res.status === 200) {
                dispatch({
                    type: REFRESH_SUCCESS,
                    payload: res.data
                });
            } else {
                dispatch({
                    type: REFRESH_FAIL
                });
            }
        }catch(err){
            dispatch({
                type: REFRESH_FAIL
            });
        }
    } else {
        dispatch({
            type: REFRESH_FAIL
        });
    }
}

export const logout = () => dispatch => {
    dispatch({
        type: LOGOUT
    })
    dispatch(setAlert('sesion cerrada correctamente', 'green'));
}