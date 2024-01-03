// import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';
// import {decode as base64_decode, encode as base64_encode, encode} from 'base-64';
import { Base64, encode, decode } from 'js-base64';

let login = 'admin'
let password = 'Wu57u4n6_@'

export default class MyComponent extends Component {
   constructor(props) {
      super(props);
      this.state = {
         error: null,
         isLoaded: false,
         items: []
      };
   }

   componentDidMount(){
      fetch("http://127.0.0.1:8000/rest/api-auth/login/", {
         headers: new Headers({
            "Authorization": `Basic ${encode(`${login}:${password}`)}`
         }),
      }).then(response => {
         if (!response.ok) throw new Error(response.status);
         return response.json();
      })
   }
   // componentDidMount() {
   //     fetch("http://127.0.0.1:8000/rest/users/")
   //     .then(res => res.json())
   //     .then(
   //       (result) => {
   //          this.setState({
   //             isLoaded: true,
   //             items: result.results
   //          });
   //       },
   //       (error) => {
   //          this.setState({
   //             isLoaded:true,
   //             error
   //          });
   //       }
   //     )
   // }

   render() {
      const { error, isLoaded, items } = this.state;
      if (error) {
        return <div>Ошибка: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Загрузка...</div>;
      } else {
        return (
         //  <ul>
         //    {items.map(item => (
         //      <li id={item.id} key={item.id}>
         //        {item.id} : {item.name} : {item.alias}
         //      </li>
         //    ))}
         //  </ul>
         <div>
            {items.map(item => (
               <div>
                  <p>{item.username}</p>
                  {/* <p>{item.id}</p>  */}
                  {/* <p>{item.name}</p> */}
                  {/* <p>{item.alias}</p> */}
               </div>
         ))}
         </div>
        );
      }
    }
}






// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//  export default App;