import { share } from "rxjs/operators";
import { webSocket } from "rxjs/webSocket";
import { uuid } from "uuidv4";

let _socket: any;
export let messages: any;
export const clientUUID = uuid();

export const connect = (boardID: number) => {
  if (!_socket || _socket.closed) {
    console.log("connecting to websockets");
    _socket = webSocket(`ws://localhost:8000/ws/board/${boardID}`);
    messages = _socket.pipe(share());
    messages.subscribe((message: any) => console.log(message));
  }
};

export const sendMessage = (type: string, data: any, boardID: number) => {
  connect(boardID);
  const message = {
    type: type,
    data: data,
  };
  _socket.next(message);
};

export const disconnect = () => {
  if (_socket || _socket.open) {
    console.log("disconnecting");
    _socket.unsubscribe();
  }
};

export const NEW_COLUMN = "new.column";
