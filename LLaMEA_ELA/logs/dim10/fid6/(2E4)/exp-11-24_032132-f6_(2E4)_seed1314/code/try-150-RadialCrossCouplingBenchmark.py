import numpy as np

class RadialCrossCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_rbf_centers = 12
        self.noise_injection_rate = 0.15
        self.coupling_strength = 1.5
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Generate random RBF centers
        np.random.seed(42)  # For reproducibility
        centers = np.random.uniform(-5.0, 5.0, (self.num_rbf_centers, self.dim))
        
        # Radial basis function component with varying widths
        for i in range(self.num_rbf_centers):
            center = centers[i]
            # Adaptive width based on dimension
            width = 1.0 + 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(i * 0.9)
            diff = x - center
            distance_sq = np.sum(diff ** 2)
            result += np.exp(-distance_sq / (2 * width ** 2))
        
        # Cross-dimensional coupling term
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling coefficient
                coeff = 0.5 + 0.3 * np.sin(i * 0.8 + j * 0.6) + 0.2 * np.cos(i * 0.4 + j * 0.9)
                coupling_term += coeff * (x[i] - x[j]) ** 2
        
        # Adaptive noise injection
        noise = 0.0
        if np.random.rand() < self.noise_injection_rate:
            noise = np.random.normal(0, 1.0) * (1.0 + 0.5 * np.sin(np.sum(x)))
        
        # Combine components with varying weights
        return 0.6 * result + 0.3 * coupling_term + 0.1 * noise