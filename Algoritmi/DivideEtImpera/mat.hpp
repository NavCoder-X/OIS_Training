#ifndef _MAT_HPP
#define _MAT_HPP

#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cassert>

template <typename T>
struct Mat {
    static Mat<T> load(std::istream& f) {
        unsigned rows, cols;
        f >> rows >> cols;
        Mat<T> m(rows, cols);
        for(unsigned i = 0; (i < rows * cols) && (f >> m._data[i]); i++);
        return m;
    }

    static Mat<T> load(const std::string& path) {
        std::ifstream f(path);
        return load(f);
    }

    friend std::ostream& operator <<(std::ostream& cout, const Mat<T>& m) {
        const T *p = m._data.data();
        for(unsigned i = 0; i < m.rows; i++) {
            for(unsigned j = 0; j < m.cols; j++)
                cout << *p++ << " ";
            cout << std::endl;
        }
        return cout;
    }

    Mat(unsigned rows = 0, unsigned cols = 0) : rows(rows), cols(cols) {
        _data.resize(rows * cols);
    }

    Mat(unsigned rows, unsigned cols, T val) : Mat(rows, cols) {
        std::fill(_data.begin(), _data.end(), val);
    }

    Mat(unsigned rows, unsigned cols, const std::vector<T>& il) : Mat(rows, cols) {
        assert(il.size() == rows * cols);
        _data.resize(il.size());
        std::copy(il.begin(), il.end(), _data.begin());
    }

    T* operator[](unsigned row) { return _data.data() + row * cols; }
    const T* operator[](unsigned row) const { return _data.data() + row * cols; }

    bool find(T val, unsigned *row, unsigned *col) const {
        auto it = std::find(_data.cbegin(), _data.cend(), val);
        bool found = (it != _data.cend());
        if(found) {
            unsigned n = it - _data.cbegin();
            *row = n / cols;
            *col = n % cols;
        }
        return found;
    }

    const unsigned rows, cols;
    std::vector<T> _data;
};

#endif // _MAT_HPP
