import React, { useState } from 'react';
import './App.css';
import { Welcome } from './components/Welcome'
import { Wordcloud } from './components/Wordcloud'

type User = {
  inputText: string,
  HatenaID: string,
};

type initialContext = {
  user: User,
  setUser: React.Dispatch<React.SetStateAction<User>>
};

const initialValue = {
  inputText: '',
  HatenaID: '',
};

export const UserContext = React.createContext({} as initialContext)
export const HatenaIDContext = React.createContext('' as User["HatenaID"])

function App() {
  const [user, setUser] = useState<User>(initialValue);
  return (
    <div className="App">
      <UserContext.Provider value={{ user, setUser }}>
        <Welcome />
      </UserContext.Provider>
      <HatenaIDContext.Provider value={user.HatenaID}>
        <Wordcloud />
      </HatenaIDContext.Provider>
    </div>
  );
}

export default App;
