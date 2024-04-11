import React, { useState, useRef } from 'react';
import { useIdleTimer } from 'react-idle-timer';
import Modal from 'react-modal';

Modal.setAppElement('#root')

export default function IdleTimerContainer(){

    const [isLoggedIn, setIsLoggedIn] = useState(false);      //Determine if the user is logged in
    const [modalIsOpen, setModalIsOpen] = useState(false);   //Determines if the model is open or false.
    const [username, setUsername] = useState('');             // Define and initialize 'username'
    const [password, setPassword] = useState('');
    
    const idleTimerRef=useRef(null)                         
    const sessionTimeoutRef = useRef(null)                  //Stores reference to the session timeout timer                        
    
    //Authentication
    const handleLogin = () => {
        // Hardcoded login credentials for testing
        if (username === 'admin' && password === 'admin') {
            setIsLoggedIn(true);
            setModalIsOpen(false);
            console.log('User logged in successfully')
        } 
        else {
            console.log('User login failed')
            alert('Invalid username or password');
        }
    };

    //Determines if the user is idle
    const onIdle=()=>{
        console.log('User is Idle')                              //logs message to the console

        if(isLoggedIn){
            setModalIsOpen(true)                                       //Modal is open
            sessionTimeoutRef.current = setTimeout(logOut, 5*1000)     //5 secs for testing purposes: 
        }
            
    }
    //Timeout timer 
    const idleTimer = useIdleTimer({
        crossTab: true,                         //This will detect user activity across multiple tabs.
        ref: idleTimerRef,
        onIdle: onIdle,
        timeout: 5*1000                         //timeout timer: 5 secs for testing purposes
    })
    
    //This function is called when the user decides to stay active 
    const stayActive = () => {
        setModalIsOpen(false)                     //closes modal
        clearTimeout(sessionTimeoutRef.current)   //clears the timeout timer set using the setTimeout function
        console.log('User is active')
    }

    //Determines if User is logged out due to inactivity or their own will.
    const logOut = () => {
        setModalIsOpen(false)                     
        setIsLoggedIn(false)                       //Logs the user out
        clearTimeout(sessionTimeoutRef.current)
        console.log('User has logged out') 
    }
    
    // Warning modal for inactive users
    return (
        <div idleTimer ={idleTimer}>
            { isLoggedIn ? (<h2>Hello Admin</h2>
            ) : (
                <div>
                    <h2>Sign In</h2>
                    <div>
                        <input
                            type="text"
                            placeholder="Username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}/>
                        <input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}/>
                        <button onClick={handleLogin}>Login</button>
                    </div>
                </div>
            )}     

            <Modal isOpen = {modalIsOpen}> 
                <h2>Your session is about to expire!</h2>
                <p>You are being timed out due to inactivity. Please choose to stay signed in or to logoff</p>
                <div>
                    <button onClick={logOut}>Log Off</button>
                    <button onClick={stayActive}>Stay Logged In</button>
                </div>
            </Modal>
        </div>
    );
}
