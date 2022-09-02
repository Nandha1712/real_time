import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { io } from 'socket.io-client';
let socket;

const App = () => {
    const [chatInput, setChatInput] = useState("");
    const [messages, setMessages] = useState([]);
    // const user = useSelector(state => state.session.user)
    const user = {username: "Nandha"};

    useEffect(() => {
        // open socket connection
        // create websocket
        console.log("Inside use_effect")
        socket = io("http://127.0.0.1:5000");

        socket.on("chat", (chat) => {
          console.log("REceieved results: ....")
            setMessages(messages => [...messages, chat])
        })

        // when component unmounts, disconnect
        return (() => {
            socket.disconnect()
        })
    }, [])

    const updateChatInput = (e) => {
        setChatInput(e.target.value)
    };

    const sendChat = (e) => {
        e.preventDefault()
        socket.emit("chat", { user: user.username, msg: chatInput });
        setChatInput("")
    }

    return (user && (
        <div>
            <div>
                {messages.map((message, ind) => (
                    <div key={ind}>{`${message.user}: ${message.msg}`}</div>
                ))}
            </div>
            <form onSubmit={sendChat}>
                <input
                    value={chatInput}
                    onChange={updateChatInput}
                />
                <button type="submit">Send</button>
            </form>
        </div>
    )
    )
};


export default App;