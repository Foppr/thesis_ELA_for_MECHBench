import numpy as np

class RadialFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute cluster centers with fractal-like distribution
        self.centers = []
        for i in range(dim):
            center = 5.0 * np.sin(i * np.pi / (dim + 1))
            self.centers.append(center)
        self.centers = np.array(self.centers)
        
        # Adaptive scaling factors based on dimension
        self.scales = [1.0 + 0.2 * np.cos(i * 0.5) for i in range(dim)]
        self.decay_rates = [0.5 + 0.3 * np.sin(i * 0.8) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive centers
        rbfs = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            scale = self.scales[i]
            decay = self.decay_rates[i]
            diff = x[i] - center
            rbfs += scale * np.exp(-decay * diff**2)
            
        # Multi-scale fractal interaction terms
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction with exponential decay
                dist = abs(x[i] - x[j])
                fractal_term += np.exp(-dist**2) * np.sin(dist * np.pi)
                
        # Exponential decay coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += np.exp(-abs(x[i]) / (1.0 + self.decay_rates[i]))
            
        # Self-similarity pattern with multiple scales
        similarity_term = 0.0
        scales = [1.0, 2.0, 3.0, 4.0]
        for scale in scales:
            for i in range(self.dim):
                similarity_term += np.sin(x[i] / scale) * np.cos(x[i] / scale)
                
        # Asymmetric penalty with fractal structure
        penalty_term = 0.0
        for i in range(self.dim):
            val = x[i]
            penalty_term += (val**2 + 0.5 * np.sin(3 * val)) * np.exp(-abs(val) / 2.0)
            
        # Combine all terms with adjusted weights
        weights = [0.30, 0.25, 0.20, 0.15, 0.10]
        total = (weights[0] * rbfs + 
                weights[1] * fractal_term + 
                weights[2] * coupling_term + 
                weights[3] * similarity_term + 
                weights[4] * penalty_term)
                
        # Add dimensionality-based scaling with fractal adjustment
        scale = 1.0 + 0.25 * np.log(self.dim + 1) + 0.10 * np.sum(np.abs(x)**1.5)
        
        return scale * total