# Install required R packages for SIH extraction
repos <- "https://cloud.r-project.org"

pkgs_cran <- c("dplyr", "readr", "remotes")
for (p in pkgs_cran) {
  if (!requireNamespace(p, quietly = TRUE)) {
    cat("Installing", p, "...\n")
    install.packages(p, repos = repos, quiet = TRUE)
  } else {
    cat(p, "already installed\n")
  }
}

if (!requireNamespace("microdatasus", quietly = TRUE)) {
  cat("Installing microdatasus from GitHub...\n")
  remotes::install_github("rfsaldanha/microdatasus", quiet = TRUE)
} else {
  cat("microdatasus already installed\n")
}

cat("\nFinal check:\n")
for (p in c("microdatasus", "dplyr", "readr", "arrow", "read.dbc")) {
  ok <- requireNamespace(p, quietly = TRUE)
  cat(p, if (ok) ": OK" else ": MISSING", "\n")
}
