import create_sonics_data
import argparse
import psycopg2
import sys


class SonicsSearcher(object):
    def __init__(self):
        # Connect to an existing database
        self.conn = psycopg2.connect("dbname=test user=postgres")
        # Open a cursor to perform database operations
        self.cur = self.conn.cursor()
        # Create top level arg parser
        parser = argparse.ArgumentParser(
                    description='96 Sonics were the best',
                    usage="""
<function> [<arguments>]
   search     Search the database
   insert     Insert a player
   top        Get the leaders in a statistical category
   edit       Edit a player
""")

        parser.add_argument('function',
                            help="The function you'd like to run")
        parser.add_argument('-i', '--insert', metavar="Insert", help='Insert a player')
        parser.add_argument('-t', '--top', metavar="Top", help='Get the top 5 performers for a given statistical category')
        parser.add_argument('-e', '--edit', metavar="Edit", help='Edit a player')
        args = parser.parse_args()
        print(args)
        if not hasattr(self, args.function):
            print('Unrecognized command')
            print('fudge')
            parser.print_help()
            exit(1)
        print('yes')
        getattr(self, args.function)()

        self.conn.close()

    def search(self):
        print('searching!')
        parser = argparse.ArgumentParser(
            description='Search for a player by name OR age`')
        parser.add_argument('--name',
                            help="Player Name", type=str, required=False)
        parser.add_argument('--age',
                            help="Player Age", type=int, required=False)
        # print 'Running git commit, amend=%s' % args.amend
        print('here')
        args = parser.parse_args(sys.argv[1:])
        print('here', args)
        print(type(args))
        if hasattr(self, args.age):
            self.cur.execute("SELECT * FROM stats WHERE age = %s;", args[2])
            stats = self.cur.fetchone()
        elif hasattr(self, args.name):
            self.cur.execute("SELECT * FROM stats WHERE player = %s;", args[1])
        else:
            print('Unrecognized command')
            print('fudge')
            parser.print_help()
            exit(1)
        stats = self.cur.fetchone()

        print('search')

    def insert(self):
        parser = argparse.ArgumentParser(
            description='Please enter your search criteria',
        )
        print('insert')

    def top(self):
        parser = argparse.ArgumentParser(
            description='Please enter your search criteria',
        )
        print('top')

    def edit(self):
        parser = argparse.ArgumentParser(
            description='Please enter your search criteria',
        )
        print('edit')

def main():
    SonicsSearcher()
    # if database does not exist, create it
    # create_sonics_data.main()
    # parser = argparse.ArgumentParser(description='Greatest Team Ever')
    # parser.add_argument('-pl', '--player', metavar='Player Name', type=str,
    #                 help="The player's full name", required=True)
    #
    # parser.add_argument('-r', '--rank', metavar='Rank', type=int,
    #                     help='The player, required=True)
    # parser.add_argument('--birthday', metavar='Birthday', type=str,
    #                     help='YYYY-MM-DD')
    # parser.add_argument('--height', metavar='Height', type=int,
    #                     help='Height in inches')
    # parser.add_argument('--is_deleted', metavar='Is Deleted', type=bool,
    #                     default=False,
    #                     help='True if the student has dropped the class')
    # args = parser.parse_args()
    # print(args.name)

if __name__ == "__main__":
    main()

# player varchar,
# age integer,
# games integer,
# games_started integer,
# minutes_played decimal,
# field_goals decimal,
# field_goal_attempts decimal,
# field_goal_percentage decimal,
# three_pointers_made decimal,
# three_pointers_attempted decimal,
# three_point_percentage decimal,
# two_pointers_made decimal,
# two_pointers_attempted decimal,
# two_point_percentage decimal,
# e_field_goal_percentage decimal,
# free_throws decimal,
# free_throws_attempted decimal,
# free_throw_percentage decimal,
# offensive_rebounds decimal,
# defensive_rebounds decimal,
# total_rebounds decimal,
# assists decimal,
# steals decimal,
# blocks decimal,
# turnovers decimal,
# personal_fouls decimal,
# points decimal
