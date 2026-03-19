version 1.0

workflow test_wget {
    input {
        String url = "https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR609/001/ERR6090701/ERR6090701_1.fastq.gz"
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
        docker: "getwilds/ena-tools:2.1.1"
        cpu: 1
        memory: "2 GB"
    }

    output {
        File outfile = "outfile"
    }
}
