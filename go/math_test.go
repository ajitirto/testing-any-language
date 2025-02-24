package math

import "testing"

func TestTambah(t *testing.T) {
        hasil := Tambah(2, 3)
        if hasil != 5 {
                t.Errorf("Tambah(2, 3) seharusnya 5, tetapi mendapatkan %d", hasil)
        }
}