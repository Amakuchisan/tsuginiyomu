import { useContext, useState } from 'react';

import { CreateWordCloudRequest } from "../pb/wordcloud/wordcloud_pb";
import { WordcloudClient } from "../pb/wordcloud/WordcloudServiceClientPb";
import { UserContext } from '../App';

export const Wordcloud = () => {
    const { user, setUser } = useContext(UserContext);
    const [message, setMessage] = useState("画像を更新する");

    const updateWordcloud = () => {
        const request = new CreateWordCloudRequest();
        if (user.HatenaID) {
            request.setHatenaId(user.HatenaID);
            setMessage("更新中...")

            const client = new WordcloudClient(`http://${window.location.hostname}:8080/wordcloud`, {}, {});
            client.createWordCloud(request, {}, (err, ret) => {
                if (err || ret === null) {
                    throw err;
                }
                const wordcloud = window.atob(ret.getWordcloud_asB64());
                setUser({ ...user, wordcloud: wordcloud });
                setMessage("画像を更新する")
            });
        }
    }
    const onClick = () => {
        updateWordcloud();
    };

    return (
        <header className="wordcloud">
            { user.HatenaID && (
                <div>
                    <h2>{user.HatenaID}さんのワードクラウドを作成する</h2>
                    <button onClick={onClick}>{message}</button>
                    {user.wordcloud && (
                        <div className="image">
                            <img src={`data:;image/png;base64,${user.wordcloud}`} alt="wordcloud" />
                        </div>
                    )}
                </div>
            )}
        </header>
    )
}
