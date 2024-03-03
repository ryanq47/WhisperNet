import sqlite3
import logging
import inspect
import Utils.ErrorDefinitions
from Utils.Logger import LoggingSingleton

class AuthenticationSQLDBHandler():
    '''
    This DB handler is for Authentication

    DB is connected to on initialization of this class.
    
    '''

    #[X]
    def __init__(self, db_path):
        self.logger = LoggingSingleton.get_logger()
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_path)
        self.logger.debug(f"[*] Successful DB connection to {db_path}")

    #[X]
    def connect_to_db(self, db_path):
        '''
        Initiates the connection to the database

        sets self.dbconn to the connection
        sets self.curson to the cursor of self.dbconn
        
        '''
        #

        try:
            self.dbconn = sqlite3.connect(db_path)
            self.cursor = self.dbconn.cursor()
            self.logger.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_path}")

        except Exception as e:
            self.logger.error(f"Error connecting to the database: {e}")
            raise

    def nuke_and_recreate_db(self):
        '''
        Wipe, and recreate the DB. 
        '''

        self._wipe_db()
        self._create_tables()
        self._add_roles()
        #self._add_initial_admin_user()

    #[X]
    def get_api_username(self, username=None) -> bool:
        '''
        Get a username - basically a "check if user exists" function
        
        returns a bool, true if exists, false if not
        '''

        #
        try:
            if username == None:
                self.logger.info("Username argument is None!")
                return False

            # check if user exists
            self.cursor.execute(f"SELECT 1 FROM api_users WHERE username = ?", (username,))
            result = self.cursor.fetchone()

            if result:
                return True
            else:
                return False

        except Exception as e:
            self.logger.error(f"Error retrieving username: {e}")
            raise

    #[X]
    def get_api_password_blob(self, username=None) -> bytes:
        '''
        Get a password blob for API users. Exact copy of get_password_blob save for the table being accessed
        
        Note, may need to add a check for if more than one result is returned -- hey dipshit, fixed with primary keys
        '''
        #

        try:
            # guard clause to check if username is none.
            if username == None:
                self.logger.info("Username argument is None!")
                return False

            self.cursor.execute(f"SELECT password_hash FROM api_users WHERE username = ?", (username,))
            password_hash = self.cursor.fetchone()

            if password_hash:
                return password_hash
            else:
                return False

        except Exception as e:
            self.logger.error(f"Error retrieving password blob: {e}")
            raise

    def change_api_user_password(self, username=None, password_hash=None) -> bool:
        '''
        
        '''
        #

        if not all([username, password_hash]):
            self.logger.debug("Invalid input parameters for changing password")
            return False

        try:
            ## Update user in table
            self.cursor.execute("UPDATE api_users SET password_hash = ? WHERE username = ?", (password_hash, username,))
            self.dbconn.commit()

            ## Checking for affected rows basically
            if self.cursor.rowcount == 0:
                self.logger.error(f"No rows were updated")
                return False

            return True
        except Exception as e:
            self.logger.error(f"Error changing user password: {e}")
            raise

    #[X]
    def create_api_user(self, username=None, password_blob=None) -> bool:
        '''
        The DB implementation of create_user. This directly accesses, and modifies the DB. Apart of the 
        AuthenticationSQLDBHandler class
        '''
        #

        try:
            insert_query = 'INSERT OR IGNORE INTO api_users (username, password_hash) VALUES (?, ?)'
            values = (username, password_blob)
            self.cursor.execute(insert_query, values)
            self.dbconn.commit()
            return True
        except sqlite3.IntegrityError:
            self.logger.warning(f"[*] User {username} already exists!")

        except Exception as e:
            self.logger.error(f"Error creating API user: {e}")
            raise

        return False
    
    #[x]
    def delete_api_user(self, username):
        '''
        Deletes a user and their associated roles from the database.

        :param username: The username of the user to be deleted
        :return: True if the deletion is successful, False otherwise
        '''
        try:
            # Begin a transaction
            #self.dbconn.begin()

            # Step 1: Delete entries from user_roles
            # Fetch user_id from the username
            user_query = 'SELECT user_id FROM api_users WHERE username = ?'
            self.cursor.execute(user_query, (username,))
            user_id = self.cursor.fetchone()

            if user_id is None:
                self.logger.error(f"User {username} not found for deletion")
                return False

            delete_roles_query = 'DELETE FROM user_roles WHERE user_id = ?'
            self.cursor.execute(delete_roles_query, (user_id[0],))

            # Step 2: Delete the user
            delete_user_query = 'DELETE FROM api_users WHERE username = ?'
            self.cursor.execute(delete_user_query, (username,))

            # Commit the transaction
            self.dbconn.commit()
            return True

        except Exception as e:
            # Rollback in case of error
            self.dbconn.rollback()
            self.logger.error(f"Error deleting user {username}: {e}")
            raise

    # [x]
    def add_api_role(self, username=None, roles=None):
        '''
        Adds roles to an API user, skipping any roles that cannot be added.

        roles (list): Roles to be added
            Ex: ["filehost_admin", "iam_admin"]
        '''
        #

        if not username:
            self.logger.error("Username not provided")
            return False
        
        if not roles:
            self.logger.error("Roles not provided")
            return False

        try:
            # Fetch user_id from the username
            user_query = 'SELECT user_id FROM api_users WHERE username = ?'
            self.cursor.execute(user_query, (username,))
            user_id = self.cursor.fetchone()

            if user_id is None:
                raise ValueError("User not found")

            # Initialize a counter for successful role additions
            successful_additions = 0

            # Add each role to the user
            for role_name in roles:
                try:
                    # Fetch role_id from the role_name
                    role_query = 'SELECT role_id FROM roles WHERE role_name = ?'
                    self.cursor.execute(role_query, (role_name,))
                    role_id = self.cursor.fetchone()

                    if role_id is None:
                        raise ValueError(f"Role '{role_name}' not found")

                    # Insert user_id and role_id into user_roles
                    insert_query = 'INSERT INTO user_roles (user_id, role_id) VALUES (?, ?)'
                    self.cursor.execute(insert_query, (user_id[0], role_id[0]))
                    successful_additions += 1

                except Exception as role_error:
                    self.logger.error(f"Error adding role '{role_name}': {role_error}")
                    continue  # Skip to the next role

            self.dbconn.commit()

            # Check if any roles were added successfully
            if successful_additions > 0:
                return True
            else:
                return False

        except Exception as e:
            self.dbconn.rollback()
            self.logger.error(f"Error adding roles: {e}")
            raise

    def delete_api_role(self, username=None, roles=None):
        '''
        Removes specified roles from an API user, skipping any roles that cannot be removed.

        roles (list): Roles to be removed
            Ex: ["filehost_admin", "iam_admin"]
        '''
       # 

        if not username:
            self.logger.error("Username not provided")
            return False
        
        if not roles:
            self.logger.error("Roles not provided")
            return False

        try:
            # Fetch user_id from the username
            user_query = 'SELECT user_id FROM api_users WHERE username = ?'
            self.cursor.execute(user_query, (username,))
            user_id = self.cursor.fetchone()

            if user_id is None:
                raise ValueError("User not found")

            # Initialize a counter for successful role removals
            successful_removals = 0

            # Remove each specified role from the user
            for role_name in roles:
                try:
                    # Fetch role_id from the role_name
                    role_query = 'SELECT role_id FROM roles WHERE role_name = ?'
                    self.cursor.execute(role_query, (role_name,))
                    role_id = self.cursor.fetchone()

                    if role_id is None:
                        raise ValueError(f"Role '{role_name}' not found")

                    # Delete user_id and role_id from user_roles
                    delete_query = 'DELETE FROM user_roles WHERE user_id = ? AND role_id = ?'
                    self.cursor.execute(delete_query, (user_id[0], role_id[0]))
                    if self.cursor.rowcount > 0:
                        successful_removals += 1

                except Exception as role_error:
                    self.logger.error(f"Error removing role '{role_name}': {role_error}")
                    continue  # Skip to the next role

            self.dbconn.commit()

            # Check if any roles were successfully removed
            if successful_removals > 0:
                return True
            else:
                return False

        except Exception as e:
            self.dbconn.rollback()
            self.logger.error(f"Error deleting roles: {e}")
            raise

    #[x]
    def get_all_api_user_roles(self, username):
        """
        Fetches all roles for a specific user.

        :param username: The username of the user
        :return: List of roles for the user
        """
        user_id = self.get_api_user_id(username)
        if user_id is None:
            return "User not found"

        query = """
            SELECT u.username, r.role_name FROM user_roles ur
            JOIN api_users u ON ur.user_id = u.user_id
            JOIN roles r ON ur.role_id = r.role_id
            WHERE u.user_id = ?
        """
        try:
            self.cursor.execute(query, (user_id,))
            roles = self.cursor.fetchall()
            return roles
        except Exception as e:
            self.logger.error(f"Error fetching roles for user {username}: {e}")
            return "Error fetching roles"

    #[X]
    def get_api_users_with_role(self, role_name):
        """
        Fetches all users who have a specific role.

        :param role_name: The name of the role
        :return: List of users with the role
        """
        # First, get the role_id from role_name
        role_query = 'SELECT role_id FROM roles WHERE role_name = ?'
        try:
            self.cursor.execute(role_query, (role_name,))
            role_result = self.cursor.fetchone()
            if role_result is None:
                return "Role not found"
            role_id = role_result[0]
        except Exception as e:
            self.logger.error(f"Error fetching role ID for role {role_name}: {e}")
            return "Error fetching role ID"

        # Then, get the users with the role_id
        user_query = """
            SELECT u.username, r.role_name FROM user_roles ur
            JOIN api_users u ON ur.user_id = u.user_id
            JOIN roles r ON ur.role_id = r.role_id
            WHERE r.role_id = ?
        """
        try:
            self.cursor.execute(user_query, (role_id,))
            users = self.cursor.fetchall()
            return users
        except Exception as e:
            self.logger.error(f"Error fetching users with role {role_name}: {e}")
            return "Error fetching users"

    def get_api_user_id(self, username):
        """
        Fetches the user ID for a given username.

        :param username: The username of the user
        :return: User ID or None if not found
        """
        query = 'SELECT user_id FROM api_users WHERE username = ?'
        try:
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            self.logger.error(f"Error fetching user ID for username {username}: {e}")
            return None

    #[x] -- May run into type issues, changed user_id in api_users 
    # into integer for auto increment
    def _create_tables(self):
        """
        Creates tables if needed

        user: blob
        pass: blob
        id: BLOB (not sure if needed)
        """
        

        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS api_users (
                    user_id INTEGER PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password_hash BLOB
                );
            """)

            ## Roles table
            self.cursor.execute("""
                CREATE TABLE roles (
                    role_id INT PRIMARY KEY,
                    role_name VARCHAR(255) UNIQUE NOT NULL
                );                   
            """)

            # combined user roles
            self.cursor.execute("""
                CREATE TABLE user_roles (
                    user_id INT,
                    role_id INT,
                    PRIMARY KEY (user_id, role_id),
                    FOREIGN KEY (user_id) REFERENCES api_users(user_id), 
                    FOREIGN KEY (role_id) REFERENCES roles(role_id)
                );           
            """)

            self.dbconn.commit()
        except Exception as e:
            self.dbconn.rollback()
            self.logger.error(f"Error creating tables: {e}")
            raise

    # [x]
    def _wipe_db(self):
        
        '''
        Clears out the database with a predefined list of tables:
        ['api_users','users','user_roles']

        Technically injectable, but no input is taken so its "safe". 
        '''
        

        tables = ['api_users','roles','user_roles']

        try:
            for table in tables:
                self.cursor.execute(f"DROP TABLE IF EXISTS {table}")
            self.dbconn.commit()
        except Exception as e:
            self.dbconn.rollback()
            self.logger.error(f"Error wiping database: {e}")
            raise
        
    # [x]
    def _add_roles(self):
        '''
        Adds initial roles to DB. Should only be called on table wipe/recreation.

        Roles have to be manually added to this function for now. Will figure out the plugin 
        & custom role situation later.
        
        '''
        roles_to_insert = [
            (1, 'iam_admin'),
            (2, 'iam_user'),
            # ... more roles
        ]

        insert_query = 'INSERT INTO roles (role_id, role_name) VALUES (?, ?)'

        try:
            self.cursor.executemany(insert_query, roles_to_insert)
            self.dbconn.commit()
        except Exception as e:
            self.dbconn.rollback()
            self.logger.error(f"Error adding roles: {e}")
            raise


