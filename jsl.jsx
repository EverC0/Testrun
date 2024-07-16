const App = () => {
    // Js up here
    const name = 'John'
    const x = 10;
    const y = 20;
    const names = ['Brad', 'Ever', 'Kev']
  
    const loggedIn = true;
  
    // if(loggedIn){
    //   return <h1>
    //     Hello Member
    //   </h1>
    // }
  
    return (
      // everything that is being returned must be wrapped in a single element
      // this is called a fragment <> </>
      <> 
        <div className="text-5xl">App</div>
        <p>hello {name}</p>
        <p> The sum {x} and {y} is {x + y}</p>
  
        <ul>
          {names.map((name, index) =>
            <li key={index}> {name}</li>
            // since maps reurns somthing new compared to for each that is why it's suitable
          )}
        </ul>
  
        {loggedIn ? <h1 style={{fontSize:'24px'}}> Hello member</h1> : <h1> hello guest</h1>}
  
      </>
    )
  }
  
  export default App