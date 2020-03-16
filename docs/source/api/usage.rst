*********
API Usage
*********

- instalation through pypy not yet implemented
- make setup.py installer
- from a python script, call import randhom


This project is organized as an API to be used from a python prompt.

Steps:

- Complete the configuration of the experiment
- All the settings of the experimets are parsed from the configuration
  files using configparser.


Prerequisites
=============

* Put data files on the ``data`` directory.
* Complete the names of the data files in the configuration file
* Directories in out/ must be uppercase

Data
====

Data is stored in the *data* directory.


=========================================  =================================================
 filename                                   contents
=========================================  =================================================
file                                       description 
=========================================  =================================================





Configuration files
===================


.. code-block::
   [dirs]

   # directories

   dir_data = ../data/
   base_in = out/
   base_out = out/

   [exp]
   # experiment, option: cct, glass, rancross, ransplit, zelrec, ran

   experiment = ccvt

   nran = 87**3

   nfiles_max = 200

   # scales (unit must be astropy.units compatible)
   scale_min = 1.
   scale_max = 150.
   scale_nbins = 29
   unit = Mpc


   [output]

   mean_dir = xi_mean/
   sd_dir = xi_sd/



Interactive usage
=================

For a simple test, go to randhom directory and run:

.. code-block::

   $ python sd.py ../set/config.ini


Run experiments at IATE
=======================

In order to use the `HPC services at IATE <https://wiki.oac.uncor.edu/doku.php>`_ the following steps shoul be followed:


1. log in into a cluster (e.g., ``ssh clemente``)
2. git clone or pull the `randhom <https://github.com/mlares/randhom>`_ project.
3. prepare a SLURM script (src/submit_python_jobs.sh)
4. launch the script: ``sbatch submit_python_jobs.sh``


SLURM script example for *clemente* running python in parallel:

.. code-block::
   #!/bin/bash

   # SLURM script for: CLEMENTE
    
   ## Las líneas #SBATCH configuran los recursos de la tarea
   ## (aunque parezcan estar comentadas)

   # More info:
   # http://homeowmorphism.com/articles/17/Python-Slurm-Cluster-Five-Minutes


   ## Nombre de la tarea
   #SBATCH --job-name=randhom

   ## Cola de trabajos a la cual enviar.
   #SBATCH --partition=small

   ## tasks requested
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=20

   ## STDOUT
   #SBATCH -o submit_python_jobs.out

   ## STDOUT
   #SBATCH -e submit_python_jobs.err

   ## Tiempo de ejecucion. Formato dias-horas:minutos.
   #SBATCH --time 0-1:00

   ## Script que se ejecuta al arrancar el trabajo

   ## Cargar el entorno del usuario incluyendo la funcionalidad de modules
   ## No tocar
   . /etc/profile

   # conda init bash
   # source /home/${USER}/.bashrc

   module load gcc/8.2.0
   conda activate
   # por las dudas activar conda antes de correr el sbatch

   ## Launch program

   srun python randhom/sd.py ../set/config.ini

   ## launch script
   ## $>sbatch submit_python_jobs.sh







