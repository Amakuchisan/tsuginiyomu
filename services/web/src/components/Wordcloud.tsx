import React, { useContext } from 'react';

import { CreateWordCloudRequest } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";
import { UserContext } from '../App';

export const Wordcloud = () => {
    const { user, setUser } = useContext(UserContext);

    const updateWordcloud = () => {
        const request = new CreateWordCloudRequest();
        if (user.HatenaID) {
            request.setHatenaId(user.HatenaID);

            const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
            client.createWordCloud(request, {}, (err, ret) => {
                if (err || ret === null) {
                    throw err;
                }
                const wordcloud = window.atob(ret.getWordcloud_asB64());
                setUser({...user, wordcloud: wordcloud});
            });
        }
    }
    const onClick = () => {
        updateWordcloud();
    };

    return (
        <header className="wordcloud">
            <h2>{user.HatenaID}さんのワードクラウドを作成する</h2>

            <button onClick={onClick}>画像を更新する</button>
            {user.wordcloud && (
                <div className="image">
                    <img src={`data:;image/png;base64,${user.wordcloud}`} alt="wordcloud" />
                </div>
            )}
        </header>
    )
}
