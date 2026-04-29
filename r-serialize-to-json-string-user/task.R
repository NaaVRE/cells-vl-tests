setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("jsonlite", quietly = TRUE)) {
	install.packages("jsonlite", repos="http://cran.us.r-project.org")
}
library(jsonlite)



print('option_list')
option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="task id")
)


opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(var){
    if (is.null(var)){
        print("Variable is null")
        exit(1)
    }
    tryCatch(
        {
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        error=function(e) {
            print("Error while deserializing the variable")
            print(var)
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        warning=function(w) {
            print("Warning while deserializing the variable")
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        }
    )
}

id <- gsub('"', '', opt$id)


print("Running the cell")
data <- list(
  task = "Write Python",
  number = 1,
  skills = c("python", "sql")
)

json_str <- toJSON(data, pretty = TRUE, auto_unbox = TRUE)

print(json_str)
# capturing outputs
print('Serialization of data')
file <- file(paste0('/tmp/data_', id, '.json'))
writeLines(toJSON(data, auto_unbox=TRUE), file)
close(file)
print('Serialization of json_str')
file <- file(paste0('/tmp/json_str_', id, '.json'))
writeLines(toJSON(json_str, auto_unbox=TRUE), file)
close(file)
