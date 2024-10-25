import React from 'react';

// Define the component as a named function
function NeighborhoodsList() {
    const sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];
    
    const addNeighborhood = newNeighborhood => {
        sanFranciscoNeighborhoods.push(newNeighborhood);
        return sanFranciscoNeighborhoods;
    };

    // Render JSX here
    return (
        <div>
            <h1>San Francisco Neighborhoods</h1>
            <ul>
                {sanFranciscoNeighborhoods.map((neighborhood, index) => (
                    <li key={index}>{neighborhood}</li>
                ))}
            </ul>
            {/* Add a form to input new neighborhoods */}
            <form onSubmit={(e) => {
                e.preventDefault();
                const newNeighborhood = e.target.neighborhood.value.trim();
                if (newNeighborhood) {
                    addNeighborhood(newNeighborhood);
                    e.target.reset();
                }
            }}>
                <input type="text" name="neighborhood" placeholder="Add neighborhood" />
                <button type="submit">Add</button>
            </form>
        </div>
    );
}

// Export the component
export default NeighborhoodsList;