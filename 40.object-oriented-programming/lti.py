import numpy as np


class LTI_DT(object):
    
    def __init__(self, A, B, C, D, x0=None,):

        # Set state space representation
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        # is A matrix square?
        assert A.shape[0] == A.shape[1]
        
        # number of state variables
        self.n = A.shape[0]

        # check number of rows of B matrix
        assert B.shape[0] == self.n
        
        # expected size of input
        self.m = B.shape[1]

        # Initialize state column vector
        # https://stackoverflow.com/questions/12575421/convert-a-1d-array-to-a-2d-array-in-numpy
        self.x = np.array(x0).reshape((self.n, 1))

    def get_y(self, u_array=None):
        """
        y[k] = C x[k] + D u[k]
        """
        result = self.C @ self.x
        try:
            if u_array is not None:
                result += self.D @ u_array.reshape((self.m, 1))
        except ValueError as e:
            print(f'self.D = \n{self.D}')
            print(f'self.D.shape = \n{self.D.shape}')
            print(f'u_array = \n{u_array}')
            print(f'u_array.shape = \n{u_array.shape}')
            print(f'self.D @ u_array = \n{self.D @ u_array}')
            print(f'(self.D @ u_array).shape = \n{(self.D @ u_array).shape}')
            print(f'result = \n{result}')
            print(f'result.shape = \n{result.shape}')
            raise e
            
        return result

    def get_next_x(self, u_array=None):
        """
        x[k+1] = A x[k] + B u[k]
        """
        next_x = self.A @ self.x
        
        if u_array is not None:
            next_x += self.B @ u_array.reshape((self.m, 1))
        
        self.x = next_x


class LTI_CT(LTI_DT):
    def __init__(self, A, B, C, D, delta_t, x0=None, t0=0):
        super().__init__(A, B, C, D, x0)
        self.delta_t = delta_t
        self.t = t0

    def get_dx_dt(self, u_t=None):
        """
        dx_dt(t[i]) = A x(t[i]) + B u(t[i])
        """

        dx_dt_now = self.A @ self.x

        if u_t is not None:
            dx_dt_now += self.B @ u_t.reshape((self.m, 1))

        return dx_dt_now

    def get_next_x(self, u_t=None):
        """
        Euler method
        x(t[i+1]) = x(t[i]) + delta_t * dx_dt(t[i])
        """

        next_x = self.x + self.delta_t * self.get_dx_dt(u_t)

        self.x = next_x
        self.t += self.delta_t

