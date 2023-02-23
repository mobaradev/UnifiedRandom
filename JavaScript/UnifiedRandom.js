const crypto = require('crypto');

/*
    UnifiedRandom version 1.00
    by Michal Obara (mobaradev) mobaradev@yahoo.com http://mobaradev.com
    MIT License
*/

class UnifiedRandom {
    seed = "";
    index = 0;

    constructor(seed) {
        if (!seed || seed === "") seed = Date.now().toString();
        this.seed = seed;
    }

    _getSignValue(sign) {
        if (sign === '0') return (1/16)/2;
        if (sign === '1') return (1/16 + 2/16)/2;
        if (sign === '2') return (2/16 + 3/16)/2;
        if (sign === '3') return (3/16 + 4/16)/2;
        if (sign === '4') return (4/16 + 5/16)/2;
        if (sign === '5') return (5/16 + 6/16)/2;
        if (sign === '6') return (6/16 + 7/16)/2;
        if (sign === '7') return (7/16 + 8/16)/2;
        if (sign === '8') return (8/16 + 9/16)/2;
        if (sign === '9') return (9/16 + 10/16)/2;
        if (sign === 'a') return (10/16 + 11/16)/2;
        if (sign === 'b') return (11/16 + 12/16)/2;
        if (sign === 'c') return (12/16 + 13/16)/2;
        if (sign === 'd') return (13/16 + 14/16)/2;
        if (sign === 'e') return (14/16 + 15/16)/2;
        if (sign === 'f') return (15/16 + 16/16)/2;
    }

    getValue() {
        const toHash = this.seed + "-" + this.index;
        const hash = crypto.createHash('sha256').update(toHash).digest('hex');

        let value = 0;

        for (let i = 0; i < 8; i++) {
            let sign = hash[i];
            let signValue = this._getSignValue(sign);

            if (i === 0) {
                value = signValue;
            } else {
                let delta = 1;
                for (let j = 0; j < i; j++) delta = delta/16;

                if (this._getSignValue(hash[15 - i]) < 0.5) {
                    value -= signValue * delta;
                } else {
                    value += signValue * delta;
                }
                if (value < 0) value = 0;
                else if (value > 1) value = 1;
            }
        }

        this.index++;
        return value;
    }

    getNumber(min, max) {
        const value = this.getValue();
        const intervals = max - min + 1;

        return Math.floor(intervals * value);
    }
}

export default UnifiedRandom;
