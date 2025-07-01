---
lesson_title: Dart & Flutter Dasar hingga Menengah
lesson_slug: dart-flutter-dasar-menengah
keywords: [dart, flutter, mobile, cross-platform, ui, widget]
objective: Memberikan pemahaman menyeluruh tentang bahasa Dart dan framework Flutter, mulai sintaks dasar hingga pola arsitektur aplikasi lintas-platform.
level: beginner
---

# Dart

Dart adalah bahasa pemrograman modern yang dikembangkan Google sejak 2011 untuk menyelesaikan kebutuhan UI lintas-platform dengan performa nyaris _native_. Berkat kombinasi _AOT_ (Ahead-of-Time) dan _JIT_ (Just-in-Time), Dart memungkinkan **hot-reload** saat pengembangan dan menghasilkan binary mesin efisien saat rilis.

---

## 1 · Sintaks & Fitur Inti

| Konsep | Contoh | Keterangan Ringkas |
|--------|--------|--------------------|
| Deklarasi Variabel | `var x = 10; const pi = 3.14;` | `var` tipe-inferensi, `final/const` _immutable_. |
| Fungsi Singkat | `int add(int a, int b) => a + b;` | Arrow syntax. |
| _Null Safety_ | `String? name;` | Compiler mencegah _null-pointer crash_. |
| Koleksi | `List<int> nums = [1,2,3];` | `List`, `Set`, `Map` generik & literasi ringkas. |
| Cascade | `object..method1()..method2();` | Panggilan berantai, mempercepat builder pattern. |
| Async-Await | `var data = await fetch();` | _Futures_ bawaan tanpa kata kunci `Promise`. |

> **Tips** – Gunakan mode **sound null-safety** (default Dart 3) untuk catch bug di compile-time.

---

## 2 · Flutter Fundamentals

| Elemen | Contoh | Fungsi |
|--------|--------|--------|
| Widget | `Text('Hello')`, `Container()` | Blok UI terkecil, semuanya widget. |
| Layout | `Row`, `Column`, `Stack`, `Flex` | Penyusunan posisi responsif. |
| State Management | `setState`, **Provider**, Riverpod, BLoC | Mengelola perubahan UI + business logic. |
| Routing & Navigation | `Navigator.push()` | Perpindahan halaman, _deeplink_. |
| Theming | `ThemeData(...)` | Global color‐scheme & typography. |

---

## 3 · Tooling & Build Pipeline

| Tool | Fungsi | Highlight |
|------|--------|-----------|
| **Flutter CLI** | `flutter doctor`, `flutter build` | Diagnosis SDK & build multiplatform. |
| **pub.dev** | Registry paket Dart/Flutter | 50 k+ paket (2025). |
| `dart format` & `dart analyze` | Formatter & linter | Menjaga konsistensi kode. |
| `melos` | Workspace monorepo multi-package | Cocok untuk proyek besar plugin + app. |

---

## 4 · Ekosistem Paket Populer

| Kategori | Paket | Deskripsi |
|----------|-------|-----------|
| UI Kit | `flutter_bloc`, `riverpod`, `go_router` | Arsitektur & navigasi. |
| HTTP/API | `dio`, `http`, `retrofit` | Client HTTP fitur lengkap + interceptors. |
| State Persistence | `hive`, `shared_preferences` | Local storage NoSQL & key-value. |
| Native Bridge | `camera`, `geolocator`, `permission_handler` | Akses fitur perangkat. |

---

## 5 · Kelebihan Dart & Flutter

1. **Hot-reload** mempercepat iterasi UI.  
2. **Single codebase** → native iOS, Android, web, desktop.  
3. **Sound type system** menekan bug logic.  
4. **Rendering engine Skia** → performa & konsistensi tampilan.

---

## 6 · Kekurangan

* Ekosistem belum seluas npm/PyPI; beberapa SDK native perlu ditulis manual.  
* Ukuran binary awal (≈ 4–7 MB) lebih besar dibanding Kotlin/Swift murni.  
* Pasar kerja global masih lebih kecil dibanding JavaScript & Python.

---

## 7 · Studi Kasus Nyata

| Perusahaan/Proyek | Keterangan |
|-------------------|------------|
| **Google Classroom** (Mobile) | Migrasi sebagian fitur ke Flutter untuk pace UI seragam. |
| **ByteDance** - _Xianyu_ | Aplikasi e-commerce multi-platform 50 M pengguna. |
| **BMW iDrive** | Prototipe UI infotainment menggunakan Flutter Desktop. |

---

## 8 · Jalur Karier

1. **Flutter Mobile Engineer** – membangun aplikasi lintas iOS/Android.  
2. **Full-Stack Dart** – menggunakan `Dart Frog` / `Shelf` di backend, Flutter di front.  
3. **Embedded UI Developer** – memanfaatkan Flutter di IoT & otomotif.

---

## 9 · Roadmap Belajar Disarankan

| Tahap | Target | Durasi |
|-------|--------|--------|
| Sintaks Dart + Null Safety | Variabel, fungsi, koleksi | 1 minggu |
| Flutter UI Basics | Widget, layout | 1 minggu |
| State Mgmt | Provider/Riverpod | 1 minggu |
| API & JSON | Dio + model `fromJson` | 1 minggu |
| Deployment | Play Store & App Store | 1 minggu |
| Advanced | Animasi, testing, CI/CD | 2 minggu |

---

### Referensi Lanjut

* **Flutter Documentation** – docs.flutter.dev  
* _Flutter Apprentice_ – kode lab raywenderlich  
* _Pragmatic Flutter_ – PragProg 2024

---

> ✅ **Sasaran Lesson**: Setelah menyelesaikan modul ini, pelajar dapat menulis aplikasi Flutter sederhana dengan arsitektur state-management bersih, memahami build pipeline multi-platform, dan menilai trade-off Dart vs stack lain.
