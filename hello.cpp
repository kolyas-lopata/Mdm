#include <iostream>
#include <cstddef>

// Указатель на функцию — через него будем печатать каждый символ.
using CharPrinter = void (*)(const char*);

void printChar(const char*);
void printString(const char**, const CharPrinter*);

// Печатает один символ, получая его адрес.
void printChar(const char* ch) {
    std::cout << *ch;
}

// Печатает строку, адрес которой спрятан за указателем на указатель,
// а сам вывод выполняется через указатель на функцию.
void printString(const char** str, const CharPrinter* printer) {
    const char* cursor = *str;   // разыменовываем до адреса начала строки
    const char** it = &cursor;   // ещё один уровень косвенности

    while (**it != '\0') {       // смотрим символ через двойное разыменование
        (*printer)(*it);         // печатаем символ по его адресу
        ++(*it);                 // двигаем курсор арифметикой указателей
    }
    std::cout << std::endl;
}

int main() {
    // Динамическая строка: "Hello, World!" = 13 символов + '\0' = 14 байт.
    char* buffer = new char[14];

    // Копируем строку байт за байтом, сдвигая указатели.
    const char* source = "Hello, World!";
    char* dst = buffer;
    const char* src = source;
    while ((*dst++ = *src++)) {}

    // Длина — через арифметику указателей (разность адресов минус терминатор).
    std::ptrdiff_t length = dst - buffer - 1;

    // Упаковываем адрес буфера в указатель на указатель.
    const char* heap = buffer;

    // Берём адрес функции и тоже передаём через указатель.
    CharPrinter printer = &printChar;

    printString(&heap, &printer);

    std::cout << "  (примерено через указатели: "
              << length << " символов)" << std::endl;

    delete[] buffer; // освобождаем динамическую память
    return 0;
}