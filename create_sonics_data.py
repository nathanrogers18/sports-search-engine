import psycopg2
import csv


def main():
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS sonics_1996_per_game;")
    cur.execute("""
        CREATE TABLE sonics_1996_per_game (id serial PRIMARY KEY,
                                           player varchar,
                                           age integer,
                                           games integer,
                                           games_started integer,
                                           minutes_played decimal,
                                           field_goals decimal,
                                           field_goal_attempts decimal,
                                           field_goal_percentage decimal,
                                           three_pointers_made decimal,
                                           three_pointers_attempted decimal,
                                           three_point_percentage decimal,
                                           two_pointers_made decimal,
                                           two_pointers_attempted decimal,
                                           two_point_percentage decimal,
                                           e_field_goal_percentage decimal,
                                           free_throws decimal,
                                           free_throws_attempted decimal,
                                           free_throw_percentage decimal,
                                           offensive_rebounds decimal,
                                           defensive_rebounds decimal,
                                           total_rebounds decimal,
                                           assists decimal,
                                           steals decimal,
                                           blocks decimal,
                                           turnovers decimal,
                                           personal_fouls decimal,
                                           points decimal);""")
    with open("teams_SEA_1996_per_game.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO sonics_1996_per_game (player,
                                                    age,
                                                    games,
                                                    games_started,
                                                    minutes_played,
                                                    field_goals,
                                                    field_goal_attempts,
                                                    field_goal_percentage,
                                                    three_pointers_made,
                                                    three_pointers_attempted,
                                                    three_point_percentage,
                                                    two_pointers_made,
                                                    two_pointers_attempted,
                                                    two_point_percentage,
                                                    e_field_goal_percentage,
                                                    free_throws,
                                                    free_throws_attempted,
                                                    free_throw_percentage,
                                                    offensive_rebounds,
                                                    defensive_rebounds,
                                                    total_rebounds,
                                                    assists,
                                                    steals,
                                                    blocks,
                                                    turnovers,
                                                    personal_fouls,
                                                    points)
                VALUES (%s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s)""",
                        (row))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
