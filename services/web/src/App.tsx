import React, { useState } from 'react';
import './App.css';
import { Atodeyomu } from './components/Atodeyomu'
import { Hotentory } from './components/Hotentory'
import { Welcome } from './components/Welcome'
import { Wordcloud } from './components/Wordcloud'

// react-tabs
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';

type User = {
  HatenaID: string,
  wordcloud: string,
};

type initialContext = {
  user: User,
  setUser: React.Dispatch<React.SetStateAction<User>>
};

const initialUserValue = {
  HatenaID: '',
  wordcloud: '',
};

type wordcloudContext = {
  user: User,
  setWordcloud: React.Dispatch<React.SetStateAction<User['wordcloud']>>
};

export const UserContext = React.createContext({} as initialContext)
// export const HatenaIDContext = React.createContext('' as User["HatenaID"])
export const WordcloudContext = React.createContext({} as wordcloudContext)

function App() {
  const [user, setUser] = useState<User>(initialUserValue);
  const [wordcloud, setWordcloud] = useState<string>("");
  return (
    <div className="App">
      <UserContext.Provider value={{ user, setUser }}>
        <Welcome />
      </UserContext.Provider>
      <div className="Tab">
        {/* react-tab */}
        <Tabs>
          <TabList>
            <Tab>あとで読むから探す</Tab>
            <Tab>ホットエントリーから探す</Tab>
          </TabList>
          <TabPanel>
            <Atodeyomu />
          </TabPanel>
          <TabPanel>
            <Hotentory />
          </TabPanel>
        </Tabs>
        {/* react-tab */}
      </div>
      {/* <HatenaIDContext.Provider value={[user.HatenaID, user.wordcloud]}> */}
      <WordcloudContext.Provider value={{user, setWordcloud}}>
        <Wordcloud />
      </WordcloudContext.Provider>
    </div>
  );
}

export default App;
