#!/usr/bin/env python3
import json
import logging
import os
import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset, read_json


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s [PreprocessDataset] %(message)s'
    )
    logger = logging.getLogger(__name__)

    dataset_root = os.getenv("PW_S3_DATASET")
    config_dir = f"{dataset_root}/config"
    logger.info(f"Reading params from {config_dir}")

    params = read_json(f"{config_dir}/params.json")

    try:
        metadata = read_json(f"{config_dir}/metadata.json")
    except Exception:
        metadata = {}

    ds = PreprocessDataset(
        samplesheet=pd.DataFrame(columns=["sample"]),
        files=pd.DataFrame(columns=["sample", "file"]),
        params=params,
        metadata=metadata,
        dataset_root=dataset_root
    )

    setup_inputs(ds)
    setup_options(ds)


def write_json(fp, obj, indent=4) -> None:
    with open(fp, "wt") as handle:
        json.dump(obj, handle, indent=indent)


def setup_inputs(ds: PreprocessDataset):
    ds.logger.info("Formatting inputs")
    write_json("inputs.0.json", {
        "test_wget.url": ds.params.get("url")
    })


def setup_options(ds: PreprocessDataset):
    options = {
        "workflow_failure_mode": "ContinueWhilePossible",
        "write_to_cache": True,
        "read_from_cache": True,
        "default_runtime_attributes": {
            "maxRetries": 1
        },
        "final_workflow_outputs_dir": ds.params["out_dir"],
        "use_relative_output_paths": True
    }
    write_json("options.json", options)


if __name__ == "__main__":
    main()
