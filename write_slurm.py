#!/usr/bin/env python3

job_name = "mna.test"
hours = 
queue_name = 
email = "mnalbrit@uark.edu"
time = 

print("#!/usr/bin/env python3")
print("#SBATCH --job-name={job_name}")
print("#SBATCH --partition comp01")
print("#SBATCH --nodes=1")
print("#SBATCH --qos comp")
print("#SBATCH --cpus-per-task=32")
print("#SBATCH --time=00:05:00")
print("#SBATCH --output=%x.%j.out")
print("#SBATCH --error=%x.%j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user={email}")

