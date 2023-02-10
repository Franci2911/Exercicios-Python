{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O faturamento foi de 1000 e o lucro foi de 600 \n",
      "O faturamento foi de 1000 e o lucro foi de 600\n"
     ]
    }
   ],
   "source": [
    "faturamento = 1000\n",
    "custo = 400\n",
    "\n",
    "lucro = faturamento - custo\n",
    "\n",
    "# com format\n",
    "print('O faturamento foi de {} e o lucro foi de {} '.format(faturamento, lucro) )\n",
    "\n",
    "# com f.string\n",
    "print(f'O faturamento foi de {faturamento} e o lucro foi de {lucro}')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "faturamento = float(input('Insira o faturamento: '))\n",
    "custo = float(input('Insira o custo: '))\n",
    "\n",
    "lucro = faturamento - custo \n",
    "\n",
    "print(lucro)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "nome = input('digite o seu nome: ')\n",
    "print(nome)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "916dbcbb3f70747c44a77c7bcd40155683ae19c65e1c03b4aa3499c5328201f1"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
