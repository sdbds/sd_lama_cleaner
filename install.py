import launch

if not launch.is_installed("lama-cleaner"):
    launch.run_pip("install lama-cleaner", "requirements for sd_lama_cleaner")
