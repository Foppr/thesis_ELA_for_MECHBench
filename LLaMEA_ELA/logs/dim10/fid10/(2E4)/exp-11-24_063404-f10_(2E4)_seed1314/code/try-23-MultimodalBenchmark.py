import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal-like radial component with multiple scales and chaotic behavior
        r = np.sqrt(np.sum(x_scaled**2))
        fractal_radial = (np.sin(10 * r) * np.exp(-0.5 * r**2) + 
                          0.5 * np.sin(30 * r) * np.exp(-r**2) + 
                          0.3 * np.sin(50 * r) * np.exp(-2 * r**2))
        
        # Angular component with fractal-like structure and multiple interacting frequencies
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Multiple angular frequencies with chaotic modulation
            for i in range(min(4, self.dim)):
                freq = (i + 1) * 7 + np.sin(i * 3.14159 / 4)
                angular += np.sin(freq * angles) * np.cos(freq * angles) * np.exp(-0.1 * i)
        
        # High-dimensional polynomial chaos with cross-terms
        poly_chaos = np.sum(x_scaled**4) + 0.3 * np.sum(x_scaled**3) + 0.1 * np.sum(x_scaled**2)
        
        # Cross-dimensional interaction terms creating complex landscape topology
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_scaled[i] * x_scaled[j]) / (1 + np.abs(x_scaled[i] - x_scaled[j]))
        
        # Add a small chaotic perturbation component
        chaos_perturb = 0.05 * np.sum(np.sin(20 * x_scaled) * np.cos(15 * x_scaled))
        
        # Combine all components with carefully tuned weights
        return (fractal_radial + 0.4 * angular + 0.3 * poly_chaos + 
                0.2 * cross_interaction + 0.1 * chaos_perturb + 0.001 * np.sum(x_scaled**5))