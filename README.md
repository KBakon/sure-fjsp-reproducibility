# SURE-FJSP numerical evidence package

SURE-FJSP studies compound tail risk in fixed flexible job-shop schedules. This package supports the GEN1 scientific object, freeze handoff SHA256 `4892e75b09ee72f35077b32f12b00c93c59ea1f481a11657b739e7ef0cafefeb`, and manuscript review PDF SHA256 `31be29baff93de2080c7faa818417812ce8535f3e265bbe4dbbb3a814960141e`. These identifiers identify project records; the manuscript and freeze handoff are not redistributed here.

The generated schedule-risk, transport, bootstrap and support tables permit recomputation of RMSE ratios, intervals, paired wins and the isolated decision screen behind the main cross-severity table and forest plot. The verification reads only these data; it does not run simulations or fit a model. It cannot independently reconstruct CVaR from replication outcomes, regenerate the original moderate analyses, or verify end-to-end simulation. The supplied bootstrap draws support percentile interval checking; they do not by themselves establish how the draws were generated. Read `docs/DATA_DICTIONARY.md` and `docs/PROVENANCE.md` for scope, lineage and limitations.

## Verify

From the package root, with Python 3.11 or newer:

```text
python code/verify.py
```

The script checks payload checksums, row counts, absolute-score selection, schedule-level errors, model RMSE, ratio and percentile intervals. It uses only Python's standard library. `environment/README.md` describes this limited environment.

## Benchmark sources and exclusions

This package contains project-generated summary data, not benchmark instance files, replay samples, operation/machine schedules, historical source, simulation executables, or unresolved legacy modules. Original inputs must be obtained independently under applicable terms: Brandimarte (1993), DOI https://doi.org/10.1007/BF02023073, with an academic source index at https://bda.univie.ac.at/research/data-instances; Hurink, Jurisch and Thole (1994), DOI https://doi.org/10.1007/BF01719451, with a research mirror at https://github.com/SchedulingLab/fjsp-instances. Host availability does not establish redistribution permission. Verify source contents and rights directly before use. Acquisition, dependencies and a full rerun have not been tested by this package. The project does not grant rights in third-party benchmarks.

## Licences and citation

The project-created verification code `code/verify.py` is licensed under the MIT License; see `code/LICENSE`. Project-generated data and project-created release documentation are licensed under CC BY 4.0; see `LICENSES.md` for the file-by-file mapping and attribution guidance. No licence in this package applies to external benchmark material, which is not included.

Please cite this versioned artifact using `CITATION.cff`. Add manuscript bibliographic details and actual public identifiers only after publication. Version v1.0.0 is permanently archived on Zenodo: https://doi.org/10.5281/zenodo.24076119. See `RELEASE_NOTES.md` for this version and `MANIFEST.csv` and `SHA256SUMS.txt` for package inventory and integrity.
