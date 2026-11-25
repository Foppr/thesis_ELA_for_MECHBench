import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base spherical function with global minimum at origin
        result = np.sum(x**2) / (2 * self.dim)
        
        # Add exponentially decaying trigonometric waves with varying frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.8)
            result += 2.0 * np.exp(-0.1 * np.abs(x[i])) * np.sin(freq * x[i])**2
        
        # Add wave interference terms with phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = 0.5 * np.sin(i * 0.3 + j * 0.4)
                result += 0.8 * np.cos(x[i] * x[j] + phase) * \
                         np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add a radial component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            result += 1.5 * np.sin(3 * r) * np.exp(-0.2 * r)
        
        # Add asymmetric terms to break symmetry
        for i in range(self.dim):
            result += 0.3 * x[i]**3 * np.cos(x[i]) + \
                     0.2 * np.abs(x[i])**1.5 * np.sin(2 * x[i])
        
        # Add coupling between dimensions with different interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.4 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * \
                         np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Add a noise component to prevent convergence to trivial solutions
        result += 0.05 * np.random.random()
        
        return result