{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e619d1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average purchase items: \n",
      "20.6\n"
     ]
    }
   ],
   "source": [
    "import array as arr\n",
    "\n",
    "def display_ave():\n",
    "    print(\"Average purchase items: \")\n",
    "    \n",
    "def get_ave():\n",
    "    n = len (items)\n",
    "    get_sum = sum (items)\n",
    "    mean = get_sum / n\n",
    "    m = str(mean)\n",
    "    print(m)\n",
    "    \n",
    "online_pur = [19, 27, 17, 24, 16]\n",
    "\n",
    "sample_data = arr.array('i', online_pur)\n",
    "items = sample_data[0:5]\n",
    "sample_data_list = items.tolist()\n",
    "\n",
    "display_ave()\n",
    "get_ave()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c272d83",
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
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
