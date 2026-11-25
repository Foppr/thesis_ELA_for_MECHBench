import numpy as np

class AsymmetricSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Exponential decay attraction toward boundaries
        boundary_attraction = 0.0
        for i in range(self.dim):
            boundary_attraction += np.exp(-0.5 * (x[i] - 5.0)**2) + np.exp(-0.5 * (x[i] + 5.0)**2)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Asymmetric saddle points with polynomial distortions
        saddle_term = 0.0
        for i in range(self.dim):
            # Create asymmetric behavior based on dimension index
            asymmetry = 1.0 + 0.2 * np.sin(i * np.pi / self.dim)
            saddle_term += asymmetry * (x[i]**3 - 3*x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimension coupling with weighted interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + 1) / (j + 1)
                coupling += weight * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Quadratic baseline with dimensionality scaling
        quadratic = np.sum(x**2)
        
        # Combine all terms with adaptive weights based on dimensionality
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return dim_factor * (0.5 * quadratic + 0.3 * boundary_attraction + 
                            0.2 * trig_term + 0.25 * saddle_term + 0.15 * coupling)