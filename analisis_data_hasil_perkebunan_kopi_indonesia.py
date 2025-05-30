# -*- coding: utf-8 -*-
"""Analisis Data Hasil Perkebunan Kopi Indonesia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AXYdFbfhU6Hh_6LfqUQwsafM8ZLK8wxq
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

luasdanproduksi = pd.read_excel("Luas dan produksi.xlsx")
luasdanproduksi

ekspor = pd.read_excel("Nilai ekspor.xlsx")
ekspor

gabungan = pd.concat([luasdanproduksi, ekspor], ignore_index=True)
gabungan.to_csv("gabungan_vertikal.csv", index=False)

gabungan

gabungan = gabungan.drop(index=[38,57], errors='ignore')
gabungan

gabungan.describe(include="all")

top5_provinsi = gabungan.nlargest(5, 'Luas Areal Perkebunan Kopi (Ribu Hektar)')

plt.figure(figsize=(7, 3))

sns.barplot(
    x='38 Provinsi',
    y='Luas Areal Perkebunan Kopi (Ribu Hektar)',
    data=top5_provinsi,
    label='Luas Areal',
    color='skyblue'
)

ax2 = plt.gca().twinx()
sns.lineplot(
    x='38 Provinsi',
    y='Produksi Perkebunan Kopi (Ribu Ton)',
    data=top5_provinsi,
    marker='o',
    color='red',
    ax=ax2,
    label='Hasil Produksi'
)

plt.title('Top 5 Provinsi Berdasarkan Luas Areal dan Hasil Produksi Kopi')
plt.xlabel('Provinsi')
plt.ylabel('Luas Areal (Ribu Hektar)')
ax2.set_ylabel('Hasil Produksi (Ribu Ton)')
plt.tight_layout()

plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Luas Areal Perkebunan Kopi (Ribu Hektar)', y='Produksi Perkebunan Kopi (Ribu Ton)', data=gabungan)
plt.title('Luas Areal vs Hasil Produksi per Provinsi')
plt.xlabel('Luas Areal Perkebunan Kopi (Ribu Hektar)')
plt.ylabel('Produksi Perkebunan Kopi (Ribu Ton)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

ax1 = sns.lineplot(x='Negara Tujuan', y='Nilai FOB (US$)', data=gabungan, color='red', marker='o', label='Nilai FOB (US$)')
plt.xticks(rotation=45, ha='right')

ax2 = plt.gca().twinx()
sns.barplot(x='Negara Tujuan', y='Berat Bersih Ekspor Kopi (Ton)', data=gabungan, color='blue', ax=ax2, label='Berat Bersih (Ton)')
plt.xticks(rotation=45, ha='right')

plt.title('Berat Bersih dan Nilai FOB dari negara tujuan ekspor kopi indonesia')
plt.xlabel('Negara Tujuan')
plt.ylabel('Nilai FOB')
ax1.set_ylabel('Nilai FOB (US$)')
ax2.set_ylabel('Berat Bersih Ekspor Kopi (Ton)')

handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

all_handles = handles + handles2
all_labels = ["Merah: " + labels[0], "Biru: " + labels2[0]]

plt.legend(all_handles, all_labels, loc='upper left')

plt.tight_layout()
plt.show()

produksi_total = gabungan['Produksi Perkebunan Kopi (Ribu Ton)'].sum()
ekspor_total = gabungan['Berat Bersih Ekspor Kopi (Ton)'].sum()

data = {
    'Produksi': produksi_total,
    'Ekspor': ekspor_total
}

labels = list(data.keys())
sizes = list(data.values())

plt.figure(figsize=(3, 3))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Perbandingan Total Produksi dan Ekspor Kopi')
plt.axis('equal')
plt.show()

