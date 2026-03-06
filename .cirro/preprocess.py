#!/usr/bin/env python3
import json
from cirro.helpers.preprocess_dataset import PreprocessDataset


def main():
    ds = PreprocessDataset.from_running()
    setup_inputs(ds)
    setup_options(ds)


def write_json(fp, obj, indent=4) -> None:
    with open(fp, "wt") as handle:
        json.dump(obj, handle, indent=indent)


def setup_inputs(ds: PreprocessDataset):
    ds.logger.info("Formatting inputs")
    write_json("inputs.0.json", {
        "test_wget.url": ds.params.get("url", "https://raw.githubusercontent.com/getwilds/wilds-wdl-library/main/README.md")
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
