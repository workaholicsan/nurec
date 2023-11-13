# Test System (Neural universit recognition check)

## Colab Examples

[Colab Examples](https://colab.research.google.com/drive/19878-C6WMm1ApNNEw5-Y3Xt-Tskwrgwb?usp=sharing).

## Usage

```bash
!pip install git+https://github.com/AlexNimoy/nurec.git

from nurec import Nurec
```

```python
recognized_data = [{<JSON_PARAMS>}, {...}]

result = Nurec(recognized_data)
```

### Methods

#### accuracy

`result.accuracy()`

returns accuracy like `100.00` or worse

#### details

`result.details()`

```bash
[key] file
distance: Number
expected:
String
received:
String
```

#### total_distance

returns total Levenshtein distance

`result.total_distance()`

Number

## JSON example

```json
{
 "File Name": "",
    "01 Receipt": "",
    "04-01 Counterparty 1": "",
    "04-02 Counterparty 2": "",
    "05 Contract": "",
    "06 Our Company BIN": "",
    "07 Counterparty Bank BIC": "",
    "08 Counterparty Current Account IIC": "",
    "09 Counterparty Payment Purpose Code": "",
    "10 Items Table": [
        {
            "10-01 Item": "",
            "10-02 Unit": "",
            "10-03 Quantity": "",
            "10-04 Price": "",
            "10-05 Amount": ""
        },
    ]
}
```
## Params Table

[Params Table (Google Disc)](https://docs.google.com/spreadsheets/d/14AIRNzPu7_TQo_VaDG64RQo2k1brj8DDg_k--Eqtkzk/edit#gid=0)

| №    | Описание                           | Название поля                        |
| ---- | ---------------------------------- | ------------------------------------ |
| 1    | Номер и Дата Счета                 | 01 Receipt                           |
| 4.1  | БИН и наименование Контрагента 1   | 04-01 Counterparty 1                 |
| 4.2  | БИН и наименование Контрагента 2   | 04-02 Counterparty 2                 |
| 5    | Договор                            | 05 Contract                          |
| 6    | БИН Нашей организации              | 06 Our Company BIN                   |
| 7    | БИК банка Контрагента              | 07 Counterparty Bank BIC             |
| 8    | Расчетный счет (ИИК) Контрагента   | 08 Counterparty Current Account IIC  |
| 9    | Код назначения платежа Контрагента | 09 Counterparty Payment Purpose Code |
| 10   | Информация из табличной части:     | 10 Items Table                       |
| 10.1 | Наименование товара                | 10-01 Item                           |
| 10.2 | Единица измерения                  | 10-02 Unit                           |
| 10.3 | Количество                         | 10-03 Quantity                       |
| 10.4 | Цена                               | 10-04 Price                          |
| 10.5 | Сумма                              | 10-05 Amount                         |
