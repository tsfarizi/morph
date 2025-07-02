# Rangkuman Materi Belajar Dart

Dart adalah bahasa pemrograman modern yang dirancang untuk efisiensi, portabilitas, dan produktivitas. Digunakan secara luas dalam pengembangan aplikasi multiplatform seperti Flutter untuk mobile dan web, Dart memiliki sintaks yang bersih dan kuat untuk membangun aplikasi UI maupun CLI. Bahasa ini mendukung paradigma OOP, null safety, serta berbagai fitur lanjutan seperti closure, asynchronous, dan modularisasi. Materi berikut dirancang agar pengguna dapat mempelajari Dart secara terstruktur, praktis, dan menyeluruh.

## Implementasi Umum Dart

| Konteks Penggunaan       | Implementasi Umum                                     | Tool/Framework yang Mendukung   |
|--------------------------|-------------------------------------------------------|---------------------------------|
| **Mobile Development**   | Aplikasi Android/iOS multiplatform                   | Flutter                         |
| **Web Development**      | Web interaktif modern dengan kompilasi ke JS         | Flutter Web, Dart Web           |
| **CLI Tools**            | Aplikasi terminal, utilities baris perintah          | dart:io, args                   |
| **Backend/API**          | REST API, server HTTP ringan                         | Dart Shelf, Aqueduct (deprecated)|
| **Desain Modular**       | Manajemen paket, struktur file terpisah              | pub.dev, dart pub, import/export|

---

## Halaman 1: Sintaks Dasar Dart
- **Topik**: `void main()`, `print()`, komentar, struktur file `.dart`
- **Deskripsi**: Dasar pemrograman Dart dimulai dari fungsi `main()` sebagai titik awal program. Penggunaan `print()` untuk output, penulisan komentar satu dan banyak baris, serta struktur file `.dart` yang rapi memperkenalkan alur kode yang jelas.

## Halaman 2: Variabel dan Tipe Data
- **Topik**: `var`, `final`, `const`, `int`, `double`, `String`, `bool`, `dynamic`
- **Deskripsi**: Dart adalah bahasa statis dengan dukungan type inference. Materi ini membahas penugasan variabel, perbedaan `final` dan `const`, serta tipe data dasar yang umum digunakan.

## Halaman 3: Operasi dan Ekspresi
- **Topik**: operator aritmatika, logika, ternary, null-aware (`??`, `??=`, `?.`)
- **Deskripsi**: Dart mendukung berbagai ekspresi logis dan matematis. Bagian ini membahas operator dasar hingga ekspresi kondisional dan null-aware yang sering digunakan dalam pengembangan aplikasi nyata.

## Halaman 4: Struktur Kontrol
- **Topik**: `if`, `switch`, `for`, `while`, `do...while`, `break`, `continue`
- **Deskripsi**: Struktur kontrol memberikan alur dinamis dalam eksekusi program. Materi ini mencakup percabangan dan perulangan lengkap dengan implementasi praktis.

## Halaman 5: Fungsi dan Scope
- **Topik**: `=>` arrow function, named & optional parameters, closure, lexical scope
- **Deskripsi**: Fungsi di Dart sangat fleksibel dengan dukungan parameter opsional dan closure. Bagian ini juga membahas ruang lingkup variabel dan bagaimana lexical scoping memengaruhi akses data dalam program.

## Halaman 6: Struktur Data Kolektif
- **Topik**: `List`, `Set`, `Map`, `.add()`, `.contains()`, `.forEach()`
- **Deskripsi**: Struktur data kolektif merupakan elemen kunci dalam manajemen koleksi data. Materi ini mengeksplorasi perbedaan dan manipulasi dasar antar ketiganya.

## Halaman 7: Penanganan Error
- **Topik**: `try`, `catch`, `on`, `finally`, exception custom
- **Deskripsi**: Dart menyediakan sistem penanganan error yang ekspresif. Bagian ini menjelaskan cara menangani exception, membedakan error umum, serta membuat custom exception untuk kasus spesifik.

## Halaman 8: Paradigma dan Gaya Penulisan
- **Topik**: Class-based OOP, null safety, `mixin`, `abstract class`, `typedef`
- **Deskripsi**: Dart mengadopsi paradigma pemrograman berorientasi objek dengan fitur modern seperti null safety dan mixin. Materi ini membahas prinsip desain dan gaya penulisan kode Dart yang ringkas dan ekspresif.

## Halaman 9: Refaktor dan Performance Dasar
- **Topik**: modularisasi file, `dart analyze`, profiling ringan (`Stopwatch`)
- **Deskripsi**: Refaktor meningkatkan keterbacaan dan performa. Topik ini mencakup pemisahan fungsi ke file, penggunaan linter, dan teknik profiling ringan untuk mendeteksi bottleneck.

## Halaman 10: Mini-Proyek Dart
- **Topik**: CLI tools, konversi suhu, pembaca file (dart:io)
- **Deskripsi**: Proyek mini ini memberikan latihan langsung dengan membuat aplikasi kecil seperti konverter suhu dan pembaca file menggunakan `dart:io`. Dilengkapi dengan interaksi input/output serta struktur modular.

---