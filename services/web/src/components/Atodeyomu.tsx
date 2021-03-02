import React, { useContext } from 'react';
// import { HatenaIDContext } from '../App';

export const Atodeyomu = () => {
    // const HatenaID = useContext(HatenaIDContext)
    //   const [HatenaID, setHatenaID] = useState('sample');
    //   const [message, setMessage] = useState('');

    const onClick = () => {
        // setMessage(`Hello ${HatenaID} !!`)
    };

    return (
        <header className="wordcloud">
            <h2>あとで読むから次に読む記事を探す</h2>
            {/* <h3>{HatenaID}</h3> */}

            <button onClick={onClick}>探す</button>
        </header>
    )
}
