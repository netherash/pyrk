
"""
This module creates a table to store information about components in the
simulation.
"""

from __future__ import print_function

import numpy as np
import tables as tb


def make_components_table(db, components):
    """Adds a components table to hold information about each component in the
    database

    Parameters
    ----------
    db: Database
        The prke backend database object

    components: list(Component)
    """

    # Define data types involved in a component
    component_dtype = np.dtype([
        ('id', int),
        ('vol', float),
        ('name', 'S10')
    ])

    # Convert to numpy array
    component_array = np.array(components, dtype=component_dtype)

    # Open the hdf5 file
    db_file = tb.openFile(db, 'a')

    # Create a group for the table (TODO: add something that fixes the
    input_group = db_file.createGroup("/", "input", "Input")

    # Make the new table
    component_table = db_file.createTable(input_group, 'Components',
                                          component_array, 'Component ID, \
                                          Component Volume [m^3], \
                                          Component Name')

    # Ensure that data was written to table
    component_table.flush()

    # Close the hdf5 file
    db_file.close()