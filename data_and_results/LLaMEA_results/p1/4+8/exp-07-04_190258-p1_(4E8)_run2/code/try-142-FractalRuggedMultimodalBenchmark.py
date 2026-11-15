import numpy as np

class FractalRuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for scalability
        self.fractal_params = np.random.uniform(0.5, 2.0, dim)
        self.hill_params = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Clip input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        base = np.sum(x**2) * 0.1
        
        # Fractal-like ruggedness using sine waves with varying frequencies
        fractal_rugged = 0
        for i in range(self.dim):
            freq = 10 * (i + 1) / self.dim
            fractal_rugged += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * \
                              np.exp(-0.05 * x[i]**2)
        
        # Hierarchical valleys with varying depths
        valleys = 0
        for i in range(self.dim):
            # Create nested valley structure
            valley_depth = 0.5 * np.sin(2 * np.pi * x[i]) + 0.3 * np.sin(4 * np.pi * x[i])
            valleys += valley_depth * np.exp(-0.1 * np.abs(x[i]))
        
        # Controlled chaos with logistic map inspired terms
        chaos = 0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            # Logistic map component
            logistic_val = np.sin(x[i]) * np.cos(x[i])
            chaos += np.sin(r * logistic_val) * np.exp(-0.02 * x[i]**2)
        
        # Multi-scale sinusoidal interference
        interference = 0
        for i in range(self.dim):
            interference += np.sin(15 * x[i]) * np.cos(12 * x[i]) * \
                          np.sin(8 * x[i]) * np.exp(-0.01 * x[i]**2)
        
        # Asymmetric hill structure with exponential modulation
        hills = 0
        for i in range(self.dim):
            hill_height = self.hill_params[i] * np.exp(-0.5 * (x[i] - 1)**2) + \
                         0.5 * np.exp(-0.5 * (x[i] + 1)**2)
            hills += hill_height * np.sin(3 * x[i])
        
        # Global minimum perturbation
        global_min = 0.01 * np.sum((x - 0.5)**4)
        
        # Combine all components
        return base + fractal_rugged + valleys + chaos + interference + hills + global_min