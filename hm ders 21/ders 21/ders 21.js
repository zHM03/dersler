function compareStrings() {
    const string1 = document.getElementById('string1').value;
    const string2 = document.getElementById('string2').value;
    let result;

    if (string1.length > string2.length) {
        result = 'First string is longer (>)';
    } else if (string1.length < string2.length) {
        result = 'Second string is longer (<)';
    } else {
        result = 'Both strings are of equal length (=)';
    }

    document.getElementById('result').textContent = result;
}
