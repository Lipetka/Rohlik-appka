# Rohlik application

## What is this project about?

This project is trying to solve the problem when multiple people order or buy products from one store and need a fast way to split up bills. This application is focused on [Rohlik](https://www.rohlik.cz/) online grocery store. 

## App capabilities

Extract data from PDF receipt, figure out what is an item and its cost. Display these data in simple table with ticks and ratios and calculate cost for each person or group (TBD).

## Receipt example

Receipt example is in located in [Ver.2/files/pdfFileName.pdf](/Ver.2/files/pdfFileName.pdf) this file is default target of getContents function:


```
def getContents(file_name = "Ver.2/files/pdfFileName.pdf"):
```
