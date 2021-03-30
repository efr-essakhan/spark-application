from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def loadMovieNames():
    movieNames = {}
    with open("ml-100k/u.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

def parseInput(line):
    fields = line.split()
    return Row(movieID = int(fields[1]), rating = float(fields[2]))

if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

    # Load up movie ID -> name dictionary
    movieNames = loadMovieNames()

    # Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.data")
    # Convert it to a RDD of Row objects with (movieID, rating)
    movies = lines.map(parseInput)
    # Convert that to a DataFrame
    movieDataset = spark.createDataFrame(movies)

    #Show the db of all movies ordered according to popularity:
    movieDataset.show()
    # If you want to show the results at this point of all movies ordered according to popularity:
    # #topMovieIDs.show()


    # Print the results
    #print("Movie name | Total number of ratings")
    # count = 0
    # for result in movieDataset:
    #     text = "%s | %d" % (movieNames[result[0]], result[1])
    #     count = count + 1
    #     print("{}. {}".format(count, text))

    # Stop the session
    spark.stop()
