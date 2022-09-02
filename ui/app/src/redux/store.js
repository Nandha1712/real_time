import { createStore } from "redux";
import rootReducer from "./reducers";
import { persistReducer } from 'redux-persist';
import localforage from 'localforage';

const persistConfig = {
    key: 'root',
    storage: localforage,
}

const persistedReducer = persistReducer(persistConfig, rootReducer)

export default createStore(persistedReducer);

