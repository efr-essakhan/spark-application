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
    # Create a SparkSession (the config bit is only for Windows!)
    spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

    # Load up our movie ID -> name dictionary
    movieNames = loadMovieNames()

    # Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.data")
    # Convert it to a RDD of Row objects with (movieID, rating)
    movies = lines.map(parseInput)
    # Convert that to a DataFrame
    movieDataset = spark.createDataFrame(movies)

    # SQL-style technique to sort all movies by popularity in one line!
    topMovieIDs = movieDataset.groupBy("movieID").count().orderBy("count", ascending=False).cache()

    # If you want to show the results at this point of all movies ordered according to popularity:

    #topMovieIDs.show()

    # Grab the top 10
    top10 = topMovieIDs.take(10)

    # Print the results
    #print("\n")
    print("Movie name | Total number of ratings")
    for result in top10:
        # Each row has movieID, count as above.
        print("%s: %d" % (movieNames[result[0]], result[1]))

    # Stop the session
    spark.stop()
