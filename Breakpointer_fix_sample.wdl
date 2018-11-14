task breakpointer_fix_sample_task_1 {
    File input_SV_tsv
    String id 
    String stub
    Float? ram_gb
    Int? local_disk_gb
    Int? num_preemptions

    String ext="${if defined(stub) then '.Breakpointer_fix_SV.tsv' else 'Breakpointer_fix_SV.tsv'}"

    command {
        set -euo pipefail

        echo "${input_SV_tsv}"
        echo "${blacklist_bed}"
        echo "${id}"
        echo "${stub}"

        ls -lath
        
        python /opt/src/breakpointer_fix_sample.py -d ${input_SV_tsv} -i ${id} -s ${stub} 

        ls -lath        
    }

    output {
        File breakpointer_fix_sample_tsv="${id}.${stub}${ext}"
    }

    runtime {
        docker : "chipstewart/breakpointer_fix_sample_task_1:1"
        memory: "${if defined(ram_gb) then ram_gb else '2'}GB"
        disks : "local-disk ${if defined(local_disk_gb) then local_disk_gb else '10'} HDD"
        preemptible : "${if defined(num_preemptions) then num_preemptions else '0'}"
    }

    meta {
        author : "Chip Stewart"
        email : "stewart@broadinstitute.org"
    }
}

workflow Breakpointer_fix_sample {

    call breakpointer_fix_sample_task_1 
}
