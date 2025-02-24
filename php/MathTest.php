// tests/KalkulatorTest.php
<?php

use PHPUnit\Framework\TestCase;

require_once 'Math.php'; // Sesuaikan path

class MathTest extends TestCase {
    private $math;

    protected function setUp(): void {
        $this->math = new Math();
    }

    public function testTambah() {
        $hasil = $this->math->tambah(2, 3);
        $this->assertEquals(5, $hasil);
    }

    public function testKurang() {
        $hasil = $this->math->kurang(5, 2);
        $this->assertEquals(3, $hasil);
    }
}