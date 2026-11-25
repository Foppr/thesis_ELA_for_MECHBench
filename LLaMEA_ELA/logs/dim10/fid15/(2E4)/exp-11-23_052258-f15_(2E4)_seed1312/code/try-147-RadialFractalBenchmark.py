import numpy as np

class RadialFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute cluster centers with modified fractal-like distribution
        self.centers = []
        for i in range(dim):
            center = 5.0 * np.sin(i * np.pi / (dim + 2))
            self.centers.append(center)
        self.centers = np.array(self.centers)
        
        # Modified adaptive scaling factors based on dimension
        self.scales = [1.0 + 0.3 * np.cos(i * 0.6) for i in range(dim)]
        self.decay_rates = [0.6 + 0.2 * np.sin(i * 0.9) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Modified radial basis function component with adaptive centers
        rbfs = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            scale = self.scales[i]
            decay = self.decay_rates[i]
            diff = x[i] - center
            rbfs += scale * np.exp(-decay * diff**2)
            
        # Altered multi-scale fractal interaction terms
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified fractal-like interaction with different decay
                dist = abs(x[i] - x[j])
                fractal_term += np.exp(-dist**1.5) * np.sin(dist * np.pi * 0.5)
                
        # Adjusted exponential decay coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += np.exp(-abs(x[i]) / (1.5 + self.decay_rates[i]))
            
        # Modified self-similarity pattern with different scales
        similarity_term = 0.0
        scales = [1.5, 2.5, 3.5, 4.5]
        for scale in scales:
            for i in range(self.dim):
                similarity_term += np.sin(x[i] / scale) * np.cos(x[i] / (scale * 0.8))
                
        # Modified asymmetric penalty with fractal structure
        penalty_term = 0.0
        for i in range(self.dim):
            val = x[i]
            penalty_term += (val**3 + 0.4 * np.sin(2 * val)) * np.exp(-abs(val) / 1.5)
            
        # Combine all terms with adjusted weights
        weights = [0.25, 0.30, 0.25, 0.15, 0.05]
        total = (weights[0] * rbfs + 
                weights[1] * fractal_term + 
                weights[2] * coupling_term + 
                weights[3] * similarity_term + 
                weights[4] * penalty_term)
                
        # Modified dimensionality-based scaling with enhanced fractal adjustment
        scale = 1.0 + 0.30 * np.log(self.dim + 1) + 0.15 * np.sum(np.abs(x)**1.8)
        
        return scale * total