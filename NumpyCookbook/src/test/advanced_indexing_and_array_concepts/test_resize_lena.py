'''
Created on 6 Jul 2014

@author: wrightm
'''
import unittest
import scipy.misc
import numpy.testing
import matplotlib.pyplot


class ResizeLenaTest(unittest.TestCase):


    def test(self):
        
        # Loads the Lena image into an array
        lena = scipy.misc.lena()

        #Lena's dimensions
        LENA_X = 512
        LENA_Y = 512

        #Check the shape of the Lena array
        numpy.testing.assert_equal((LENA_X, LENA_Y), lena.shape)

        # Get the resize factors
        yfactor = 10.0
        xfactor = 10.0

        # Resize the Lena array
        resized = lena.repeat(yfactor, axis=0).repeat(xfactor, axis=1)

        #Check the shape of the resized array
        numpy.testing.assert_equal((yfactor * LENA_Y, xfactor * LENA_Y), resized.shape)

        # Plot the Lena array
        matplotlib.pyplot.subplot(211)
        matplotlib.pyplot.imshow(lena)

        #Plot the resized array
        matplotlib.pyplot.subplot(212)
        matplotlib.pyplot.imshow(resized)
        matplotlib.pyplot.show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()