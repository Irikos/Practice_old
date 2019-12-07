
## Comparing two supervised learning algorithms

### SVM vs KNN
Data source: https://www.kaggle.com/loveall/cervical-cancer-risk-classification

### Data description
data.info()

Data columns (total 36 columns): **?** means unknown
| **Header** | **Type** | **Meaning** | 
| -------------- | -------------- | --------------|
| **Age** |  int64 | Age of the patient |
| **Number of sexual partners** | float64 | With which the patient had intercourse.|
| **First sexual intercourse** | float64 | Age when it happened. |
| **Num of pregnancies** | float64 | Total number of pregnancies |
| **Smokes** | float64 | 0 or 1, smokes or not |
| **Smokes (years)** | float64 | For how many years the person has been |
| **Smokes (packs/year)**| float64 | How many packs / years |
| **Hormonal Contraceptives**| float64 | 1 is yes, 0 is no|
| **Hormonal Contraceptives (years)**| float64 | For how many years |
| **IUD** | float64 | Intrauterine device: 1 (yes) or 0 (no) |
| **IUD (years)** | float64 |  For how many years |
| **STDs** | float64 | Any STDs: 1 (yes) or 0 (no) |
| **STDs (number)** | float64 | From 0 to 4 |
| **STDs:condylomatosis** | float64 | yes(1) or no(0) |
| **STDs:cervical condylomatosis** |  float64 | yes(1) or no(0) |
| **STDs:vaginal condylomatosis** | float64 | yes(1) or no(0) |
| **STDs:vulvo-perineal condylomatosis** | float64 | yes(1) or no(0) |
| **STDs:syphilis** | float64 | yes(1) or no(0) |
| **STDs:pelvic inflammatory disease** | float64 | yes(1) or no(0) |
| **STDs:genital herpes** | float64 | yes(1) or no(0) |
| **STDs:molluscum contagiosum** |float64 | yes(1) or no(0) |
| **STDs:AIDS** | float64 | yes(1) or no(0) |
| **STDs:HIV** | float64 | yes(1) or no(0) |
| **STDs:Hepatitis B** | float64 | yes(1) or no(0) |
| **STDs:HPV** | float64 | yes(1) or no(0) |
| **STDs: Number of diagnosis** | int64 | not sure how it differs from number |
| **STDs: Time since first diagnosis** | int64 | Time passed in years. |
| **STDs: Time since last diagnosis** | int64 | Time passed in years. |
| **Dx:Cancer** | int64 | Person had previous cervical cancer diagnostic |
| **Dx:CIN** | int64 | Person had previous diagnostic of Cervical intraepithelial neoplasia |
| **Dx:HPV** | int64 | Person had Human Papilloma Virus |
| **Dx** | int64 | Diagnosys |
| **Hinselmann** | int64 | Hinselmann test: olposcopy using acetic acid |
| **Schiller** | int64 | Schiller test: colposcopy using Lugol iodine |
| **Citology** | int64 | Citology: colposcopy using Lugol iodine examinations |
| **Biopsy** | int64 | Target: Biopsy: colposcopy using Lugol iodine |

| **CervicalCancer** | Inferred variable that is 1 is all 4 test variables are 1 and 0 otherwise. |

The patient has cancer iff Hinselmann, Schiller, Citology and Biopsy ALL are true (1).

