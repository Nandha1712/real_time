import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import {connect} from "react-redux";
import { io } from 'socket.io-client';
import {addMetaData} from './redux/actions';

let socket;

const App = (props) => {
  console.log("Inside App func...")
  const [chatInput, setChatInput] = useState("");
  // const ru_user = useSelector(state => state)
  // console.log(ru_user);
  const user = { username: "Nandha" };
  
  let messages = props.dataModule.messages;
  console.log(messages);
  useEffect(() => {
    // open socket connection
    // create websocket
    console.log("Inside use_effect");
    socket = io("http://127.0.0.1:5000");

    socket.on("chat", (chat) => {
      console.log("REceieved results: ....");
      props.addMetaData(chat)
      // setMessages(messages => [...messages, chat])
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
          <div key={`${ind}_${message.msg}`}>{`${message.user}: ${message.msg}`}</div>
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


const mapStateToProps = state => {
  return state;
}


export default connect(mapStateToProps, {addMetaData}) (App);