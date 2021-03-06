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
                    setMessage("エラーが発生")
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
        <div className="wordcloud">
            { user.HatenaID && (
                <div>
                    <h2>ワードクラウドを作成する</h2>
                    <p>{user.HatenaID}さんの過去のブックマークデータからワード・クラウドを作成します</p>
                    <button onClick={onClick}>{message}</button>
                    {user.wordcloud && (
                        <div className="image">
                            <img src={`data:image/png;base64,${user.wordcloud}`} alt="wordcloud" />
                        </div>
                    )}
                </div>
            )}
        </div>
    )
}
