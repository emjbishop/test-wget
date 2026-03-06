version 1.0

workflow test_wget {
    call download_file

    output {
        File downloaded = download_file.outfile
    }
}

task download_file {
    command <<<
        set -euo pipefail
        wget -O README.md "https://raw.githubusercontent.com/getwilds/wilds-wdl-library/main/README.md"
    >>>

    runtime {
        docker: "ubuntu:22.04"
        cpu: 1
        memory: "2 GB"
    }

    output {
        File outfile = "README.md"
    }
}
