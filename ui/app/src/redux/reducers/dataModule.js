const initialState = {
    messages: [],
}

export default function dataModuleFunc(state = initialState, action) {
    switch (action.type) {
        case "ADD_METADATA":
            let prevMessages = state.messages;
            if (prevMessages === undefined) {
                prevMessages = [];
            }
            

            const newMessage = action.payload.content;
            let newMessages = [];
            if (newMessage !== undefined) {
                newMessages.push(newMessage);
            }
            
            return {
                ...state,
                messages: [ ...prevMessages,  ...newMessages]
            }

        default:
            return state;
    }

}
