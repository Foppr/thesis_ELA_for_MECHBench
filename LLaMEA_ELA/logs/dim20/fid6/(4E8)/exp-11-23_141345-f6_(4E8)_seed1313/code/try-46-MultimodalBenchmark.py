import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with Hermite polynomials
        poly_chaos = np.sum((x**4 - 6*x**2 + 3) * np.exp(-0.1 * x**2))
        
        # Radial basis function with multiquadric kernel
        rbfn = 0.0
        for i in range(self.dim):
            rbfn += np.exp(-0.5 * np.sum((x - x[i])**2) / (0.5**2))
        
        # Coupled harmonic oscillators with varying frequencies and damping
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            damping = 0.1 + 0.2 * np.cos(i)
            harmonic += (np.sin(freq * x[i]) * np.exp(-damping * x[i]**2))
        
        # Cross-dimensional coupling with cubic interactions
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (x[i]**3 + x[i+1]**3) * np.sin(0.5 * (x[i] + x[i+1]))
        
        # Fractional Brownian motion inspired term with long-range dependence
        fbm = 0.0
        for i in range(self.dim):
            fbm += np.sin(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.02 * np.abs(x[i]))
        
        # Combined function with adjusted weights
        return 0.3 * poly_chaos + 0.25 * rbfn + 0.2 * harmonic + 0.15 * cross_coupling + 0.1 * fbm