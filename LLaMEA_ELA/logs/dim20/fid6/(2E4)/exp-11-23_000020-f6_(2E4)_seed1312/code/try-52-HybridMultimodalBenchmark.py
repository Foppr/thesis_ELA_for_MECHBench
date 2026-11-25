import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for wave components
        self.freqs = np.linspace(1.0, 8.0, dim)
        # Precompute RBF centers and variances
        self.centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.variances = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian radial basis function component
        rbf = 0.0
        for i in range(10):
            diff = x_norm - self.centers[i]
            rbf += np.exp(-np.sum(diff**2) / (2 * self.variances[i]**2))
        
        # Sine-cosine wave interference with varying frequencies
        wave = 0.0
        for i in range(self.dim):
            wave += np.sin(self.freqs[i] * x_norm[i]) * np.cos(self.freqs[i] * x_norm[i])
        
        # Polynomial conditioning with mixed powers
        poly = np.sum(0.5 * x_norm**4 + 0.3 * x_norm**3 + 0.2 * x_norm**2 + 0.1 * x_norm)
        
        # Coupling between dimensions using exponential decay and trigonometric interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(3 * (x_norm[i] + x_norm[j]))
        
        # Add a global sine modulation to increase landscape complexity
        global_mod = np.sin(0.5 * np.sum(x_norm**2))
        
        # Combine all components with optimized weights
        return 0.3 * rbf + 0.4 * wave + 0.15 * poly + 0.1 * coupling + 0.05 * global_mod + 2.1