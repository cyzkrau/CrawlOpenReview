# Crawl paper data from openreview

This repository contains a script designed to scrape and process academic paper data from OpenReview. It outputs detailed information including titles, author IDs, keywords, abstracts, and citation details in JSON format. 

Now, it works for AI conferences in 2024: ICLR, ICML, NeurIPS, and UAI. And the processed data is stored in `./data/`. 

## Usage

Run the script to load data from UAI2024poster with the following command:
```bash
python main.py --year=2024 --name=UAI --type=poster
```

## Output

Here is an example of the JSON output format for one paper: 
```json
{
    {
        "title": "Adaptive Time-Stepping Schedules for Diffusion Models",
        "authorids": [
            "~Yuzhu_Chen1",
            "~Fengxiang_He1",
            "~Shi_Fu1",
            "~Xinmei_Tian1",
            "~Dacheng_Tao1"
        ],
        "keywords": [
            "diffusion models",
            "stepping schedule",
            "generative model"
        ],
        "abstract": "This paper studies how to tune the stepping schedule in diffusion models, which is mostly fixed in current practice, lacking theoretical foundations and assurance of optimal performance at the chosen discretization points. In this paper, we advocate the use of adaptive time-stepping schedules and design two algorithms with an optimized sampling error bound $EB$: (1) for continuous diffusion, we treat $EB$ as the loss function to discretization points and run gradient descent to adjust them; and (2) for discrete diffusion, we propose a greedy algorithm that adjusts only one discretization point to its best position in each iteration. We conducted extensive experiments that show (1) improved generation ability in well-trained models, and (2) premature though usable generation ability in under-trained models. The code is submitted and will be released publicly.",
        "_bibtex": "@inproceedings{\nchen2024adaptive,\ntitle={Adaptive Time-Stepping Schedules for Diffusion Models},\nauthor={Yuzhu Chen and Fengxiang He and Shi Fu and Xinmei Tian and Dacheng Tao},\nbooktitle={The 40th Conference on Uncertainty in Artificial Intelligence},\nyear={2024},\nurl={https://openreview.net/forum?id=lZzriJH2DC}\n}"
    },
}
```


