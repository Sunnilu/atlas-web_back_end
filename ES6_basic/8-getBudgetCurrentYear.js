function getCurrentYear() {
    const date = new Date();
    return date.getFullYear();
}

export default function getBudgetCurrentYear(income, gdp, capita) {
    const currentYear = getCurrentYear();

    const budget = {
        ['income-${currentYear}']: income,
        ['gdp-${currentYear}']: gdp,
        ['capita-${currentYear}']: capita,
    };

    return budget
}
