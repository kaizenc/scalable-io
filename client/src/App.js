import React from "react";
import io from "socket.io-client";
const ENDPOINT = "http://kaizenc_server_1:8080";

function App() {
  // const [response, setResponse] = useState("");

  // useEffect(() => {
  //   const socket = socketIOClient(ENDPOINT);
  //   socket.on("FromAPI", data => {
  //     setResponse(data);
  //   });
  // }, []);

  const socket = io(ENDPOINT)
  socket.emit("question", "data")
  return (
    <p>
      Emitted
    </p>
  );
}

export default App;