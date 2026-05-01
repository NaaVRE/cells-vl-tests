setwd('/app')
library(optparse)
library(jsonlite)


load_json_args <- function(file_path) {
  fromJSON(file_path, simplifyVector = FALSE)
}

parse_value <- function(value, field_name, target_type, elem_type = NULL) {
  if (identical(target_type, "list")) {
    if (is.list(value)) {
      return(value)
    } else if (is.character(value) && length(value) == 1) {
      return(fromJSON(value, simplifyVector = FALSE))
    }
  }

  if (identical(target_type, "str")) {
    return(as.character(value))
  }

  if (identical(target_type, "int")) {
    return(as.integer(value))
  }

  if (identical(target_type, "float")) {
    if (is.numeric(value) || (is.character(value) && length(value) == 1)) {
      return(as.numeric(value))
    }
  }

  stop(paste0(field_name, " has unsupported target type"), call. = FALSE)
}

get_arg_value <- function(name, raw_args) {
  for (arg in raw_args) {
    if (!is.null(arg$name) && identical(arg$name, name)) {
      return(arg$value)
    }
  }
  stop(paste0("Argument '", name, "' not found in JSON args"), call. = FALSE)
}


option_list = list(
make_option(c("--args_json"), action="store", default=NA, type="character", help="args json path")
)

opt = parse_args(OptionParser(option_list=option_list))
raw_args = load_json_args(opt$args_json)




L <- c("a", "b", "c")

conf_data_folder <- "/tmp/data"
file_path <- file.path(conf_data_folder, "hello.txt")

writeLines(L, file_path)

onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)
# capturing outputs
file <- file(paste0('/tmp/file_path_', id, '.json'))
writeLines(toJSON(file_path, auto_unbox=TRUE), file)
close(file)
