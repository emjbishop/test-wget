version 1.0

workflow test_wget {
    input {
        String url = "https://github.com/getwilds/wilds-wdl-library/blob/main/README.md"
    }

    call download_file { input: url = url }

    output {
        File downloaded = download_file.outfile
    }
}

task download_file {
    input {
        String url
    }

    command <<<
        set -euo pipefail
        wget -O outfile --no-check-certificate ~{url}
    >>>

    runtime {
        docker: "getwilds/gtf-smash:v8"
        cpu: 1
        memory: "2 GB"
    }

    output {
        File outfile = "outfile"
    }
}
