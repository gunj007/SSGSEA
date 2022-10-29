# SSGSEA

Single-sample GSEA (ssGSEA), an extension of Gene Set Enrichment Analysis (GSEA), calculates separate enrichment scores for each pairing of a sample and gene set.
Each ssGSEA enrichment score represents the degree to which the genes in a particular gene set are coordinately up- or down-regulated within a sample.

		Dataset : previous DEG files was converted into log values matrix wes continue with it.

read the log_values , produce zscore the ssgsea output for comparative analysis
then we take an ideal marker's gene data plot Heatmap for zscore

# Heatmap 
![image](https://user-images.githubusercontent.com/110597928/198850678-c8a266b8-15f8-4a2b-a81c-55bb31d80c05.png)

	   in the heatmap shows till 0 to-2 down-regulated genes (green) and from 0 to 2 up-regulated genes(orange)
