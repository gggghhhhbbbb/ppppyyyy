class Calculator {
    constructor() {
        this.displayValue = '0';
        this.firstOperand = null;
        this.waitingForSecondOperand = false;
        this.operator = null;
    }

    updateDisplay() {
        document.querySelector('.display').textContent = this.displayValue;
    }

    inputDigit(digit) {
        if (this.waitingForSecondOperand) {
            this.displayValue = digit;
            this.waitingForSecondOperand = false;
        } else {
            this.displayValue = this.displayValue === '0' ? digit : this.displayValue + digit;
        }
    }

    inputDecimal() {
        if (this.waitingForSecondOperand) {
            this.displayValue = '0.';
            this.waitingForSecondOperand = false;
            return;
        }

        if (!this.displayValue.includes('.')) {
            this.displayValue += '.';
        }
    }

    handleOperator(nextOperator) {
        const inputValue = parseFloat(this.displayValue);

        if (this.operator && this.waitingForSecondOperand) {
            this.operator = nextOperator;
            return;
        }

        if (this.firstOperand === null && !isNaN(inputValue)) {
            this.firstOperand = inputValue;
        } else if (this.operator) {
            const result = this.calculate(this.firstOperand, inputValue, this.operator);
            this.displayValue = `${parseFloat(result.toFixed(7))}`;
            this.firstOperand = result;
        }

        this.waitingForSecondOperand = true;
        this.operator = nextOperator;
    }

    calculate(firstOperand, secondOperand, operator) {
        switch (operator) {
            case 'add': return firstOperand + secondOperand;
            case 'subtract': return firstOperand - secondOperand;
            case 'multiply': return firstOperand * secondOperand;
            case 'divide': return firstOperand / secondOperand;
            default: return secondOperand;
        }
    }

    clear() {
        this.displayValue = '0';
        this.firstOperand = null;
        this.waitingForSecondOperand = false;
        this.operator = null;
    }

    plusMinus() {
        this.displayValue = this.displayValue.charAt(0) === '-' ? 
            this.displayValue.slice(1) : 
            '-' + this.displayValue;
    }

    percentage() {
        const value = parseFloat(this.displayValue);
        this.displayValue = `${value / 100}`;
    }
}

const calculator = new Calculator();

document.querySelector('.buttons').addEventListener('click', (event) => {
    if (!event.target.matches('button')) return;

    const key = event.target.dataset.key;

    if (key.match(/[0-9]/)) {
        calculator.inputDigit(key);
        calculator.updateDisplay();
    }
    else if (key === 'decimal') {
        calculator.inputDecimal();
        calculator.updateDisplay();
    }
    else if (['add', 'subtract', 'multiply', 'divide'].includes(key)) {
        calculator.handleOperator(key);
        calculator.updateDisplay();
    }
    else if (key === 'equals') {
        calculator.handleOperator(null);
        calculator.updateDisplay();
    }
    else if (key === 'clear') {
        calculator.clear();
        calculator.updateDisplay();
    }
    else if (key === 'plusMinus') {
        calculator.plusMinus();
        calculator.updateDisplay();
    }
    else if (key === 'percentage') {
        calculator.percentage();
        calculator.updateDisplay();
    }
}); 