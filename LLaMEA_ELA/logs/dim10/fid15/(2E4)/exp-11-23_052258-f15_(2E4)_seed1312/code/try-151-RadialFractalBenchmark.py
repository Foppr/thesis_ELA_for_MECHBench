import numpy as np

class RadialFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute cluster centers with chaotic fractal distribution
        self.centers = []
        for i in range(dim):
            center = 5.0 * np.sin(i * np.pi / (dim + 3)) * np.cos(i * 0.7)
            self.centers.append(center)
        self.centers = np.array(self.centers)
        
        # Enhanced adaptive scaling factors with chaotic components
        self.scales = [1.0 + 0.5 * np.cos(i * 0.8) * np.sin(i * 0.3) for i in range(dim)]
        self.decay_rates = [0.7 + 0.3 * np.sin(i * 1.1) * np.cos(i * 0.5) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with chaotic centers
        rbfs = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            scale = self.scales[i]
            decay = self.decay_rates[i]
            diff = x[i] - center
            rbfs += scale * np.exp(-decay * diff**2) * np.sin(x[i] * 0.5)
            
        # Chaotic multi-scale fractal interaction terms
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                fractal_term += np.exp(-dist**1.8) * np.sin(dist * np.pi * 0.3) * np.cos(dist * 0.7)
                
        # Enhanced exponential decay coupling with chaotic coefficients
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += np.exp(-abs(x[i]) / (2.0 + self.decay_rates[i] * np.sin(i * 0.4)))
            
        # Multi-scale self-similarity pattern with chaotic scaling
        similarity_term = 0.0
        scales = [1.2, 2.3, 3.7, 4.8, 5.1]
        for scale in scales:
            for i in range(self.dim):
                similarity_term += np.sin(x[i] / scale) * np.cos(x[i] / (scale * 0.6)) * np.sin(scale * 0.3)
                
        # Novel asymmetric penalty with chaotic structure
        penalty_term = 0.0
        for i in range(self.dim):
            val = x[i]
            penalty_term += (val**4 + 0.5 * np.sin(3 * val) + 0.2 * np.cos(2 * val)) * np.exp(-abs(val) / 2.0)
            
        # Combine all terms with enhanced weights
        weights = [0.30, 0.25, 0.20, 0.18, 0.07]
        total = (weights[0] * rbfs + 
                weights[1] * fractal_term + 
                weights[2] * coupling_term + 
                weights[3] * similarity_term + 
                weights[4] * penalty_term)
                
        # Enhanced dimensionality-based scaling with chaotic adjustment
        scale = 1.0 + 0.40 * np.log(self.dim + 1) + 0.20 * np.sum(np.abs(x)**2.2) * np.sin(self.dim * 0.5)
        
        return scale * total