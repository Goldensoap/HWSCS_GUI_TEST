#include <stdio.h>

unsigned int cal_crc(unsigned int *ptr, int len);

unsigned int cal_crc(unsigned int *ptr, int len)
{
    unsigned int Polynomial = 0x04c11db7;
    unsigned int    xbit;
    unsigned int    data;
    unsigned int    CRC = 0xFFFFFFFF;    // init
    while (len--) {
        xbit = 1 << 31;

        data = *ptr++;
        //printf("%x\r\n",data);
        for (int bits = 0; bits < 32; bits++) {
            if (CRC & 0x80000000) {
                CRC <<= 1;
                CRC ^= Polynomial;
            }
            else
                CRC <<= 1;
            if (data & xbit)
                CRC ^= Polynomial;

            xbit >>= 1;
        }
    }
    //printf("%x\r\n",CRC);
    return CRC;
}
