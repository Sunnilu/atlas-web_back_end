// Regex pattern to find budget object: const budget = \{\s*income, \s*gdp, \s*capita\s*\}

export default function getBudgetObject(income, gdp, capita) {
    const budget ={
        income,
        gdp,
        capita,
    };

    return budget
}