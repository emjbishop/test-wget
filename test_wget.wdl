version 1.0

workflow test_wget {
    input {
        String url = "https://raw.githubusercontent.com/getwilds/wilds-wdl-library/main/README.md"
    }

    call download_file { input: url = url }

    output {
        File downloaded = download_file.outfile
    }
}

task download_file {
    input {
        String url = "https://raw.githubusercontent.com/getwilds/wilds-wdl-library/main/README.md"
    }

    command <<<
        set -euo pipefail
        wget -O outfile "~{url}"
    >>>

    runtime {
        docker: "ubuntu:22.04"
        cpu: 1
        memory: "2 GB"
    }

    output {
        File outfile = "outfile"
    }
}
