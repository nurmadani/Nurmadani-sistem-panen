{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyORYkS01qTH7IEV8VY7JVnh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nurmadani/Nurmadani-sistem-panen/blob/main/panen.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "90HvqeCsTorn",
        "outputId": "cba5ec43-df68-40c2-e96c-d2b15ae3fca3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=== SISTEM PENCATATAN HASIL PANEN ===\n",
            "Jumlah panen : 100 kg\n",
            "Harga per kg : Rp 8000\n",
            "Total hasil panen : Rp 800000\n"
          ]
        }
      ],
      "source": [
        "# Program Penghitung Total Hasil Panen\n",
        "\n",
        "def hitung_total_panen(jumlah_kg, harga_per_kg):\n",
        "    return jumlah_kg * harga_per_kg\n",
        "\n",
        "\n",
        "# Data hasil panen\n",
        "jumlah_panen = 100\n",
        "harga_per_kg = 8000\n",
        "\n",
        "# Menghitung total\n",
        "total = hitung_total_panen(jumlah_panen, harga_per_kg)\n",
        "\n",
        "# Menampilkan hasil\n",
        "print(\"=== SISTEM PENCATATAN HASIL PANEN ===\")\n",
        "print(\"Jumlah panen :\", jumlah_panen, \"kg\")\n",
        "print(\"Harga per kg :\", \"Rp\", harga_per_kg)\n",
        "print(\"Total hasil panen : Rp\", total)"
      ]
    }
  ]
}