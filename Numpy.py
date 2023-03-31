{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cdcc0198",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6 7]\n",
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([1,2,3,4,5,6,7])\n",
    "print(a)\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "90639ba4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]]\n",
      "\n",
      " [[0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]]\n",
      "\n",
      " [[0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]]\n",
      "\n",
      " [[0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]]\n",
      "\n",
      " [[0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]\n",
      "  [0. 0. 0. 0. 0. 0.]]]\n"
     ]
    }
   ],
   "source": [
    "zero_array = np.zeros(shape = (5,3,6))\n",
    "print(zero_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f5a769d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 1.]\n"
     ]
    }
   ],
   "source": [
    "um_array = np.ones(2)\n",
    "print(um_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d61e426",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1.24610859e-306  1.06820579e-311 -0.00000000e+000]\n"
     ]
    }
   ],
   "source": [
    "vazio_array = np.empty(3)\n",
    "print(vazio_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "eba465a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 50  80 110 140 170]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(50,200,30)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "02d8682f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7 8 9]\n",
      "[ 3  5  7  9 11 13]\n"
     ]
    }
   ],
   "source": [
    "zero_dez = np.arange(10)\n",
    "print(zero_dez)\n",
    "pula_dois = np.arange(3,15,2)\n",
    "print(pula_dois)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5450634c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([ 0.,  5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55., 60.,\n",
      "       65., 70., 75., 80., 85., 90., 95.]), 5.0)\n"
     ]
    }
   ],
   "source": [
    "array_linear = np.linspace(0,100, num = 20, endpoint = False, retstep = True)\n",
    "print(array_linear)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9d9a9d7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
