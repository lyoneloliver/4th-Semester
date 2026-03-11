## Bagaimana Teori Bayes Digunakan dalam Algoritma Naive Bayes

Algoritma **Naive Bayes** menggunakan **Teori Bayes** untuk menghitung probabilitas suatu data termasuk ke dalam kelas tertentu berdasarkan fitur yang dimiliki data tersebut. Dengan kata lain, algoritma ini digunakan untuk menentukan **kelas yang paling mungkin** untuk sebuah data berdasarkan informasi yang tersedia.

Teori Bayes dinyatakan dengan rumus:

P(C | X) = (P(X | C) × P(C)) / P(X)

Di dalam konteks klasifikasi menggunakan Naive Bayes:

- **C** merupakan kelas atau kategori yang ingin diprediksi  
- **X** merupakan data yang terdiri dari beberapa fitur (x₁, x₂, ..., xₙ)  
- **P(C | X)** adalah probabilitas bahwa data X termasuk dalam kelas C  
- **P(C)** adalah probabilitas awal dari kelas C (prior probability)  
- **P(X | C)** adalah probabilitas munculnya data X jika diketahui kelasnya adalah C  
- **P(X)** adalah probabilitas keseluruhan dari data X

Dalam proses klasifikasi, Naive Bayes akan menghitung nilai **P(C | X)** untuk setiap kelas yang mungkin. Kemudian algoritma akan memilih kelas dengan probabilitas terbesar sebagai hasil prediksi.

Karena sebuah data biasanya memiliki banyak fitur, menghitung **P(X | C)** secara langsung akan sangat kompleks. Oleh karena itu, Naive Bayes membuat asumsi sederhana yaitu **setiap fitur dianggap independen satu sama lain jika kelasnya sudah diketahui**. Dengan asumsi ini, perhitungan dapat disederhanakan menjadi:

P(X | C) = P(x₁ | C) × P(x₂ | C) × ... × P(xₙ | C)

Dengan demikian, algoritma cukup menghitung probabilitas masing-masing fitur terhadap kelas, kemudian mengalikan semua probabilitas tersebut dengan probabilitas awal kelas **P(C)**. Kelas dengan nilai probabilitas terbesar akan dipilih sebagai hasil klasifikasi.