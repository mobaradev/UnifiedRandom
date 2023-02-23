using System;

/*
    UnifiedRandom version 1.00
    by Michal Obara (mobaradev) mobaradev@yahoo.com http://mobaradev.com
    MIT License
*/

public class UnifiedRandom
{
    private string _seed;
    private int _index = 0;

    public UnifiedRandom()
    {
        this._seed = ((long)DateTime.UtcNow.Subtract(DateTime.UnixEpoch).TotalSeconds).ToString();
    }

    public UnifiedRandom(string seed)
    {
        this._seed = seed;
    }

    private double _getSignValue(char sign) {
        if (sign == '0') return (1f/16f)/2f;
        if (sign == '1') return (1f/16f + 2f/16f)/2f;
        if (sign == '2') return (2f/16f + 3f/16f)/2f;
        if (sign == '3') return (3f/16f + 4f/16f)/2f;
        if (sign == '4') return (4f/16f + 5f/16f)/2f;
        if (sign == '5') return (5f/16f + 6f/16f)/2f;
        if (sign == '6') return (6f/16f + 7f/16f)/2f;
        if (sign == '7') return (7f/16f + 8f/16f)/2f;
        if (sign == '8') return (8f/16f + 9f/16f)/2f;
        if (sign == '9') return (9f/16f + 10f/16f)/2f;
        if (sign == 'a' || sign == 'A') return (10f/16f + 11f/16f)/2f;
        if (sign == 'b' || sign == 'B') return (11f/16f + 12f/16f)/2f;
        if (sign == 'c' || sign == 'C') return (12f/16f + 13f/16f)/2f;
        if (sign == 'd' || sign == 'D') return (13f/16f + 14f/16f)/2f;
        if (sign == 'e' || sign == 'E') return (14f/16f + 15f/16f)/2f;
        if (sign == 'f' || sign == 'F') return (15f/16f + 16f/16f)/2f;

        return 0;
    }

    private string _hash(string text)
    {
        using (var sha = new System.Security.Cryptography.SHA256Managed())
        {
            byte[] textBytes = System.Text.Encoding.UTF8.GetBytes(text);
            byte[] hashBytes = sha.ComputeHash(textBytes);

            string hash = BitConverter
                .ToString(hashBytes)
                .Replace("-", String.Empty);

            return hash;
        }
    }

    public double GetValue()
    {
        string toHash = this._seed + "-" + this._index;
        string hash = this._hash(toHash);

        double value = 0;

        for (int i = 0; i < 8; i++)
        {
            char sign = hash[i];
            double signValue = this._getSignValue(sign);

            if (i == 0)
            {
                value = signValue;
            }
            else
            {
                float delta = 1;
                for (int j = 0; j < i; j++) delta = delta/16;

                if (this._getSignValue(hash[15 - i]) < 0.5)
                {
                    value -= signValue * delta;
                }
                else
                {
                    value += signValue * delta;
                }

                if (value < 0) value = 0;
                else if (value > 1) value = 1;
            }
        }

        this._index++;
        return value;
    }

    public int GetNumber(int min, int max)
    {
        double value = this.GetValue();

        int intervals = max - min + 1;
		return (int)Math.Floor((intervals * value));
        return 0;
    }
}
