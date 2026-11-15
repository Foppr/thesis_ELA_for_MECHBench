import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and cubic terms with asymmetric scaling
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i] - 1.0)**2 + 0.3 * (x[i] + 1.0)**3 + 0.01 * x[i]**4
        
        # Chaotic interaction terms using sine waves with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_factor = 0.5 + 0.5 * np.sin(i * 0.7) * np.cos(j * 0.9)
                result += freq_factor * np.sin(5.0 * (x[i] - x[j])) * np.cos(3.0 * (x[i] + x[j]))
        
        # Asymmetric saddle points with fractal-like behavior
        for i in range(self.dim):
            result += 0.4 * np.sin(2.0 * x[i]) * np.cos(4.0 * x[i]) + 0.2 * np.sin(7.0 * x[i])
        
        # Add a complex global minimum with non-uniform curvature
        result += 0.001 * np.sum(np.abs(x)**3) + 0.0002 * np.sum(np.abs(x)**5)
        
        # Fractal-like periodic modulation to increase ruggedness
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(8.0 * x[i]) * np.cos(6.0 * x[i]) + 0.3 * np.sin(12.0 * x[i])
        result += 0.2 * fractal_term
        
        # Add asymmetric noise to create irregular basins
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(15.0 * x[i]) * np.cos(11.0 * x[i]) + 0.01 * np.sin(20.0 * x[i])
        result += noise
        
        # Shifted and scaled global minimum to encourage convergence
        result += 0.5 * np.sum((x - 0.5)**2) + 0.02 * np.sum((x - 0.5)**6)
        
        return result