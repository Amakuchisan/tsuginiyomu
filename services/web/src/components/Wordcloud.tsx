import React, { useContext } from 'react';
import { HatenaIDContext } from '../App';

export const Wordcloud = () => {
    const [HatenaID, wordcloud] = useContext(HatenaIDContext)
    //   const [HatenaID, setHatenaID] = useState('sample');
    //   const [message, setMessage] = useState('');

    const onClick = () => {
        // setMessage(`Hello ${HatenaID} !!`)
    };

    return (
        <header className="wordcloud">
            <h2>ワードクラウドを作成する</h2>
            <h3>{HatenaID}</h3>

            <button onClick={onClick}>画像を更新する</button>
            {wordcloud && (
                <div className="wordcloud">
                    <img src={`data:;image/png;base64,${wordcloud}`} alt="wordcloud" />
                </div>
            )}
        </header>
    )
}
